#!/usr/bin/env sh
set -eu
export PATH_BLOODIED_DEV=0
python -m pip install -e . 'pyinstaller>=6,<7'
python -m PyInstaller --noconfirm --clean PathOfTheBloodiedOne.spec
