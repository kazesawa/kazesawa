#!/usr/bin/env fontforge -lang=py -script
# -*- coding: utf-8 -*-

# Kazesawa Font Generator
#
# Original one of this script is derived from Koruri project
# https://gist.github.com/lindwurm/b24657c335bb11a520c4
# https://gist.github.com/mandel59/530c20924768ce180923

import fontforge
from datetime import datetime
import sys

args = sys.argv

if len(args) != 3:
    print("Usage: generate_ttf.py <path to directory of Source Sans Pro> <path to directory of M+>")
    quit()

sourcesans_path = args[1]
mplus_path = args[2]

# Kazesawa を生成するディレクトリのパス
# 同じディレクトリに一時ファイルも生成される
kazesawa_path = "./out"

# .sfd を出力するディレクトリのパス
sfd_path ="./out"

# フォントリスト
# Source Sans Pro ファイル名, M+ ファイル名, Kazesawa ウェイト
font_list = [
    ("SourceSansPro-ExtraLight.otf", "mplus-1p-thin.ttf", "ExtraLight"),
    ("SourceSansPro-Light.otf", "mplus-1p-light.ttf", "Light"),
    ("SourceSansPro-Regular.otf", "mplus-1p-regular.ttf", "Regular"),
    ("SourceSansPro-Semibold.otf", "mplus-1p-medium.ttf", "Semibold"),
    ("SourceSansPro-Bold.otf", "mplus-1p-bold.ttf", "Bold"),
    ("SourceSansPro-Black.otf", "mplus-1p-heavy.ttf", "Extrabold"),
]

def main():
    # 縦書き対応
    fontforge.setPrefs('CoverageFormatsAllowed', 1)

    # バージョンを時刻から生成する
    version = "Kazesawa-{0}".format(datetime.utcnow().strftime("%Y%m%d%H%M%S"))

    for (op, mp, weight) in font_list:
        op_path = "{0}/{1}".format(sourcesans_path, op)
        mp_path = "{0}/{1}".format(mplus_path, mp)
        ko_path = "{0}/Kazesawa-{1}.ttf".format(kazesawa_path, weight)
        sf_path = "{0}/Kazesawa-{1}".format(sfd_path, weight)
        generate_kazesawa(op_path, mp_path, ko_path, sf_path, weight, version)

def kazesawa_sfnt_names(weight, version):
    return (
        ('English (US)', 'Copyright',
         '''\
Kazesawa: Copylight (c) 2015 polamjag.

This font is generated by merging these fonts:
Source Sans Pro: Copyright (c) 2012 Adobe Systems Incorporated.
M+ OUTLINE FONTS: Copyright (C) 2015 M+ FONTS PROJECT.'''),
        ('English (US)', 'Family', 'Kazesawa {0}'.format(weight)),
        ('English (US)', 'SubFamily', weight),
        ('English (US)', 'Fullname', 'Kazesawa-{0}'.format(weight)),
        ('English (US)', 'Version', version),
        ('English (US)', 'PostScriptName', 'Kazesawa-{0}'.format(weight)),
        ('English (US)', 'Vendor URL', 'https://github.com/kazesawa/'),
        ('English (US)', 'Preferred Family', 'Kazesawa'),
        ('English (US)', 'Preferred Styles', weight),
        ('Japanese', 'Preferred Family', 'Kazesawa'),
        ('Japanese', 'Preferred Styles', weight),
    )

def kazesawa_gasp():
    return (
        (8, ('antialias',)),
        (13, ('antialias', 'symmetric-smoothing')),
        (65535, ('gridfit', 'antialias', 'symmetric-smoothing', 'gridfit+smoothing')),
    )

