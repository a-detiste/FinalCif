
#REM execute me from the main directory

source venv/bin/activate

pip install pip -U

pip3 install -r requirements.txt

pyinstaller Finalcif_onefile.spec --clean -y

VER=$(cat tools/version.py |grep VERSION |cut -d ' ' -f 3)

mv dist/Finalcif dist/FinalCif-v"$VER"_opensuse

echo "FinalCif version ""$VER"" finished"