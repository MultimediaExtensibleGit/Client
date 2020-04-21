# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os
import importlib

package_imports = [['meg_runtime', ['ui/*.ui', 'ui/images/*.svg']]]

datas = []
for package, files in package_imports:
    proot = os.path.dirname(importlib.import_module(package).__file__)
    datas.extend((os.path.join(proot, f), os.path.join(package, os.path.dirname(f))) for f in files)

a = Analysis(['src/main.py'],
             pathex=['.'],
             binaries=[],
             datas=datas,
             hiddenimports=['pip', 'pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='meg',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon='src/images/meg.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='meg')
