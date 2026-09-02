from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Sixgun Pro v5 LIVE!</h1><p>Bot is Online</p>"

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
