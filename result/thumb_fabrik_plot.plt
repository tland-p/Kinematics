#Y軸のグリッド線を入れる
set grid

#凡例の位置(center, left, right, outside, top, bottom等)
set key center top

#xyz軸のラベル設定
set xlabel "x[mm]"
set ylabel "y[mm]"
set zlabel "z[mm]"
#図のタイトル、論文やスライドのグラフには原則不要、進捗報告用とかに
# set title "title hogefuga"

#png画像を作る場合
set terminal png
#出力先のファイル指定(相対パス)
set output "./thumb_fabrik_plot.png"

# プロットデータからグラフ生成
# 基本:plot "filename" with 描画スタイル オプション
# withの後に続く描画スタイルの指定(必須)でグラフの種類が決まる
# with lp(linespoints)
# title:凡例名
#plot "./sample1.plot" with lp title "foobar"
set datafile separator ","

set xrange [-50:50]
set yrange [-50:50]
set zrange [0:100]
set view equal xyz

splot "./csv/thumb_calculated_with_FABRIK2.csv" using 1:2:3 title "links" with linespoints ,\
      "./csv/thumb_calculated_with_FABRIK2.csv" every 3::0 using 1:2:3 title "thumb0" with points pointtype 6 ,\
      "./csv/thumb_calculated_with_FABRIK2.csv" every 3::1 using 1:2:3 title "thumb1" with points pointtype 6 ,\
      "./csv/thumb_calculated_with_FABRIK2.csv" every 3::2 using 1:2:3 title "thumb2" with points pointtype 6 ,\
      "./csv/target.csv" using 1:2:3 title "target" with points pointtype 13 ,\

#splot "fk_thumb_joint.csv" using 1:2:3 title "init" with linespoints ,\
#      "fk_thumb_joint.csv" every 3::0 using 1:2:3 title "thumb0" with points pointtype 2 ,\
#      "fk_thumb_joint.csv" every 3::1 using 1:2:3 title "thumb1" with points pointtype 2 ,\
#      "fk_thumb_joint.csv" every 3::2 using 1:2:3 title "thumb2" with points pointtype 2