import sys
sys.platform = 'linux'  # Force Linux platform

a = Analysis(
    ['app/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    target_arch='aarch64'  # Set target architecture
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='minecraft-schematic-generator-termux',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='aarch64',
    codesign_identity=None,
    entitlements_file=None,
)
