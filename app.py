from flask import Flask, render_template_string
import os
app = Flask(__name__)
HTML = """
<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Six Gun Pro V5 Maphotla</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:sans-serif}
body{background:#0a0e13;display:flex;justify-content:center;min-height:100vh}
.phone{width:100%;max-width:390px;background:#7cc8f7;min-height:100vh;position:relative;padding:12px}
.inner{background:linear-gradient(180deg,#6ec6ff 0%,#a3ddff 30%,#d6efff 100%);min-height:calc(100vh - 24px);border-radius:28px;position:relative;overflow:hidden;padding-bottom:90px}
.card{margin:18px;background:rgba(78,190,255,0.55);border-radius:26px;padding:22px 15px 18px;text-align:center;position:relative;border:1.5px solid rgba(255,255,255,0.4)}
.avatar{width:110px;height:110px;border-radius:50%;margin:0 auto 12px;border:4px solid white;overflow:hidden;background:white}
.avatar img{width:100%;height:100%;object-fit:cover}
.title{color:white;font-weight:800;font-size:13px;letter-spacing:0.8px}
.btn{margin:18px;background:linear-gradient(90deg,#33b9ff,#4cc3ff);border-radius:16px;padding:16px;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:13px;width:calc(100% - 36px);border:none;cursor:pointer}
.box{margin:16px 18px 0;background:white;border-radius:16px;padding:14px}
</style></head>
<body>
<div class="phone"><div class="inner">
<div class="card">
<div class="avatar"><img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png"></div>
<div class="title">SIX GUN PRO<br>V5.0 • MAPHOTLA</div>
<div style="display:flex;justify-content:space-around;margin-top:16px;color:white;font-size:10px;font-weight:600">
<div><i class="fas fa-chart-bar"></i><br>ANALYZE</div>
<div><i class="fas fa-crosshairs"></i><br>6 GUNS</div>
<div><i class="fas fa-trash"></i><br>REMOVE</div>
</div>
</div>
<button class="btn" onclick="alert('🔫 SIX GUN PRO V5 MAPHOTLA ACTIVATED! ✅')"><i class="fas fa-plus"></i>&nbsp; ADD ROBOT - HOST ROBOT V5</button>
<div class="box">
<div style="background:#00e676;color:white;font-size:8px;font-weight:800;padding:3px 8px;border-radius:20px;display:inline-block">● LIVE</div>
<div style="font-weight:800;font-size:12px;color:#0a3d62;margin-top:4px">XAUUSD GOLD • Maphotla Sniper</div>
<div style="font-size:22px;font-weight:900;color:#03a9f4;margin:6px 0">$2,684.52</div>
<div style="background:#e8f5e9;color:#2e7d32;padding:6px 10px;border-radius:8px;font-weight:800;font-size:10px;display:inline-block">🟢 BUY • 6/6 GUNS CONFIRMED</div>
</div>
<div style="margin:16px 18px 0;display:grid;grid-template-columns:1fr 1fr;gap:10px">
<div class="box" style="margin:0"><div style="font-size:8px;color:#90a4ae">WIN RATE</div><div style="font-weight:800">94.7% 🎯</div></div>
<div class="box" style="margin:0"><div style="font-size:8px;color:#90a4ae">LOCATION</div><div style="font-weight:800">Maphotla 🇿🇦</div></div>
</div>
</div></div></body></html>
"""
@app.route('/')
def home(): return render_template_string(HTML)
@app.route('/health')
def health(): return {"status":"ok"}
if __name__ == "__main__": app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
