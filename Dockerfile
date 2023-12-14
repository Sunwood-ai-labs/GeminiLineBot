# 基本イメージとしてPythonの公式イメージを使用
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /app

# 必要なPythonライブラリをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコンテナにコピー
COPY . .

# アプリケーションを起動
CMD ["python", "./line_bot.py"]
