set -x

sudo apt-get download sqlitebrowser
for i in $(apt-cache depends sqlitebrowser | grep -E 'Hängt ab von:' | cut -d ':' -f 2,3 | sed -e s/'<'/''/ -e s/'>'/''/); do sudo apt-get download $i 2>>errors.txt; done
for i in $(ls -a | grep deb ); do dpkg-deb -x $i lib ; done
rm -rf ../AppDir/lib/*
rm -rf ../AppDir/opt/application/*

mkdir -p ../AppDir/lib
mkdir -p ../AppDir/opt/application


cp -r lib/usr/lib/x86_64-linux-gnu/* ../AppDir/lib
cp -r lib/usr/lib/* ../AppDir/lib

rm -rf ../AppDir/lib/x86_64-linux-gnu

cp -r lib/usr/bin/* ../AppDir/opt/application
rm -f *.deb
rm -rf lib errors.txt
