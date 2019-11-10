SOURCE="https://pencil.evolus.vn/dl/development/Pencil-3.1.0.20191109003003.tar.gz"
DESTINATION="build.tar.bz2"
OUTPUT="Pencil.AppImage"


all:
	echo "Building: $(OUTPUT)"
	wget -O $(DESTINATION)  $(SOURCE)
	
	tar -zxvf $(DESTINATION)
	rm -rf AppDir/opt
	
	mkdir --parents AppDir/opt/application
	mv pencil-3.1.0.20191109003003/* AppDir/opt/application

	chmod +x AppDir/AppRun

	appimagetool AppDir $(OUTPUT)

	chmod +x $(OUTPUT)

	rm -rf pencil-3.1.0.20191109003003
	rm -f $(DESTINATION)
	rm -rf AppDir/opt

