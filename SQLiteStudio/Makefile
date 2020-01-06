SOURCE="https://github.com/pawelsalawa/sqlitestudio/releases/download/3.2.1/sqlitestudio-3.2.1.tar.xz"
DESTINATION="build.tar.xz"
OUTPUT="SQLiteStudio.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION) -c $(SOURCE)

	tar -xJf $(DESTINATION)
	rm -rf AppDir/opt

	mkdir --parents AppDir/lib
	mkdir --parents AppDir/opt/application

	cp -r lib/* AppDir/lib
	cp -r SQLiteStudio/lib/* AppDir/lib
	cp -r SQLiteStudio/* AppDir/opt/application
	rm -rf AppDir/opt/application/lib

	chmod +x AppDir/AppRun

	export ARCH=x86_64 && appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -f $(DESTINATION)
	rm -rf SQLiteStudio
	rm -rf AppDir/lib
	rm -rf AppDir/opt
