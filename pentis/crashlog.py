"""Crash logging - writes uncaught exceptions to crash.log in the Pentis data folder.

Standard library only, so it can be installed before pygame or any game module
is imported and still catch errors raised while those imports run.
"""
import os
import sys
import platform
import traceback
from datetime import datetime

MAX_LOG_BYTES = 1_000_000   # start a fresh log once it grows past ~1 MB


# Get platform-specific data directory
def get_app_data_dir():
    """Return platform-specific application data directory"""
    system = platform.system()

    if system == 'Windows':
        # Windows: C:\Users\<username>\AppData\Local\Pentis
        app_data = os.getenv('LOCALAPPDATA')
        if app_data:
            return os.path.join(app_data, 'Pentis')
        else:
            return os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Pentis')
    elif system == 'Darwin':
        # macOS: ~/Library/Application Support/Pentis
        return os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Pentis')
    else:
        # Linux and others: ~/.local/share/pentis
        return os.path.join(os.path.expanduser('~'), '.local', 'share', 'pentis')


def crash_log_path():
    return os.path.join(get_app_data_dir(), 'crash.log')


def write_crash_log(exc_type, exc_value, exc_tb):
    """Append one crash report to crash.log. Never raises."""
    try:
        path = crash_log_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        mode = 'w' if os.path.exists(path) and os.path.getsize(path) > MAX_LOG_BYTES else 'a'
        with open(path, mode, encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write(f"Pentis crash  {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            f.write(f"OS: {platform.platform()}  |  Python {platform.python_version()}"
                    f"  |  {'app build' if getattr(sys, 'frozen', False) else 'source'}\n\n")
            traceback.print_exception(exc_type, exc_value, exc_tb, file=f)
            f.write("\n")
    except Exception:
        pass


def _excepthook(exc_type, exc_value, exc_tb):
    if not issubclass(exc_type, KeyboardInterrupt):
        write_crash_log(exc_type, exc_value, exc_tb)
    sys.__excepthook__(exc_type, exc_value, exc_tb)


def install():
    """Route uncaught exceptions to crash.log (and still print them to the console)."""
    sys.excepthook = _excepthook