# this function is from Migu font
# see https://osdn.jp/cvs/view/mix-mplus-ipa/mixfont-mplus-ipa/mplus_outline_fonts/mig.d/scripts/build-ttf.py?view=log
def set_japanese_proportional(f):
    scale = 1

    # small kana, dakuten, onbiki
    #   ぁぃぅぇ ぉっゃゅ
    #   ょゎゕゖ ゛゜ァィ
    #   ゥェォャ ュョヮヵ
    #   ヶー(ッ 0x30c3)
    japanese_chars_small = (
        0x3041,0x3043,0x3045,0x3047, 0x3049,0x3063,0x3083,0x3085,
        0x3087,0x308e,0x3095,0x3096, 0x309b,0x309c,0x30a1,0x30a3,
        0x30a5,0x30a7,0x30a9,0x30e3, 0x30e5,0x30e7,0x30ee,0x30f5,
        0x30f6,0x30fc
    )

    # wall left (Left edges of these glyphs are drawn as lines like walls.)
    # けげしじ はばぱ
    # ほぼぽゆ り
    # トドヒビ ピレロ
    # (ハバパ)
    japanese_chars_wall_L = (
        0x3051,0x3052,0x3057,0x3058, 0x306f,0x3070,0x3071,
        0x307b,0x307c,0x307d,0x3086, 0x308a,
        0x30c8,0x30c9,0x30d2,0x30d3, 0x30d4,0x30ec,0x30ed
    )
    # ぬねの りわ
    # カガコゴ ヨリロ
    japanese_chars_wall_R = (
        0x306c,0x306d,0x306e, 0x308a,0x308f,
        0x30ab,0x30ac,0x30b3,0x30b4, 0x30e8,0x30ea,0x30ed
    )
    # needle left (Left edges of these glyphs are drawn as points like needles)
    # くへべぺ やん
    # イノヘベ ペ
    japanese_chars_needle_L = (
        0x304f,0x3078,0x3079,0x307a, 0x3084, 0x3093,
        0x30a4,0x30ce,0x30d8,0x30d9, 0x30da
    )
    # しへ
    # ピプへ
    japanese_chars_needle_R = (
        0x3057,0x3078,
        0x30d4,0x30d7,0x30d8
    )

    # parenthesis fullwitdh
    # 〈《「『  【〔（［ ｛
    #brackets_start = (0x3008,0x300a,0x300c,0x300e, 0x3010,0x3014,0xff08,0xff3b, 0xff5b)
    #brackets_end = [0x3009,0x300b,0x300d,0x300f, 0x3011,0x3015,0xff09,0xff3d, 0xff5d]
    # 「『【
    brackets_start = (0x300c,0x300e,0x3010)
    brackets_end = (0x300d,0x300f,0x3011)

    # hiragana, katakana
    for kana in range(0x3041, 0x30ff+1):
        # blank, blank, combining゛. combining゜, ・
        if kana == 0x3097 or kana == 0x3098 or kana == 0x3099 or kana == 0x309a or kana == 0x30fb:
            continue

        maxL = 75
        maxR = 75
        for c in japanese_chars_small:
            if kana == c:
                maxL = 50
                maxR = 50
                break
        for c in japanese_chars_wall_L:
            if kana == c:
                maxL = 125
                break
        for c in japanese_chars_wall_R:
            if kana == c:
                maxR = 125
                break
        for c in japanese_chars_needle_L:
            if kana == c:
                maxL = 50
                break
        for c in japanese_chars_needle_R:
            if kana == c:
                maxR = 50
                break
        maxL = int(maxL * scale)
        maxR = int(maxR * scale)

        bearing_L = f[kana].left_side_bearing
        bearing_R = f[kana].right_side_bearing
        if bearing_L > maxL:
            f[kana].left_side_bearing = maxL
        if bearing_R > maxR:
            f[kana].right_side_bearing = maxR
        else:
            f[kana].right_side_bearing = bearing_R
    # ン
    f[0x30f3].right_side_bearing = int(65 * scale)
    # nakaguro ・
    f[0x30fb].left_side_bearing = 250
    f[0x30fb].right_side_bearing = 250

    # brackets
    max = 250
    min = 50
    for c in brackets_start:
        bearing_L = f[c].left_side_bearing
        bearing_R = f[c].right_side_bearing
        if bearing_L > max:
            f[c].left_side_bearing = max
        if bearing_R > min:
            f[c].right_side_bearing = min
        else:
            f[c].right_side_bearing = bearing_R
    for c in brackets_end:
        bearing_R = f[c].right_side_bearing
        if bearing_R > max:
            f[c].right_side_bearing = max


def generate_kazesawa(op_path, mp_path, ko_path, sf_path, weight, version):
    # M+ を開く
    font = fontforge.open(mp_path)

    #font.em = 2048
    font.em = 900

    # Source Sans Pro を開く
    opfont = fontforge.open(op_path)

    # Source Sans Pro に含まれるグリフを削除する
    font.selection.none()
    opfont.selection.all()
    for glyph in opfont.selection.byGlyphs:
        if glyph.glyphname in font:
            font.selection.select(("more",), glyph.glyphname)
    font.clear()

    # Source Sans Pro をマージする
    font.mergeFonts(op_path)

    # フォント情報の設定
    font.sfnt_names = kazesawa_sfnt_names(weight, version)
    font.os2_vendor = "kaze"

    set_japanese_proportional(font)

    # Grid Fittingの設定
    font.gasp = kazesawa_gasp()

    font.em = 2048

    # .sfd を出力
    source = sf_path + ".sfd"
    font.save(source)

    # TTF の生成
    font.generate(ko_path, '', ('short-post', 'opentype', 'PfEd-lookups'))

if __name__ == '__main__':
    main()
