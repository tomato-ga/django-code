# python3のイメージを指定
FROM python:3.11.4-bullseye
# バッファリングを無効化
ENV PYTHONUNBUFFERED 1
# 直下にcodeディレクトリを作成
RUN mkdir /code
# codeディレクトリに移動
WORKDIR /code
# codeディレクトリにrequirements.txtのコピーを配置
COPY requirements.txt /code/
# pipをupgradeしてrequirements.txtに記載したパッケージをインストールする
RUN pip install --upgrade pip && pip install -r requirements.txt
# docker-django-mysql8下のファイルをcodeディレクトリにコピー
COPY . /code/

