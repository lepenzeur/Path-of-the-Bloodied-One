@echo off
setlocal
set PATH_BLOODIED_DEV=0
python -m pip install -e . "pyinstaller>=6,<7"
if errorlevel 1 exit /b 1
python -m PyInstaller --noconfirm --clean PathOfTheBloodiedOne.spec
if errorlevel 1 exit /b 1
echo Build output: dist\PathOfTheBloodiedOne
