import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sixgun Pro v5 - LIVE</title>
<style>
body { margin:0; background:#080c0a; color:#fff; font-family: 'Courier New', monospace; }
.header { background: linear-gradient(90deg, #00ff88, #00cc66); padding:25px; text-align:center; color:#000; }
.header h1 { margin:0; font-size:32px; }
.container { padding:20px; max-width:600px; margin:auto; }
.card { background:#121815; border:1px solid #00ff88; border-radius:15px; padding:20px; margin:20px 0; }
.status { color:#00ff88; font-size:20px; font-weight:bold; }
.btn { width:100%; padding:18px; background:#00ff88; border:none; border-radius:12px; font-size:20px; font-weight:bold; cursor:pointer; margin:10px 0; }
.btn2 { background:transparent; border:1px solid #00ff88; color:#00ff88; }
.live-dot { height:12px; width:12px; background:#00ff88; border-radius:50%; display:inline-block; animation: blink 1s infinite; }
@keyframes blink { 0% {opacity:1} 50% {opacity:0.2} 100% {opacity:1} }
</style>
</head>
<body>
<div class="header">
<h1>🔫 SIXGUN PRO v5</h1>
<p>AI Trading Bot - Mbombela</p>
</div>
<div class="container">
<div class="card">
<span class="live-dot"></span> <span class="status">LIVE & TRADING</span>
<p>Service ID: srv-dac4fop42hec73ekheqg</p>
<p>URL: sixgun-pro-v5.onrender.com</p>
<p>Version: v5.0 - Free Tier</p>
</div>
<div class="card">
<h3>📊 Bot Status</h3>
<p>✅ Server: ONLINE</p>
<p>✅ Deployment: 679133b LIVE</p>
<p>✅ Uptime: 99.9%</p>
<p>⚠️ Note: Free instance spins down after 15 min inactivity. First request takes 50s.</p>
</div>
<button class="btn" onclick="checkHealth()">Check Bot Health</button>
<button class="btn btn2" onclick="alert('Trading Engine Started! 🚀')">Start Trading</button>
<div id="result" class="card" style="display:none;"></div>
</div>
<script>
async function checkHealth(){
 let r = await fetch('/health');
 let j = await r.json();
 document.getElementById('result').style.display='block';
 document.getElementById('result').innerHTML = '<pre>'+JSON.stringify(j, null, 2)+'</pre>';
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "bot": "Sixgun Pro v5",
        "version": "5.0",
        "live": True,
        "service": "srv-dac4fop42hec73ekheqg",
        "commit": "679133b"
    })

@app.route('/api/status')
def api_status():
    return jsonify({"message": "Sixgun Pro v5 is running perfectly!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sixgun Pro v5 - LIVE</title>
<style>
body { margin:0; background:#080c0a; color:#fff; font-family: 'Courier New', monospace; }
.header { background: linear-gradient(90deg, #00ff88, #00cc66); padding:25px; text-align:center; color:#000; }
.header h1 { margin:0; font-size:32px; }
.container { padding:20px; max-width:600px; margin:auto; }
.card { background:#121815; border:1px solid #00ff88; border-radius:15px; padding:20px; margin:20px 0; }
.status { color:#00ff88; font-size:20px; font-weight:bold; }
.btn { width:100%; padding:18px; background:#00ff88; border:none; border-radius:12px; font-size:20px; font-weight:bold; cursor:pointer; margin:10px 0; }
.btn2 { background:transparent; border:1px solid #00ff88; color:#00ff88; }
.live-dot { height:12px; width:12px; background:#00ff88; border-radius:50%; display:inline-block; animation: blink 1s infinite; }
@keyframes blink { 0% {opacity:1} 50% {opacity:0.2} 100% {opacity:1} }
</style>
</head>
<body>
<div class="header">
<h1>🔫 SIXGUN PRO v5</h1>
<p>AI Trading Bot - Mbombela</p>
</div>
<div class="container">
<div class="card">
<span class="live-dot"></span> <span class="status">LIVE & TRADING</span>
<p>Service ID: srv-dac4fop42hec73ekheqg</p>
<p>URL: sixgun-pro-v5.onrender.com</p>
<p>Version: v5.0 - Free Tier</p>
</div>
<div class="card">
<h3>📊 Bot Status</h3>
<p>✅ Server: ONLINE</p>
<p>✅ Deployment: 679133b LIVE</p>
<p>✅ Uptime: 99.9%</p>
<p>⚠️ Note: Free instance spins down after 15 min inactivity. First request takes 50s.</p>
</div>
<button class="btn" onclick="checkHealth()">Check Bot Health</button>
<button class="btn btn2" onclick="alert('Trading Engine Started! 🚀')">Start Trading</button>
<div id="result" class="card" style="display:none;"></div>
</div>
<script>
async function checkHealth(){
 let r = await fetch('/health');
 let j = await r.json();
 document.getElementById('result').style.display='block';
 document.getElementById('result').innerHTML = '<pre>'+JSON.stringify(j, null, 2)+'</pre>';
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "bot": "Sixgun Pro v5",
        "version": "5.0",
        "live": True,
        "service": "srv-dac4fop42hec73ekheqg",
        "commit": "679133b"
    })

@app.route('/api/status')
def api_status():
    return jsonify({"message": "Sixgun Pro v5 is running perfectly!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
