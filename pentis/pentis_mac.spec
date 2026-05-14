# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for Pentis (macOS)
# Place this file in your project root (same folder as pentis_081_local.py)

block_cipher = None

a = Analysis(
    ['pentis_081_local.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('graphics', 'graphics'),   # bundles entire graphics/ folder
        ('sound', 'sound'),          # bundles entire sound/ folder
    ],
    hiddenimports=[
        'pygame',
        'numpy',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['runtime_hook_paths.py'],
    excludes=[
        'PyQt5',        # not needed at runtime, keeps build smaller
        'firebase_admin',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Pentis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # no terminal window
    disable_windowed_traceback=False,
    target_arch=None,          # arm64 (Apple Silicon M1/M2/M3/M4)
    codesign_identity=None,
    entitlements_file=None,
    icon='graphics/Pentis.icns',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Pentis',
)

app = BUNDLE(
    coll,
    name='Pentis.app',
    icon=None,              # set to a .icns file path if you have one
    bundle_identifier='com.grapefruit256.pentis',
    info_plist={
        'NSHighResolutionCapable': True,
        'CFBundleShortVersionString': '0.81',
    },
)
