# 基本イメージとしてPythonの公式イメージを使用
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 必要なPythonライブラリをインストール
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -q -U google-generativeai