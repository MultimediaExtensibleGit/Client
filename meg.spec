# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src/main.py'],
             pathex=['.'],
             binaries=[],
             datas=[
               ('./src/runtime/meg_runtime', 'runtime/meg_runtime'),
               ('./src/meg.kv', '.')
             ],
             hiddenimports=['pip', 'pkg_resources.py2_warn', 'pygit2'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='meg',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='src/images/meg.ico')
