
#REM execute me from the main directory

source venv/bin/activate

pip install pip -U

pip3 install -r requirements.txt

pyinstaller Finalcif_mac.spec --clean -y

VER=$(cat tools/version.py |grep VERSION |cut -d ' ' -f 3)

mv dist/Finalcif-v_macos.app dist/Finalcif-v"$VER"_macos.app

cd dist || exit
rm finalcif

zip -rm Finalcif-v"$VER"_macos.app.zip Finalcif-v"$VER"_macos.app/

echo "FinalCif version ""$VER"" finished"