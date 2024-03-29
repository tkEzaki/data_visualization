# 『指標・特徴量の設計から始める データ可視化学入門 データを洞察につなげる技術』 サンプルコード

## 本リポジトリについて
- 本リポジトリは、江崎貴裕著『指標・特徴量の設計から始める データ可視化学入門 データを洞察につなげる技術』（ソシム）のサンプルコードを公開するためのリポジトリです。動作確認はPython 3.10.11で実施しています。

- 各章の図版を作成するためのコードが各フォルダに入っています。各pythonファイルは独立して動くようになっているので、個別に取り出して実行できます。プロットするために必要なデータは各フォルダの中のdataフォルダの中に格納してあります。なお、著者が権利を有しないデータの再配布を避けるため、振る舞いの似たダミーデータに差し替えてあります。可視化のサンプルとしてのみ利用するようお願いいたします。

- 付録に用いたコードも一緒に格納してありますが、これにはコードの説明のためのサンプルも含まれているため、必ずしも実行できるわけではないことに注意してください。

- 本書の中で用いられている図版は、本リポジトリのコードを用いて作成したのち、デザイナーさんがデザインを整えているので、厳密に同じ図にはならないことに注意してください。また、その目的のため、（後で追加される想定だった）**一部グラフのタイトルやラベルが抜けている場合があります**。

## ご利用に際して
- 本サンプルコードはご自由にご利用いただいて構いませんが、ご自身の責任の範囲でご利用いただき、それにより万一発生した損害等につきましては著者は一切責任を負いません。
- 本サンプルコードは予告なく内容を変更する（主に修正や改善を実施予定です）場合がありますのでご了承下さい。
- 本サンプルコードに関しての質問や改善のアイディアについては随時ご連絡ください（ただし必ずしも対応をお約束するものではございません）。


## 他言語による実装

非常にありがたいことに、本プログラムのMATLABやRによる実装例を公開して下さっている方がいらっしゃいますのでリンクを張らせていただきます。普段これらの言語を使われる方は是非参考にしてみて下さい。

### MATLABによる実装
- Michio Inoue様 https://github.com/minoue-xx/MATLAB-example-for-An-Introduction-to-Data-Visualization

### Rによる実装
- Osamu Morimoto様 https://morimotoosamu.github.io/data_visualization/

## FAQ
### コードが動かない（初学者向け）
#### Pythonプログラミングは始めてなのだが何から始めたらよいか
お使いの環境ごとにPythonをインストールする方法については[Python Japanの環境構築ガイド](https://www.python.jp/install/install.html)をご参照いただいたり、Youtube上にも優れた動画がいくつも上がっているのでこれらを参考にやってみることをおすすめします。

- [【Pythonプログラミング入門】Windows PCにPythonをインストールして動かす！〜VTuberと学習するプログラミング〜](https://www.youtube.com/watch?v=XhbRqItkIYI&list=PLiaZfx-34L5oK_8hLi_jbmFfZgZoGCqnr&index=3)
- [【Pythonプログラミング入門】MacにPythonをインストールして動かす！〜VTuberと学習するプログラミング〜](https://www.youtube.com/watch?v=Gu0K4ammlHg&list=PLiaZfx-34L5oK_8hLi_jbmFfZgZoGCqnr&index=5)



#### moduleがないと言われる
必要なパッケージがインストールされていない場合、手動で追加インストールする必要があります。必要なパッケージはrequirements.txtにまとめてありますので、これを用いて一括でインストールすると便利です。いくつかわかりやすい解説動画へのリンクを張っておきます。
- [【Pythonプログラミング入門】モジュール・パッケージを解説！〜VTuberと学習〜 初心者でも必ずわかる!!](https://youtu.be/aXnB3Cm__-o?si=cJFXpkPWGp-YLiGP)
- [【Pythonプログラミング入門】ライブラリ一括インストール！ requirements.txt 〜VTuberと学習〜 【初心者向け】](https://youtu.be/iiFs3u6VkFE?si=QEf3D9a7MGx6lBR-)


#### importはできているのに関数が動かない
インストールされているパッケージのバージョンが異なっている可能性が高いです。バージョンを合わせるか、適宜お使いのバージョンに合わせた記述に変更してください。（そのような際にはChatGPTなどが便利です。）バージョン情報についてはrequirements.txtに示してあります。

#### データの読み込みができない
本サンプルコードはそれぞれの章のフォルダで独立しています。開発環境で開いているディレクトリがPythonファイルと同じかどうか確認してください。

### 利用について
#### 本サンプルコードをRやMATLABで書き直したものを公開しても良いか
大歓迎です。ご連絡いただければこちらからリンクを張らせていただきます。

#### サンプルコードを再配布したい／授業で利用したい
問題ありません。授業で利用する場合は、学生の方からの質問などは一旦教員の方が対応するようお願いします。

### コードの内容について
#### オススメの利用法について知りたい
最初からすべてを実行しながら本書を読み進めていただくのも良いですし、必要になったタイミングで「あの本のあの図みたいな可視化がしたいな」と思った際にそこだけ利用していただくのも良いかと思います。

#### 全ての可視化コードを理解できるようにするべきなのか
本書のサンプルコードは本書中で説明に使った図を再現するもので、必ずしも可視化のプログラミング教育のために作られたものではありません。したがって、ごく一部ですが少し込み入ったことをしていたり、ややマニアックな技術を利用している場合があります。そういうものはスキップしていただいてもいいと思います。

#### コメントが沢山ついているがこれくらい書いた方がいいのか
本サンプルコードでは、初学者の方が読んでも何をしているかわかりやすいように細かすぎるくらいにコメントを書いていますが、もちろん普段からここまで細かく記載する必要はありません。


# 修正履歴
- 2024/1/5 図1.2.4のクラスターマップのx軸ラベル、y軸ラベルがクラスタリング前のものになっていた点を修正
https://github.com/tkEzaki/data_visualization/pull/1/commits/38ac7c4ef9e5e34449149da8044b10cd9fe67012

- 2024/1/15 他言語での実装例へのリンクの追加