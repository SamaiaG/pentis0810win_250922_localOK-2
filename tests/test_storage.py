"""
Tests for storage.py — highscore persistence and encryption.

Run from the project root:
    python3 -m pytest tests/
"""
import sys
import os
import json
import pytest
from pathlib import Path
from unittest.mock import patch

# Make storage importable without needing to be inside pentis/
sys.path.insert(0, str(Path(__file__).parent.parent / 'pentis'))
import storage


# ─────────────────────────────────────────────
# Encrypt / Decrypt
# ─────────────────────────────────────────────

def test_encrypt_decrypt_roundtrip():
    """Data survives an encrypt → decrypt cycle unchanged."""
    data = {"Standard": {"Alice": {"score": 5000}}}
    assert storage.decrypt_data(storage.encrypt_data(data)) == data


def test_decrypt_garbage_returns_empty():
    """Corrupted data returns {} instead of crashing."""
    assert storage.decrypt_data(b"this is not valid encrypted data") == {}


def test_encrypt_produces_bytes():
    assert isinstance(storage.encrypt_data({"x": 1}), bytes)


# ─────────────────────────────────────────────
# readHighscoresJS
# ─────────────────────────────────────────────

def test_read_returns_empty_when_file_missing(tmp_path):
    """No file → empty dict, no crash."""
    with patch.object(storage, 'file_path', str(tmp_path / 'highscores.json')):
        assert storage.readHighscoresJS() == {}


def test_read_returns_empty_on_empty_file(tmp_path):
    """Empty file → empty dict."""
    f = tmp_path / 'highscores.json'
    f.write_bytes(b'')
    with patch.object(storage, 'file_path', str(f)):
        assert storage.readHighscoresJS() == {}


# ─────────────────────────────────────────────
# addHighscoresJS — mode validation
# ─────────────────────────────────────────────

def test_invalid_mode_raises_value_error(tmp_path):
    with patch.object(storage, 'file_path', str(tmp_path / 'hs.json')):
        with pytest.raises(ValueError):
            storage.addHighscoresJS(99, 'Alice', 1000)


def test_all_valid_modes_accepted(tmp_path):
    """Modes 9, 11, 12, 13 all save without error."""
    fake = str(tmp_path / 'hs.json')
    with patch.object(storage, 'file_path', fake):
        storage.addHighscoresJS(9,  'A', 100)
        storage.addHighscoresJS(11, 'B', 200)
        storage.addHighscoresJS(12, 'C', 300)
        storage.addHighscoresJS(13, 'D', 400)
        result = storage.readHighscoresJS()
    assert set(result.keys()) == {'Novice', 'Standard', 'Advanced', 'Pro'}


# ─────────────────────────────────────────────
# addHighscoresJS — score logic
# ─────────────────────────────────────────────

def test_new_score_is_saved(tmp_path):
    fake = str(tmp_path / 'hs.json')
    with patch.object(storage, 'file_path', fake):
        storage.addHighscoresJS(11, 'Alice', 5000)
        assert storage.readHighscoresJS()['Standard']['Alice']['score'] == 5000


def test_higher_score_replaces_existing(tmp_path):
    fake = str(tmp_path / 'hs.json')
    with patch.object(storage, 'file_path', fake):
        storage.addHighscoresJS(11, 'Alice', 3000)
        storage.addHighscoresJS(11, 'Alice', 8000)
        assert storage.readHighscoresJS()['Standard']['Alice']['score'] == 8000


def test_lower_score_does_not_replace(tmp_path):
    fake = str(tmp_path / 'hs.json')
    with patch.object(storage, 'file_path', fake):
        storage.addHighscoresJS(11, 'Alice', 8000)
        storage.addHighscoresJS(11, 'Alice', 3000)
        assert storage.readHighscoresJS()['Standard']['Alice']['score'] == 8000


def test_equal_score_does_not_replace(tmp_path):
    fake = str(tmp_path / 'hs.json')
    with patch.object(storage, 'file_path', fake):
        storage.addHighscoresJS(11, 'Alice', 5000)
        storage.addHighscoresJS(11, 'Alice', 5000)
        assert storage.readHighscoresJS()['Standard']['Alice']['score'] == 5000


def test_multiple_players_stored_independently(tmp_path):
    fake = str(tmp_path / 'hs.json')
    with patch.object(storage, 'file_path', fake):
        storage.addHighscoresJS(11, 'Alice',   5000)
        storage.addHighscoresJS(11, 'Bob',     3000)
        storage.addHighscoresJS(11, 'Charlie', 8000)
        scores = storage.readHighscoresJS()['Standard']
    assert scores['Alice']['score']   == 5000
    assert scores['Bob']['score']     == 3000
    assert scores['Charlie']['score'] == 8000


def test_scores_persist_across_calls(tmp_path):
    """Saving in one call and reading in the next returns the same data."""
    fake = str(tmp_path / 'hs.json')
    with patch.object(storage, 'file_path', fake):
        storage.addHighscoresJS(12, 'Martin', 9999)
    with patch.object(storage, 'file_path', fake):
        result = storage.readHighscoresJS()
    assert result['Advanced']['Martin']['score'] == 9999


def test_scores_across_modes_dont_interfere(tmp_path):
    fake = str(tmp_path / 'hs.json')
    with patch.object(storage, 'file_path', fake):
        storage.addHighscoresJS(11, 'Alice', 1000)   # Standard
        storage.addHighscoresJS(12, 'Alice', 2000)   # Advanced
        result = storage.readHighscoresJS()
    assert result['Standard']['Alice']['score']  == 1000
    assert result['Advanced']['Alice']['score']  == 2000


# ─────────────────────────────────────────────
# get_app_data_dir
# ─────────────────────────────────────────────

def test_data_dir_is_a_nonempty_string():
    result = storage.get_app_data_dir()
    assert isinstance(result, str) and len(result) > 0


def test_data_dir_contains_pentis():
    """The path should always include 'Pentis' or 'pentis'."""
    assert 'entis' in storage.get_app_data_dir()


def test_data_dir_windows(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Windows')
    monkeypatch.setenv('LOCALAPPDATA', 'C:\\Users\\Test\\AppData\\Local')
    result = storage.get_app_data_dir()
    assert 'Pentis' in result and 'AppData' in result


def test_data_dir_mac(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Darwin')
    result = storage.get_app_data_dir()
    assert 'Application Support' in result


def test_data_dir_linux(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Linux')
    result = storage.get_app_data_dir()
    assert '.local' in result
