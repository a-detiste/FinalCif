
REM execute me from the main directory

rmdir /S dist /Q

CALL venv\Scripts\activate.bat

git pull

venv\Scripts\python -m pip install -U pip
venv\Scripts\python -m pip install wheel
venv\Scripts\python -m pip install -U pyinstaller

venv\Scripts\pip3.exe install -r requirements.txt -U

venv\Scripts\python.exe scripts\make_win_release.py