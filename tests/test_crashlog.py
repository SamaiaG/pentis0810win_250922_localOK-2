"""
Tests for crashlog.py — uncaught exceptions are written to crash.log.

Run from the project root:
    python3 -m pytest tests/test_crashlog.py -v
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'pentis'))
import crashlog


def _raise_and_log(message):
    try:
        raise ValueError(message)
    except ValueError:
        crashlog.write_crash_log(*sys.exc_info())


def test_crash_is_written_to_log(tmp_path, monkeypatch):
    monkeypatch.setattr(crashlog, 'get_app_data_dir', lambda: str(tmp_path))
    _raise_and_log("boom")
    log = (tmp_path / 'crash.log').read_text(encoding='utf-8')
    assert "Pentis crash" in log
    assert "ValueError: boom" in log


def test_crashes_are_appended(tmp_path, monkeypatch):
    monkeypatch.setattr(crashlog, 'get_app_data_dir', lambda: str(tmp_path))
    _raise_and_log("first")
    _raise_and_log("second")
    log = (tmp_path / 'crash.log').read_text(encoding='utf-8')
    assert "first" in log and "second" in log


def test_oversized_log_is_restarted(tmp_path, monkeypatch):
    monkeypatch.setattr(crashlog, 'get_app_data_dir', lambda: str(tmp_path))
    monkeypatch.setattr(crashlog, 'MAX_LOG_BYTES', 10)
    (tmp_path / 'crash.log').write_text("old contents " * 10, encoding='utf-8')
    _raise_and_log("fresh")
    log = (tmp_path / 'crash.log').read_text(encoding='utf-8')
    assert "old contents" not in log and "fresh" in log


def test_missing_data_dir_is_created(tmp_path, monkeypatch):
    target = tmp_path / 'not' / 'there'
    monkeypatch.setattr(crashlog, 'get_app_data_dir', lambda: str(target))
    _raise_and_log("boom")
    assert (target / 'crash.log').exists()


def test_unwritable_location_does_not_raise(monkeypatch):
    monkeypatch.setattr(crashlog, 'crash_log_path', lambda: '/dev/null/crash.log')
    _raise_and_log("boom")   # must swallow the OSError


def test_install_sets_excepthook(monkeypatch):
    monkeypatch.setattr(sys, 'excepthook', sys.__excepthook__)
    crashlog.install()
    assert sys.excepthook is crashlog._excepthook
