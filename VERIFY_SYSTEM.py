#!/usr/bin/env python3
"""
Pentis 0.8.1 - System Verification Script
Checks if all dependencies and assets are properly installed and configured
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Check Python version is 3.6+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print(f"❌ Python version too old: {version.major}.{version.minor}")
        print(f"   Required: Python 3.6+")
        return False
    print(f"✓ Python {version.major}.{version.minor} (OK)")
    return True

def check_pygame():
    """Check Pygame is installed"""
    try:
        import pygame
        print(f"✓ Pygame {pygame.__version__} (OK)")
        return True
    except ImportError:
        print("❌ Pygame not installed")
        print("   Install with: pip install pygame")
        return False

def check_cryptography():
    """Check cryptography is installed (optional)"""
    try:
        import cryptography
        print(f"✓ Cryptography {cryptography.__version__} (Optional feature available)")
        return True
    except ImportError:
        print("⚠ Cryptography not installed (optional, but recommended)")
        print("   Install with: pip install cryptography")
        return True  # Not required, just optional

def check_directories():
    """Check required directories exist"""
    base_dir = Path(__file__).parent

    checks = [
        (base_dir / "pentis", "Source code directory"),
        (base_dir / "pentis" / "graphics", "Graphics assets"),
        (base_dir / "pentis" / "sound", "Sound assets"),
    ]

    all_ok = True
    for path, name in checks:
        if path.exists():
            print(f"✓ {name}: {path}")
        else:
            print(f"❌ {name} NOT FOUND: {path}")
            all_ok = False

    return all_ok

def check_files():
    """Check critical game files exist"""
    base_dir = Path(__file__).parent / "pentis"

    checks = [
        "pentis_081_local.py",
        "game.py",
        "startMenu.py",
        "optMenu.py",
        "endMenu.py",
        "storage.py",
        "utils.py",
        "inoutput.py",
    ]

    all_ok = True
    for filename in checks:
        path = base_dir / filename
        if path.exists():
            size = path.stat().st_size
            print(f"✓ {filename} ({size} bytes)")
        else:
            print(f"❌ {filename} NOT FOUND")
            all_ok = False

    return all_ok

def check_assets():
    """Check essential graphics and sound files"""
    base_dir = Path(__file__).parent / "pentis"

    checks = [
        ("graphics/block00.png", "Game block sprite"),
        ("graphics/Prototype.ttf", "Game font"),
        ("sound/Pentis_v02.flac", "Background music"),
    ]

    all_ok = True
    for path, name in checks:
        full_path = base_dir / path
        if full_path.exists():
            size = full_path.stat().st_size / 1024  # KB
            print(f"✓ {name}: {size:.1f} KB")
        else:
            print(f"❌ {name} NOT FOUND: {path}")
            all_ok = False

    return all_ok

def check_imports():
    """Check all game modules can be imported"""
    base_dir = Path(__file__).parent / "pentis"
    sys.path.insert(0, str(base_dir))

    modules = [
        "storage",
        "utils",
        "inoutput",
        "startMenu",
        "optMenu",
        "game",
        "endMenu",
    ]

    all_ok = True
    for module in modules:
        try:
            __import__(module)
            print(f"✓ {module} imports OK")
        except Exception as e:
            print(f"❌ {module} import FAILED: {e}")
            all_ok = False

    return all_ok

def check_save_directory():
    """Check if Pentis save directory can be created"""
    pentis_dir = Path.home() / "Pentis"
    try:
        pentis_dir.mkdir(exist_ok=True)
        test_file = pentis_dir / ".writetest"
        test_file.write_text("test")
        test_file.unlink()
        print(f"✓ Save directory: {pentis_dir} (writable)")
        return True
    except Exception as e:
        print(f"⚠ Save directory may not be writable: {e}")
        return True  # Not critical

def main():
    print("\n" + "=" * 60)
    print("  PENTIS 0.8.1 BETA - System Verification")
    print("=" * 60 + "\n")

    checks = [
        ("Python Version", check_python_version),
        ("Pygame", check_pygame),
        ("Cryptography (Optional)", check_cryptography),
        ("Directories", check_directories),
        ("Game Files", check_files),
        ("Game Assets", check_assets),
        ("Module Imports", check_imports),
        ("Save Directory", check_save_directory),
    ]

    results = []
    for name, check_func in checks:
        print(f"\n{name}:")
        print("-" * 40)
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"ERROR during check: {e}")
            results.append((name, False))

    print("\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, r in results if r)
    total = len(results)

    for name, result in results:
        status = "✓" if result else "✗"
        print(f"{status} {name}")

    print(f"\nPassed: {passed}/{total}")

    if passed == total:
        print("\n✓ System is ready! Run the game with:")
        print("  bash RUN_GAME.sh  (macOS/Linux)")
        print("  RUN_GAME.bat      (Windows)")
        print("  python3 pentis/pentis_081_local.py")
        return 0
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
