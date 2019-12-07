sudo apt-get download mysql-workbench libproj12
for i in $(apt-cache depends mysql-workbench | grep -E 'Hängt ab von:' | cut -d ':' -f 2,3 | sed -e s/'<'/''/ -e s/'>'/''/); do sudo apt-get download $i 2>>errors.txt; done
for i in $(ls -a | grep deb ); do dpkg-deb -x $i lib ; done
rm -rf ../AppDir/lib/*
rm -rf ../AppDir/opt/application/*

mkdir -p  ../AppDir/lib
mkdir -p  ../AppDir/opt/application

cp -r lib/lib/x86_64-linux-gnu/* ../AppDir/lib
cp -r lib/usr ../AppDir/
rm -f *.deb
rm -rf lib errors.txt
