SOURCE_SANS_PRO_DIR = source-sans-pro-2.020R-ro-1.075R-it
MPLUS_DIR = mplus-TESTFLIGHT-060

.DEFAULT_GOAL := ttf
.PHONY: ttf clean

fetch_deps:
	test -d deps || mkdir deps
	curl -o deps/source_sans_pro.zip https://codeload.github.com/adobe-fonts/source-sans-pro/zip/2.020R-ro/1.075R-it
	unzip deps/source_sans_pro.zip -d deps/
	curl -o deps/mplus.tar.xz http://jaist.dl.osdn.jp/mplus-fonts/62344/mplus-TESTFLIGHT-060.tar.xz
	tar	xvf deps/mplus.tar.xz -C deps/

ttf:
	test -d out || mkdir out
	python generate_ttf.py ./deps/$(SOURCE_SANS_PRO_DIR)/OTF/ ./deps/$(MPLUS_DIR)/

zip:
	zip -r kazesawa.zip out/ README.md

clean:
	rm -r out/

clean_deps:
	rm -r deps/
