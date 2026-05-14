# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pentis/pentis_081_local.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('pentis/graphics', 'graphics/'),
        ('pentis/graphics/title3.png', '.'),
        ('pentis/colors.py', '.'),
        ('pentis/inoutput.py', '.'),
        # ('pentis/username.txt', '.'),    # file no longer exists — commented out
        ('pentis/sound', 'sound/'),
        ('pentis/endMenu.py', '.'),
        ('pentis/game.py', '.'),
        ('pentis/optMenu.py', '.'),
        ('pentis/startMenu.py', '.'),
        ('pentis/utils.py', '.'),
    ],
    hiddenimports=[
        'cryptography.fernet',
        'cryptography.hazmat.primitives.kdf.pbkdf2',
        'pygame',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['pentis/runtime_hook_paths.py'],
    excludes=['PyQt5', 'firebase_admin'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Pentis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # no terminal window when sharing
    # console=True,         # uncomment for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['pentis/block_ico.ico'],
)

# ── macOS .app bundle — not used on Windows, kept for reference ──────────────
# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     name='Pentis',
# )
#
# app = BUNDLE(
#     coll,
#     name='Pentis.app',
#     icon=None,
#     bundle_identifier='com.grapefruit256.pentis',
#     info_plist={
#         'NSHighResolutionCapable': True,
#         'CFBundleShortVersionString': '0.81',
#     },
# )
