SOURCE="https://repo.skype.com/latest/skypeforlinux-64.deb"
DESTINATION="build.deb"
OUTPUT="Skype.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION) -c $(SOURCE)
	
	dpkg -x $(DESTINATION) build
	rm -rf AppDir/opt
	
	mkdir --parents AppDir/opt/application
	mv build/usr/share/skypeforlinux/* AppDir/opt/application

	chmod +x AppDir/AppRun

	appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -f $(DESTINATION)
	rm -rf AppDir/opt
	rm -rf build
