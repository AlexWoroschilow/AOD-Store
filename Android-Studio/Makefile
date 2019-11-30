SOURCE="https://dl.google.com/dl/android/studio/ide-zips/3.5.2.0/android-studio-ide-191.5977832-linux.tar.gz"
DESTINATION="build.tar.gz"
OUTPUT="Android-Studio.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION)  $(SOURCE)

	tar -zxvf $(DESTINATION)
	rm -rf AppDir/opt

	mkdir --parents AppDir/opt/application
	mv android-studio/* AppDir/opt/application

	chmod +x AppDir/AppRun
	export ARCH=x86_64 && appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -rf android-studio
	rm -f $(DESTINATION)
	rm -rf AppDir/opt
