# mypkg
* これは、ROS2のパッケージです。<br/>
![test](https://github.com/zerogu-arufa/mypkg/actions/workflows/test.yml/badge.svg)

## 行える処理
このプログラムは最初に希望の計測時間を入力する事でtalker.pyを実行する事でカウントが始まり、<br/>
listener.pyを通じて計測時間終了までの残り時間を見る事が出来ます。
## インストール方法
```
$ git clone git@github.com:zerogu-arufa/mypkg.git
$ cd mypkg
$ chmod +x mypkg
```
# コマンドの使い方
## 2つのターミナルで処理を行う場合
* talker側のコマンド(1つ目のターミナル)
```
$ cd mypkg　　　　　　　　　　　　                        #mypkgというディレクトリに移動
$ ros2 run mypkg talker                                   #talkerノードを実行するコマンド。
   (こちら側では何も表示されない）
```
* listener側のコマンド(2つ目のターミナル)
```
 $ ros2 run mypkg listener                                #listenerノードを実行するコマンド
   [INFO] [1672472619.983395319] [listener]: Listen: 12
   [INFO] [1672472620.474658465] [listener]: Listen: 11   #カウントはtalkerのコマンド実行時点から始まっているので注意してください
```
## 1つのターミナルで処理を行う場合
```
 $ cd launch                                              #launchというディレクトリに移動する。
 $ ros2 launch mypkg talk_listen.launch.py                #talkerとlistenerの2つのノードが同時に立ち上がる。   
　 [INFO] [1672472619.983395319] [listener]: Listen: 20
   [INFO] [1672472620.474658465] [listener]: Listen: 19   #希望の計測時間からカウントが始まる
```
## 計測時間の変更の仕方
```
$ cd mypkg
$ vi talker.py
```
上記入力後、「#ここを希望のカウント数に変更する」と記載されている部分の数(初期は20秒)を変更して下さい
## テスト環境
* Ubuntu2204.2.33.0

## 必要なソフトウェア
* ROSのパージョン：ROS2
* Pythonのバージョン：Python3.10.6

## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます
* © 2023 Tateuchi Naoya
