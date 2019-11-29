SOURCE="https://atom-installer.github.com/v1.41.0/atom-amd64.deb?s=1571754160&ext=.deb"
DESTINATION="build.deb"
OUTPUT="Atom.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION) -c $(SOURCE)
	
	dpkg -x $(DESTINATION) build
	rm -rf AppDir/opt
	
	mkdir --parents AppDir/opt/application
	mv build/usr/share/atom/* AppDir/opt/application

	chmod +x AppDir/AppRun

	appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -f $(DESTINATION)
	rm -rf AppDir/opt
	rm -rf build
