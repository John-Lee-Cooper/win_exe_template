# -*- mode: python -*-

block_cipher = None

a = Analysis(['search.py'],
             pathex=['C:\\Users\\lee.cooper\\Desktop\\search'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          Tree('rsrc', prefix='rsrc'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='search',
          debug=False,
          strip=False,
          upx=False,
          console=True )
