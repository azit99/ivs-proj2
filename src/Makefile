
.PHONY: all	doc tests run requirements

#runs the calculator
all: 
	python3 gui.py

#runs the calculator
run: 
	python3 gui.py

#runs profiling
profile:
	python3 profiling.py

#generate documentation
doc:
	doxygen Doxyfile

#run matlib tests
tests: 
	pytest --verbose

#install requirements
requirements:
	pip3 install -r requirements.txt

#packs project
pack: doc createfolder xzitna02_xzitna03_xdudik01_xotcen01.zip
xzitna02_xzitna03_xdudik01_xotcen01.zip:
	rm -rf ../../xzitna02_xzitna03_xdudik01_xotcen01/repo/install
	rm -rf ../../xzitna02_xzitna03_xdudik01_xotcen01/repo/doc	
	cd ../.. && zip -r $@ xzitna02_xzitna03_xdudik01_xotcen01
	
createfolder:
	mkdir -p ../../xzitna02_xzitna03_xdudik01_xotcen01/repo
	mkdir ../../xzitna02_xzitna03_xdudik01_xotcen01/install
	mkdir ../../xzitna02_xzitna03_xdudik01_xotcen01/doc
	cp -a ../../ivs-proj2/. ../../xzitna02_xzitna03_xdudik01_xotcen01/repo/
	cp -a ../doc/. ../../xzitna02_xzitna03_xdudik01_xotcen01/doc/
	cp -a ../install/. ../../xzitna02_xzitna03_xdudik01_xotcen01/install/

#remove unnecesary files
clean: 
	rm -rf ../install/usr/ ../install/ ../../xzitna02_xzitna03_xdudik01_xotcen01


