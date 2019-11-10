SOURCE="https://download.jetbrains.com/cpp/CLion-2019.2.5.tar.gz"
DESTINATION="build.tar.bz2"
OUTPUT="CLion.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION)  $(SOURCE)
	
	tar -zxvf $(DESTINATION)
	rm -rf AppDir/opt
	
	mkdir --parents AppDir/opt/application
	mv clion-2019.2.5/* AppDir/opt/application

	chmod +x AppDir/AppRun
	export ARCH=x86_64; appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -rf clion-2019.2.5
	rm -f $(DESTINATION)
	rm -rf AppDir/opt

