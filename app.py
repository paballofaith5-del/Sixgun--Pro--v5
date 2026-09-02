from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
HTML="""
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIX GUN PRO V5</title><style>
body{background:#000;color:#fff;font-family:Arial;text-align:center;margin:0}
.circle{width:170px;height:170px;border-radius:50%;border:3px solid #00e5ff;box-shadow:0 0 25px #00e5ff;margin:35px auto 10px;overflow:hidden}
.circle img{width:100%;height:100%;object-fit:cover}
.card{border:1.5px solid #00e5ff;border-radius:22px;display:flex;justify-content:space-around;padding:18px;margin:28px 14px}
.btn{background:none;border:none;color:#00e5ff;font-size:12px;font-weight:bold}
.btn-center{border:2px solid #00e5ff;border-radius:50%;width:70px;height:70px;font-size:20px}
#log{margin:15px;background:#111;padding:10px;border-radius:10px;font-size:12px;text-align:left;min-height:50px}
</style></head><body>
<div class="circle"><img src="https://i.imgur.com/4v4H3yN.png"></div>
<h2>SIX GUN PRO V5</h2><div style="color:#aaa">Nzenga Fx Traders</div>
<div class="card">
<button class="btn" onclick="fetch('/quotes').then(r=>r.text()).then(t=>log.innerText=t)">📈<br>QUOTES</button>
<button class="btn btn-center" onclick="fetch('/trade',{method:'POST'}).then(r=>r.text()).then(t=>log.innerText=t)">▶</button>
<button class="btn" onclick="fetch('/remove',{method:'POST'}).then(r=>r.text()).then(t=>log.innerText=t)">🗑️<br>REMOVE</button>
</div><div id="log">Ready...</div></body></html>
"""
@app.route("/")
def home(): return render_template_string(HTML)
@app.route("/quotes")
def q(): return jsonify({"status":"LIVE","symbol":"XAUUSD"})
@app.route("/trade", methods=["POST"])
def t(): return jsonify({"status":"BUY executed"})
@app.route("/remove", methods=["POST"])
def r(): return jsonify({"status":"Removed"})
if __name__ == "__main__": app.run(host="0.0.0.0",port=10000)from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
HTML="""
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIX GUN PRO V5</title><style>
body{background:#000;color:#fff;font-family:Arial;text-align:center;margin:0}
.circle{width:170px;height:170px;border-radius:50%;border:3px solid #00e5ff;box-shadow:0 0 25px #00e5ff;margin:35px auto 10px;overflow:hidden}
.circle img{width:100%;height:100%;object-fit:cover}
.card{border:1.5px solid #00e5ff;border-radius:22px;display:flex;justify-content:space-around;padding:18px;margin:28px 14px}
.btn{background:none;border:none;color:#00e5ff;font-size:12px;font-weight:bold}
.btn-center{border:2px solid #00e5ff;border-radius:50%;width:70px;height:70px;font-size:20px}
#log{margin:15px;background:#111;padding:10px;border-radius:10px;font-size:12px;text-align:left;min-height:50px}
</style></head><body>
<div class="circle"><img src="https://i.imgur.com/4v4H3yN.png"></div>
<h2>SIX GUN PRO V5</h2><div style="color:#aaa">Nzenga Fx Traders</div>
<div class="card">
<button class="btn" onclick="fetch('/quotes').then(r=>r.text()).then(t=>log.innerText=t)">📈<br>QUOTES</button>
<button class="btn btn-center" onclick="fetch('/trade',{method:'POST'}).then(r=>r.text()).then(t=>log.innerText=t)">▶</button>
<button class="btn" onclick="fetch('/remove',{method:'POST'}).then(r=>r.text()).then(t=>log.innerText=t)">🗑️<br>REMOVE</button>
</div><div id="log">Ready...</div></body></html>
"""
@app.route("/")
def home(): return render_template_string(HTML)
@app.route("/quotes")
def q(): return jsonify({"status":"LIVE","symbol":"XAUUSD"})
@app.route("/trade", methods=["POST"])
def t(): return jsonify({"status":"BUY executed"})
@app.route("/remove", methods=["POST"])
def r(): return jsonify({"status":"Removed"})
if __name__ == "__main__": app.run(host="0.0.0.0",port=10000)
