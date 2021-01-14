set name=search

del %name%.exe

call venv\Scripts\activate
copy rsrc\%name%.spec %name%.spec

pyinstaller.exe %name%.spec
rem pyinstaller.exe --onefile %name%.py --noupx
move /y dist\%name%.exe %name%.exe

del *.spec *.pyc
rd /s /q  build
rd /s /q  dist
rd /s /q  __pycache__
