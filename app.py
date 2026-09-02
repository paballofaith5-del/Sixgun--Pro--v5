from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Six Gun Pro V5 - Maphotla</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', -apple-system, sans-serif; }
body { background:#0a0e13; display:flex; justify-content:center; min-height:100vh; }
.phone-frame { width:100%; max-width:390px; background:#7cc8f7; min-height:100vh; position:relative; padding:12px; }
.inner-screen { background: linear-gradient(180deg, #6ec6ff 0%, #a3ddff 30%, #d6efff 100%); min-height:calc(100vh - 24px); border-radius:28px; position:relative; overflow:hidden; padding-bottom:90px; box-shadow:inset 0 0 0 2px rgba(255,255,255,0.5); }
.status-icons { display:flex; justify-content:space-between; padding:14px 22px 5px; font-size:12px; font-weight:700; color:#0a3d62; }
.profile-card { margin:18px 18px 0; background: rgba(78,190,255,0.55); backdrop-filter: blur(15px); border-radius:26px; padding:22px 15px 18px; text-align:center; position:relative; border:1.5px solid rgba(255,255,255,0.4); }
.bot-avatar { width:110px; height:110px; border-radius:50%; margin:0 auto 12px; border:4px solid white; box-shadow:0 8px 25px rgba(0,0,0,0.25); overflow:hidden; background:white; }
.bot-avatar img { width:100%; height:100%; object-fit:cover; }
.online-dot { width:12px; height:12px; background:#00ff88; border:2px solid white; border-radius:50%; position:absolute; top:18px; right:18px; box-shadow:0 0 10px #00ff88; }
.app-name { color:white; font-weight:800; font-size:13px; letter-spacing:0.8px; text-shadow:0 1px 3px rgba(0,0,0,0.2); line-height:1.3; }
.app-name span { display:block; font-size:12px; opacity:0.9; }
.action-row { display:flex; justify-content:space-around; margin-top:16px; }
.action { text-align:center; }
.action i { width:38px; height:38px; background:rgba(255,255,255,0.35); border-radius:10px; line-height:38px; color:white; font-size:16px; display:block; margin:0 auto 4px; border:1px solid rgba(255,255,255,0.4); }
.action span { font-size:9px; color:white; font-weight:600; letter-spacing:0.5px; opacity:0.9; }
.add-btn { margin:18px 18px 0; background: linear-gradient(90deg, #33b9ff, #4cc3ff); border-radius:16px; padding:16px; display:flex; align-items:center; justify-content:center; color:white; font-weight:800; font-size:13px; letter-spacing:0.8px; box-shadow:0 6px 18px rgba(51,185,255,0.4); border:1.5px solid rgba(255,255,255,0.5); cursor:pointer; width:calc(100% - 36px); }
.add-btn i { margin-right:8px; }
.info-cards { margin:16px 18px 0; display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.mini-card { background:white; border-radius:14px; padding:12px; box-shadow:0 4px 15px rgba(0,0,0,0.06); }
.mini-card h5 { font-size:8px; color:#90a4ae; letter-spacing:0.5px; margin-bottom:3px; }
.mini-card p { font-size:13px; font-weight:800; color:#0a3d62; }
.bottom-nav { position:absolute; bottom:12px; left:18px; right:18px; background:rgba(255,255,255,0.92); backdrop-filter:blur(20px); border-radius:20px; display:flex; justify-content:space-around; padding:12px 0 8px; box-shadow:0 -4px 20px rgba(0,0,0,0.08); }
.nav-icon { text-align:center; color:#b0c4de; font-size:18px; }
.nav-icon.active { color:#29b6f6; }
.nav-icon.active i { background:rgba(41,182,246,0.15); width:36px; height:36px; line-height:36px; border-radius:10px; }
.signal-box { margin:16px 18px 0; background:white; border-radius:16px; padding:14px; box-shadow:0 4px 15px rgba(0,0,0,0.06); }
.live { background:#00e676; color:white; font-size:8px; font-weight:800; padding:3px 8px; border-radius:20px; display:inline-block; margin-bottom:6px; }
</style>
</head>
<body>
<div class="phone-frame">
<div class="inner-screen">
<div class="status-icons"><span>9:41</span><span>📶 📶 🔋</span></div>

<div class="profile-card">
<div class="online-dot"></div>
<div class="bot-avatar">
<img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" alt="Robot">
</div>
<div class="app-name">SIX GUN PRO<br><span>V5.0 • MAPHOTLA</span></div>
<div class="action-row">
<div class="action"><i class="far fa-chart-bar"></i><span>ANALYZE</span></div>
<div class="action"><i class="fas fa-crosshairs"></i><span>6 GUNS</span></div>
<div class="action"><i class="far fa-trash-alt"></i><span>REMOVE</span></div>
</div>
</div>

<button class="add-btn" onclick="addRobot()"><i class="fas fa-plus"></i> ADD ROBOT - HOST ROBOT V5</button>

<div class="signal-box">
<div class="live">● LIVE</div>
<div style="font-weight:800; font-size:12px; color:#0a3d62;">XAUUSD GOLD • Maphotla Sniper</div>
<div id="price" style="font-size:22px; font-weight:900; color:#03a9f4; margin:6px 0;">$2,684.52</div>
<div id="sig" style="background:#e8f5e9; color:#2e7d32; padding:6px 10px; border-radius:8px; font-weight:800; font-size:10px; display:inline-block;">🟢 BUY • 6/6 GUNS CONFIRMED</div>
</div>

<div class="info-cards">
<div class="mini-card"><h5>WIN RATE</h5><p>94.7% 🎯</p></div>
<div class="mini-card"><h5>PROFIT</h5><p style="color:#00c853;">+$342</p></div>
<div class="mini-card"><h5>ACTIVE</h5><p>3 Bots 🔫</p></div>
<div class="mini-card"><h5>LOCATION</h5><p>Maphotla 🇿🇦</p></div>
</div>

<div class="bottom-nav">
<div class="nav-icon active"><i class="fas fa-home"></i></div>
<div class="nav-icon"><i class="fas fa-chart-line"></i></div>
<div class="nav-icon"><i class="fas fa-robot"></i></div>
</div>
</div>
</div>
<script>
function addRobot(){
 alert('🔫 SIX GUN PRO V5 • MAPHOTLA\\n\\n✅ Robot Hosted Successfully\\n✅ 6 Guns Activated\\n✅ Location: Maphotla, SA\\n\\nSniper starting...');
 document.getElementById('sig').innerText = '⏳ SNIPING...';
 setTimeout(()=>{document.getElementById('sig').innerText='🎯 EXECUTED +$18.50'; document.getElementById('sig').style.background='#e3f2fd';},2500);
}
setInterval(()=>{let p=(2684+Math.random()*5).toFixed(2); document.getElementById('price').innerText='$'+p;},2000);
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {"status":"live","brand":"Six Gun Pro V5 Maphotla"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Six Gun Pro V5 - Maphotla</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', -apple-system, sans-serif; }
body { background:#0a0e13; display:flex; justify-content:center; min-height:100vh; }
.phone-frame { width:100%; max-width:390px; background:#7cc8f7; min-height:100vh; position:relative; padding:12px; }
.inner-screen { background: linear-gradient(180deg, #6ec6ff 0%, #a3ddff 30%, #d6efff 100%); min-height:calc(100vh - 24px); border-radius:28px; position:relative; overflow:hidden; padding-bottom:90px; box-shadow:inset 0 0 0 2px rgba(255,255,255,0.5); }
.status-icons { display:flex; justify-content:space-between; padding:14px 22px 5px; font-size:12px; font-weight:700; color:#0a3d62; }
.profile-card { margin:18px 18px 0; background: rgba(78,190,255,0.55); backdrop-filter: blur(15px); border-radius:26px; padding:22px 15px 18px; text-align:center; position:relative; border:1.5px solid rgba(255,255,255,0.4); }
.bot-avatar { width:110px; height:110px; border-radius:50%; margin:0 auto 12px; border:4px solid white; box-shadow:0 8px 25px rgba(0,0,0,0.25); overflow:hidden; background:white; }
.bot-avatar img { width:100%; height:100%; object-fit:cover; }
.online-dot { width:12px; height:12px; background:#00ff88; border:2px solid white; border-radius:50%; position:absolute; top:18px; right:18px; box-shadow:0 0 10px #00ff88; }
.app-name { color:white; font-weight:800; font-size:13px; letter-spacing:0.8px; text-shadow:0 1px 3px rgba(0,0,0,0.2); line-height:1.3; }
.app-name span { display:block; font-size:12px; opacity:0.9; }
.action-row { display:flex; justify-content:space-around; margin-top:16px; }
.action { text-align:center; }
.action i { width:38px; height:38px; background:rgba(255,255,255,0.35); border-radius:10px; line-height:38px; color:white; font-size:16px; display:block; margin:0 auto 4px; border:1px solid rgba(255,255,255,0.4); }
.action span { font-size:9px; color:white; font-weight:600; letter-spacing:0.5px; opacity:0.9; }
.add-btn { margin:18px 18px 0; background: linear-gradient(90deg, #33b9ff, #4cc3ff); border-radius:16px; padding:16px; display:flex; align-items:center; justify-content:center; color:white; font-weight:800; font-size:13px; letter-spacing:0.8px; box-shadow:0 6px 18px rgba(51,185,255,0.4); border:1.5px solid rgba(255,255,255,0.5); cursor:pointer; width:calc(100% - 36px); }
.add-btn i { margin-right:8px; }
.info-cards { margin:16px 18px 0; display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.mini-card { background:white; border-radius:14px; padding:12px; box-shadow:0 4px 15px rgba(0,0,0,0.06); }
.mini-card h5 { font-size:8px; color:#90a4ae; letter-spacing:0.5px; margin-bottom:3px; }
.mini-card p { font-size:13px; font-weight:800; color:#0a3d62; }
.bottom-nav { position:absolute; bottom:12px; left:18px; right:18px; background:rgba(255,255,255,0.92); backdrop-filter:blur(20px); border-radius:20px; display:flex; justify-content:space-around; padding:12px 0 8px; box-shadow:0 -4px 20px rgba(0,0,0,0.08); }
.nav-icon { text-align:center; color:#b0c4de; font-size:18px; }
.nav-icon.active { color:#29b6f6; }
.nav-icon.active i { background:rgba(41,182,246,0.15); width:36px; height:36px; line-height:36px; border-radius:10px; }
.signal-box { margin:16px 18px 0; background:white; border-radius:16px; padding:14px; box-shadow:0 4px 15px rgba(0,0,0,0.06); }
.live { background:#00e676; color:white; font-size:8px; font-weight:800; padding:3px 8px; border-radius:20px; display:inline-block; margin-bottom:6px; }
</style>
</head>
<body>
<div class="phone-frame">
<div class="inner-screen">
<div class="status-icons"><span>9:41</span><span>📶 📶 🔋</span></div>

<div class="profile-card">
<div class="online-dot"></div>
<div class="bot-avatar">
<img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" alt="Robot">
</div>
<div class="app-name">SIX GUN PRO<br><span>V5.0 • MAPHOTLA</span></div>
<div class="action-row">
<div class="action"><i class="far fa-chart-bar"></i><span>ANALYZE</span></div>
<div class="action"><i class="fas fa-crosshairs"></i><span>6 GUNS</span></div>
<div class="action"><i class="far fa-trash-alt"></i><span>REMOVE</span></div>
</div>
</div>

<button class="add-btn" onclick="addRobot()"><i class="fas fa-plus"></i> ADD ROBOT - HOST ROBOT V5</button>

<div class="signal-box">
<div class="live">● LIVE</div>
<div style="font-weight:800; font-size:12px; color:#0a3d62;">XAUUSD GOLD • Maphotla Sniper</div>
<div id="price" style="font-size:22px; font-weight:900; color:#03a9f4; margin:6px 0;">$2,684.52</div>
<div id="sig" style="background:#e8f5e9; color:#2e7d32; padding:6px 10px; border-radius:8px; font-weight:800; font-size:10px; display:inline-block;">🟢 BUY • 6/6 GUNS CONFIRMED</div>
</div>

<div class="info-cards">
<div class="mini-card"><h5>WIN RATE</h5><p>94.7% 🎯</p></div>
<div class="mini-card"><h5>PROFIT</h5><p style="color:#00c853;">+$342</p></div>
<div class="mini-card"><h5>ACTIVE</h5><p>3 Bots 🔫</p></div>
<div class="mini-card"><h5>LOCATION</h5><p>Maphotla 🇿🇦</p></div>
</div>

<div class="bottom-nav">
<div class="nav-icon active"><i class="fas fa-home"></i></div>
<div class="nav-icon"><i class="fas fa-chart-line"></i></div>
<div class="nav-icon"><i class="fas fa-robot"></i></div>
</div>
</div>
</div>
<script>
function addRobot(){
 alert('🔫 SIX GUN PRO V5 • MAPHOTLA\\n\\n✅ Robot Hosted Successfully\\n✅ 6 Guns Activated\\n✅ Location: Maphotla, SA\\n\\nSniper starting...');
 document.getElementById('sig').innerText = '⏳ SNIPING...';
 setTimeout(()=>{document.getElementById('sig').innerText='🎯 EXECUTED +$18.50'; document.getElementById('sig').style.background='#e3f2fd';},2500);
}
setInterval(()=>{let p=(2684+Math.random()*5).toFixed(2); document.getElementById('price').innerText='$'+p;},2000);
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {"status":"live","brand":"Six Gun Pro V5 Maphotla"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
