# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

sys.path.append(str(Path.cwd()))

from spec.insert_version import write_version
write_version()

block_cipher = None


a = Analysis(['../Windows.py'],
             pathex=['Scripts'],
             binaries=[],
             datas=[('../Scripts', 'Scripts'), ('../resources', 'resources')],
             hiddenimports=['msvcrt', 'win32com', 'win32api', 'wmi'],
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
          name='Windows',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
