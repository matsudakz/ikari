1.virtualenvのインストール
sudo pip2 install virtualenv

2.実行環境用ディレクトリ作成
mkdir -p /home/pi/PycharmProjects/ikari

3.virtualenv実行
cd /home/pi/PycharmProjects/ikari
python2 -m virtualenv venv
cd /home/pi/PycharmProjects/ikari/venv
. bin/active

4.Gitから取得
cd /home/pi/PycharmProjects/ikari
ここでGitから取得

5.Webサーバー起動
cd /home/pi/PycharmProjects/ikari/webapi3
python manage.py runserver ラズパイのIPアドレス:8000
                           ^^^^^^^^^^^^^^^^^^
                           ここは自分のラズパイのIPアドレスに変えてください

6.ブラウザで実行
ブラウザのURLに
http://ラズパイのIPアドレス:8000
       ^^^^^^^^^^^^^^^^^^
       ここは自分のラズパイのIPアドレスに変えてください
そうすると、アップロードファイル選択のウィンドウが立ち上がるので、
アップロードファイルを選んで、アップロードボタンを押してください。

7.結果の確認
10秒未満で結果がWebサーバーを起動したターミナルに出るはずです。

__EOF__
