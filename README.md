# ![Kazesawa Font](https://raw.githubusercontent.com/kazesawa/logo/master/kazesawa_w700.png)

![Sample](https://raw.githubusercontent.com/kazesawa/kazesawa/master/samples/kazesawa-sample-sil.png)

[紹介スライド: Introducing Kazewasa Font](https://speakerdeck.com/polamjag/introducing-kazesawa-font)

## ダウンロード

以下の方法がおすすめです:

- [GitHub の Releases](https://github.com/kazesawa/kazesawa/releases)
- [現在の master ブランチの zip](https://github.com/kazesawa/kazesawa/archive/master.zip)

master ブランチの zip をダウンロードした場合は、フォント本体は `out/` ディレクトリ内にあります。

OS X ユーザの場合は、以下の様なワンライナーを端末で実行することで最新のものを `$HOME/Library/Fonts` にインストールできます:

```sh
pushd $(pwd) && cd $TMPDIR && curl -LO $(curl -i 'https://github.com/kazesawa/kazesawa/releases/latest/' | tr -d $'\r' | grep Location | head -n1 | awk '{print $2}' | sed -e 's|/releases/tag/|/releases/download/|' -e 's|$|/kazesawa.zip|') && unzip kazesawa.zip '*.ttf' -d $HOME/Library/Fonts/ && rm kazesawa.zip && popd
```

Linux などでも同様のことが可能です:
```sh
mkdir $HOME/.fonts $$ pushd $(pwd) && cd $TMPDIR && curl -LO $(curl -i 'https://github.com/kazesawa/kazesawa/releases/latest/' | tr -d $'\r' | grep Location | head -n1 | awk '{print $2}' | sed -e 's|/releases/tag/|/releases/download/|' -e 's|$|/kazesawa.zip|') && unzip kazesawa.zip '*.ttf' -d $HOME/.fonts/ && rm kazesawa.zip && fc-cache -fv && popd
```

## ビルド方法

```
$ git clone https://github.com/kazesawa/kazesawa && cd kazesawa
$ make fetch_deps
$ make ttf # built fonts are in out/
$ make zip # optional: creates .zip for distribution
```

or

```
$ git clone https://github.com/kazesawa/kazesawa && cd kazesawa
$ make fresh
```
