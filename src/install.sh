mkdir -p ../installer/usr/share/tractorator 2>/dev/null
cp  math_lib.py ../installer/usr/share/tractorator/math_lib.py
cp  main.py ../installer/usr/share/tractorator/main.py && chmod +x ../installer/usr/share/tractorator/main.py
cp  ../screenshot.png ../installer/usr/share/tractorator/screenshot.png
cp  expresion_eval.py ../installer/usr/share/tractorator/expresion_eval.py
mkdir -p ../installer/usr/local/bin/ 2>/dev/null
ln -sf /usr/share/tractorator/main.py ../installer/usr/local/bin/tractorator_calculator
mkdir ../installer/tmp 2>/dev/null
cp requirements.txt ../installer/tmp/requirements.txt
chmod +x ../installer/DEBIAN/postinst
dpkg-deb --build ../installer/ ../installer/installer.deb
