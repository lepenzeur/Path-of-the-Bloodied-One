@echo off
setlocal
python -m pip install -r requirements-dev.txt
python -m PyInstaller --noconfirm --clean --windowed --name "PathOfTheBloodiedOne" ^
  --add-data "assets;assets" ^
  --add-data "core;core" ^
  --add-data "characters;characters" ^
  --add-data "gameplay;gameplay" ^
  --add-data "ui;ui" ^
  main.py
echo Build output: dist\PathOfTheBloodiedOne
