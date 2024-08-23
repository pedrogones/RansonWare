# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

# Análise dos módulos necessários
a = Analysis(
    ['ransonware.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pyAesCrypt', 'requests', 'tkinter'],  # Adicione tkinter aqui
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# Adiciona arquivos e dependências adicionais ao pacote
pyz = PYZ(a.pure)

# Criação do executável
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ransonware',
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
)
