SOURCE="https://download.jetbrains.com/webide/PhpStorm-2019.3.tar.gz"
DESTINATION="build.tar.bz2"
OUTPUT="PhpStorm.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION)  $(SOURCE)

	tar -zxvf $(DESTINATION)
	rm -rf AppDir/opt

	mkdir --parents AppDir/opt/application
	cp -r PhpStorm-193.5233.101/* AppDir/opt/application

	chmod +x AppDir/AppRun
	export ARCH=x86_64; appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -rf PhpStorm-193.5233.101
	rm -f $(DESTINATION)
	rm -rf AppDir/opt
