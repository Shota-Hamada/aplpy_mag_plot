# aplpy_mag_plot

フォルダの内容
.
├── README.md　
├── figure
│   └── sgr_A_ziba.pdf
├── fits_file
│   └── iextGalCM2812YYNN.fit
├── magnetic_field
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── ziba.csv
│   ├── ziba.numbers
│   ├── ziba.py
│   ├── ziba.pyc
│   └── ziba.txt
├── main.py
└── tempCodeRunnerFile.py

## 必要なモジュール(ライブラリ)
*本来であればpython3を使うべきですが、aplpyのライブラリが3系の場合だとうまく動かないので、
ここでは敢えてpython2系を使います
$ pip2 install numpy
$ pip2 install aplpy
$ pip2 install pandas
$ pip2 install astropy


## 使い方
*本来であればpython3を使うべきですが、aplpyのライブラリが3系の場合だとうまく動かないので、
ここでは敢えてpython2系を使います。
$ python2 main.py

aplpyは基本的にdegree表記で認識されます。なので、hms,dms表記で扱っている場合は、変換が必要になります。
ds9等のツールも使うのいいですし、以下のスクリプトでも変換することができます。

$ python2 check_hmsdms_to_deg.py

or 

$ python3 check_hmsdms_to_deg.py

## 設定と変更
main.py
