SOURCE="https://download.mozilla.org/?product=thunderbird-latest&os=linux64"
DESTINATION="build.tar.bz2"
OUTPUT="Thunderbird.AppImage"

all: 
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION)  $(SOURCE)
	
	tar -jxvf $(DESTINATION)
	rm -rf AppDir/opt
	
	mkdir --parents AppDir/opt/application
	mv thunderbird/* AppDir/opt/application
	

	chmod +x AppDir/AppRun

	appimagetool AppDir $(OUTPUT)
	

	chmod +x $(OUTPUT)

	rm -f $(DESTINATION)
	rm -rf AppDir/opt
	rm -rf thunderbird

