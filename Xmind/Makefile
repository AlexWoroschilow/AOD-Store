SOURCE="https://dl3.xmind.net/xmind-8-update8-linux.zip"
DESTINATION="build.zip"
OUTPUT="XMind-8.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION) -c $(SOURCE)

	rm -rf AppDir/opt
	mkdir --parents AppDir/opt/application
	mkdir --parents xmind
	
	unzip $(DESTINATION) -d xmind
	
	mv xmind/XMind_amd64/* AppDir/opt/application
	mv xmind/plugins AppDir/opt/application
	mv xmind/features AppDir/opt/application
	mv xmind/fonts  AppDir/opt/application
	cp XMind.ini  AppDir/opt/application

	chmod +x AppDir/AppRun

	export ARCH=x86_64; appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -rf xmind
	rm -f $(DESTINATION)
	rm -rf AppDir/opt

