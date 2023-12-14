# gemini_line_bot.py
from line_bot_base import LineBot
from linebot.models import TextSendMessage
import google.generativeai as genai
import os

# 環境変数から設定を読み込み
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

# Gemini APIの設定
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

class GeminiLineBot(LineBot):
    def handle_text_message(self, event):
        user_message = event.message.text
        response = model.start_chat().send_message(user_message)
        reply_text = response.text

        self.line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text),
        )

if __name__ == "__main__":
    bot = GeminiLineBot(ACCESS_TOKEN, CHANNEL_SECRET)
    app = bot.create_app()
    app.run(port=5000)
