SOURCE="https://download.sublimetext.com/sublime_text_3_build_3211_x64.tar.bz2"
DESTINATION="build.tar.bz2"
OUTPUT="Sublime-Text.AppImage"

all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION) -c $(SOURCE)

	tar -jxvf $(DESTINATION)
	rm -rf AppDir/opt

	mkdir --parents AppDir/opt/application
	cp -r sublime_text_3/* AppDir/opt/application

	chmod +x AppDir/AppRun

	export ARCH=x86_64 && appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -f $(DESTINATION)
	rm -rf AppDir/opt
	rm -rf sublime_text_3
