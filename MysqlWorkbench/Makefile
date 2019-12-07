DESTINATION="build.deb"
OUTPUT="MySQL-Workbench.AppImage"


all:
	echo "Building: $(OUTPUT)"

	mkdir --parents AppDir/opt/application

	chmod +x AppDir/AppRun

	appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -f $(DESTINATION)
	rm -rf AppDir/opt
	rm -rf AppDir/lib
	rm -rf AppDir/usr
	rm -rf build
