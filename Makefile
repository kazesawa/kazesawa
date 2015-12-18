SOURCE_SANS_PRO_URL = https://codeload.github.com/adobe-fonts/source-sans-pro/zip/2.020R-ro/1.075R-it
SOURCE_SANS_PRO_DIR = source-sans-pro-2.020R-ro-1.075R-it
MPLUS_URL = http://jaist.dl.osdn.jp/mplus-fonts/62344/mplus-TESTFLIGHT-060.tar.xz
MPLUS_DIR = mplus-TESTFLIGHT-060

.DEFAULT_GOAL := release
.PHONY: fetch_deps ttf zip release clean clean_deps

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
	zip -r kazesawa.zip out/ README.md

fresh: | fetch_deps ttf zip

clean:
	rm -r out/
	rm kazesawa.zip

clean_deps:
	rm -r deps/

clean_all: | clean clean_deps
