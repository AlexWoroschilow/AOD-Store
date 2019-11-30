SOURCE="https://downloads.mongodb.com/compass/mongodb-compass-community_1.19.12_amd64.deb"
DESTINATION="build.deb"
OUTPUT="MongoDB-Compass.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION) -c $(SOURCE)

	dpkg -x $(DESTINATION) build
	rm -rf AppDir/opt

	mkdir --parents AppDir/opt/application
	cp -r build/usr/share/mongodb-compass-community/* AppDir/opt/application

	chmod +x AppDir/AppRun

	export ARCH=x86_64 && appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -f $(DESTINATION)
	rm -rf AppDir/opt
	rm -rf build
