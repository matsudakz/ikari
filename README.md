1.virtualenvのインストール
sudo pip2 install virtualenv

2.実行環境用ディレクトリ作成
mkdir -p /home/pi/PycharmProjects

3.Gitから取得
cd /home/pi/PycharmProjects
git clone https://github.com/matsudakz/ikari.git

4.virtualenv実行
cd /home/pi/PycharmProjects/ikari
python2 -m virtualenv venv
cd /home/pi/PycharmProjects/ikari/venv
. bin/active

5.各種ライブラリインストール
pip install Django
pip install Django-Sites-Templatetags
pip install anyjson
pip install poster

6.migrate実行
cd /home/pi/PycharmProjects/ikari/webapp3
python manage.py migrate

7.受付IPアドレス設定
cd /home/pi/PycharmProjects/ikari/webapi3/webapi3
viで以下を修正
vi settings.py
28 ALLOWED_HOSTS = ['受け付けるIPアドレスを入れる']

8.Webサーバー起動
cd /home/pi/PycharmProjects/ikari/webapi3
python manage.py runserver ラズパイのIPアドレス:8000

9.ブラウザで実行
ブラウザのURLに
http://ラズパイのIPアドレス:8000
そうすると、アップロードファイル選択のウィンドウが立ち上がるので、
アップロードファイルを選んで、アップロードボタンを押してください。

10.結果の確認
10秒未満で結果がWebサーバーを起動したターミナルに出るはずです。

__EOF__
