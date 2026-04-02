# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pentis/pentis_081_local.py'],
    pathex=[],
    binaries=[],
    datas=[('pentis/graphics', 'graphics/'), ('pentis/graphics/title3.png', '.'), ('pentis/colors.py', '.'), ('pentis/inoutput.py', '.'), ('pentis/username.txt', '.'), ('pentis/sound', 'sound/'), ('pentis/endMenu.py', '.'), ('pentis/game.py', '.'), ('pentis/optMenu.py', '.'), ('pentis/startMenu.py', '.'), ('pentis/utils.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='pentis_081_local',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['pentis/block_ico.ico'],
)
