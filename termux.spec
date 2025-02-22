import os
import sys
sys.platform = 'linux'

a = Analysis(
    ['app/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'termux',
    ],
    hookspath=['hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

# Force AArch64 architecture
a.binaries = [(x, y, z) for (x, y, z) in a.binaries if not x.startswith('libpython')]

pyz = PYZ(a.pure, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    exclude_binaries=False,
    name='minecraft-schematic-generator-termux',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='aarch64',
    runtime_tmpdir=None,
    codesign_identity=None,
    entitlements_file=None,
)
