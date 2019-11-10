SOURCE="https://download-installer.cdn.mozilla.net/pub/firefox/releases/70.0.1/linux-x86_64/de/firefox-70.0.1.tar.bz2"
DESTINATION="build.tar.bz2"
OUTPUT="Firefox.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION)  $(SOURCE)
	
	tar -jxvf $(DESTINATION)
	rm -rf AppDir/opt
	
	mkdir --parents AppDir/opt/application
	mv firefox/* AppDir/opt/application

	chmod +x AppDir/AppRun

	appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -f $(DESTINATION)
	rm -rf AppDir/opt
	rm -rf firefox
