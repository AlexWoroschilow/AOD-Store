SOURCE="https://download.jetbrains.com/ruby/RubyMine-2019.3.tar.gz"
DESTINATION="build.tar.bz2"
OUTPUT="RubyMine.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION) -c $(SOURCE)

	tar -zxvf $(DESTINATION)
	rm -rf AppDir/opt

	mkdir --parents AppDir/opt/application
	cp -r RubyMine-2019.3/* AppDir/opt/application

	chmod +x AppDir/AppRun
	export ARCH=x86_64; appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -rf RubyMine-2019.3
	rm -f $(DESTINATION)
	rm -rf AppDir/opt
