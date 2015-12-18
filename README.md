# ![Kazesawa Font](https://raw.githubusercontent.com/kazesawa/logo/master/kazesawa_w700.png)

![Sample](https://raw.githubusercontent.com/kazesawa/kazesawa/master/samples/kazesawa-sample-sil.png)

[紹介スライド: Introducing Kazewasa Font](https://speakerdeck.com/polamjag/introducing-kazesawa-font)

## ダウンロード

以下の方法がおすすめです:

- [GitHub の Releases](https://github.com/kazesawa/kazesawa/releases)
- [現在の master ブランチの zip](https://github.com/kazesawa/kazesawa/archive/master.zip)

master ブランチの zip をダウンロードした場合は、フォント本体は `out/` ディレクトリ内にあります。

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
