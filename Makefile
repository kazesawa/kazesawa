SOURCE_SANS_PRO_URL = https://codeload.github.com/adobe-fonts/source-sans-pro/zip/2.020R-ro/1.075R-it
SOURCE_SANS_PRO_DIR = source-sans-pro-2.020R-ro-1.075R-it
MPLUS_URL = http://jaist.dl.osdn.jp/mplus-fonts/62344/mplus-TESTFLIGHT-060.tar.xz
MPLUS_DIR = mplus-TESTFLIGHT-060

.DEFAULT_GOAL := release
.PHONY: fetch_deps ttf zip release clean clean_deps samples

fetch_deps:
	test -d deps || mkdir deps
	curl -o deps/source_sans_pro.zip $(SOURCE_SANS_PRO_URL)
	unzip deps/source_sans_pro.zip -d deps/
	curl -o deps/mplus.tar.xz $(MPLUS_URL)
	tar	xvf deps/mplus.tar.xz -C deps/

ttf:
	test -d out || mkdir out
	python generate_ttf.py ./deps/$(SOURCE_SANS_PRO_DIR)/OTF/ ./deps/$(MPLUS_DIR)/

zip:
	test -d out/mplus || mkdir -p out/mplus
	test -d out/source-sans-pro || mkdir -p out/source-sans-pro
	cp deps/$(MPLUS_DIR)/{LICENSE,README}_{E,J}  out/mplus/
	cp deps/$(SOURCE_SANS_PRO_DIR)/{LICENSE.txt,README.md} out/source-sans-pro/
	cp release_readme.txt out/README.txt
	cp LICENSE.txt out/
	cd out/ && zip -r ../kazesawa.zip . -x "*.sfd"

fresh: | fetch_deps ttf zip

clean:
	rm -r out/
	rm kazesawa.zip

clean_deps:
	rm -r deps/

clean_all: | clean clean_deps

samples:
	find samples/ -name '*.svg' -exec inkscape -z -A {}.pdf -d 72 {} \; -exec pdftocairo -r 72 -png {}.pdf {}.png \;
	rm samples/*.pdf
	rename -v svg\.png-1\.png png samples/*
