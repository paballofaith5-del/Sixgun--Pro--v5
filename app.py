from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>Sixgun Pro v5</title>
<style>
body { background:#0a0a0a; color:#00ff88; font-family:monospace; text-align:center; padding:50px; }
h1 { font-size:40px; }
button { padding:15px 30px; background:#00ff88; border:none; font-size:20px; cursor:pointer; border-radius:10px; }
.status { margin-top:20px; font-size:18px; }
</style>
</head>
<body>
<h1>🔫 SIXGUN PRO v5 🔥</h1>
<h2>Deployed Successfully on Render!</h2>
<div class="status">Status: ONLINE ✅</div>
<br><br>
<button onclick="alert('Sixgun Pro is LIVE!')">Test Bot</button>
<br><br>
<p>Your trading bot is now live 24/7</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return jsonify({"status": "ok", "bot": "Sixgun Pro v5", "live": True})

@app
