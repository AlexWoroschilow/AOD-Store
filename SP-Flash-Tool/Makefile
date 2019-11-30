USER_AGENT="Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"
SOURCE="https://spflashtool.com/download/SP_Flash_Tool-5.1916_Linux.zip"
DESTINATION="build.zip"
OUTPUT="SPFlash-Tool.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget --user-agent=${USER_AGENT} \
	--header="Referer: https://spflashtool.com/download/" \
	-O $(DESTINATION) -c $(SOURCE)

	wget -O libpng12.deb \
	-c http://security.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1.1_amd64.deb

	mkdir --parents AppDir/opt/application
	mkdir --parents AppDir/lib

	unzip $(DESTINATION) -d ./
	dpkg -x libpng12.deb libpng12

	cp -r SP_Flash_Tool-5.1916_Linux/lib/* AppDir/lib
	rm -rf SP_Flash_Tool-5.1916_Linux/lib
	cp -r SP_Flash_Tool-5.1916_Linux/*.so AppDir/lib
	cp -r SP_Flash_Tool-5.1916_Linux/* AppDir/opt/application
	cp -r libpng12/lib/x86_64-linux-gnu/* AppDir/lib

	chmod +x AppDir/opt/application/flash_tool.sh
	chmod +x AppDir/opt/application/flash_tool
	chmod +x AppDir/AppRun

	export ARCH=x86_64 && appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -rf SP_Flash_Tool-5.1916_Linux
	rm -f $(DESTINATION)
	rm -rf AppDir/lib
	rm -rf AppDir/opt
	rm -rf libpng12.deb
	rm -rf libpng12
