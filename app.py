import streamlit as st
import json, os
from datetime import datetime

st.set_page_config(page_title="SIX GUN PRO V5", page_icon="🔫", layout="centered")

SAVE_FILE = "trades_history.json"
LOGIN_FILE = "logins.json"

def load_json(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            try: return json.load(f)
            except: return []
    return [] if "trades" in file else {}

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

# INIT SESSION
if "started" not in st.session_state:
    st.session_state.started = False
if "step" not in st.session_state:
    st.session_state.step = 1

# --- CSS ---
st.markdown("""
<style>
.big-title {text-align:center;color:#00f2ff;font-size:32px;font-weight:bold;}
.sub {text-align:center;color:gray;}
.stButton>button {background:#00f2ff;color:black;font-weight:bold;border-radius:10px;height:50px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🔫 SIX GUN PRO V5<br>MAPHOTLA</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">AI Sniper Trading System 🇿🇦</div>', unsafe_allow_html=True)
st.divider()

# --- START SCREEN ---
if not st.session_state.started:
    st.markdown("### Welcome to Six Gun Pro V5")
    st.info("Professional Trading App with Razor Markets")
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=150)
    if st.button("🚀 TAP TO START", use_container_width=True):
        st.session_state.started = True
        st.session_state.step = 1
        st.rerun()
    st.stop()

# --- STEP 1: CHOOSE PLATFORM ---
st.markdown(f"**STEP {st.session_state.step} / 3**")
if st.session_state.step == 1:
    st.markdown("## 1️⃣ CHOOSE TRADING PLATFORM")
    platform = st.radio("Select Platform:", ["MT4", "MT5"], horizontal=True)
    st.session_state.platform = platform
    st.success(f"Selected: {platform}")
    if st.button("NEXT → CHOOSE MARKET", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --- STEP 2: MARKET LIST ---
elif st.session_state.step == 2:
    st.markdown("## 2️⃣ CHOOSE MARKET")
    st.caption(f"Platform: {st.session_state.platform}")

    markets = {
        "🔥 RAZOR MARKETS (Exclusive)": [
            "Razor Volatility 100", "Razor Volatility 75", "Razor Boom 1000",
            "Razor Crash 1000", "Razor Step Index", "Razor Range Break"
        ],
        "📈 Synthetic Indices": [
            "Volatility 10 Index", "Volatility 25 Index", "Volatility 50 Index",
            "Volatility 75 Index", "Volatility 100 Index",
            "Boom 300 Index", "Boom 500 Index", "Boom 1000 Index",
            "Crash 300 Index", "Crash 500 Index", "Crash 1000 Index",
            "Step Index", "Range Break 100/200"
        ],
        "💱 Forex": [
            "EURUSD", "GBPUSD", "USDJPY", "XAUUSD (Gold)", "USDCAD", "AUDUSD"
        ],
        "₿ Crypto": ["BTCUSD", "ETHUSD", "SOLUSD"]
    }

    category = st.selectbox("Market Category", list(markets.keys()))
    market = st.selectbox("Select Market", markets[category])
    st.session_state.market = market

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← BACK"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("NEXT → LOGIN", use_container_width=True):
            st.session_state.step = 3
            st.rerun()

# --- STEP 3: LOGIN DETAILS ---
elif st.session_state.step == 3:
    st.markdown("## 3️⃣ LOGIN DETAILS")
    st.caption(f"{st.session_state.platform} | {st.session_state.market}")

    saved = load_json(LOGIN_FILE)

    with st.form("login"):
        st.markdown(f"### Login to {st.session_state.platform}")
        if st.session_state.platform == "MT4":
            login_id = st.text_input("MT4 Login ID", value=saved.get("login","") if isinstance(saved, dict) else "")
            password = st.text_input("MT4 Password", type="password")
            server = st.text_input("MT4 Server", placeholder="e.g. RazorMarkets-Live", value="Razor Markets")
        else:
            login_id = st.text_input("MT5 Login ID", value=saved.get("login","") if isinstance(saved, dict) else "")
            password = st.text_input("MT5 Password", type="password")
            server = st.text_input("MT5 Server", placeholder="e.g. RazorMarkets-Live", value="Razor Markets")

        api_key = st.text_input("API Key (Optional)", type="password")

        submitted = st.form_submit_button("🔐 SAVE LOGIN & ENTER TRADING", use_container_width=True)
        if submitted:
            save_json(LOGIN_FILE, {"platform": st.session_state.platform, "market": st.session_state.market, "login": login_id, "server": server})
            st.session_state.logged_in = True
            st.success(f"✅ Logged in to {st.session_state.platform} - {st.session_state.market}")
            st.balloons()

    if st.session_state.get("logged_in"):
        st.divider()
        st.markdown("### 🎯 SIX GUN TRADING PANEL")
        c1, c2 = st.columns(2)
        with c1:
            stake = st.number_input("Stake ($)", 0.35, 1000.0, 1.0)
            action = st.selectbox("Action", ["BUY", "SELL"])
        with c2:
            lot = st.number_input("Lot Size", 0.01, 10.0, 0.01)
            sl = st.number_input("Stop Loss", value=10.0)

        if st.button(f"🔫 FIRE {action} ON {st.session_state.market}", use_container_width=True):
            trade = {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "platform": st.session_state.platform,
                "market": st.session_state.market,
                "action": action,
                "stake": stake,
                "lot": lot,
                "sl": sl,
                "status": "SAVED"
            }
            trades = load_json(SAVE_FILE)
            if not isinstance(trades, list): trades = []
            trades.append(trade)
            save_json(SAVE_FILE, trades)
            st.success(f"Trade SAVED! {action} {st.session_state.market}")

        st.divider()
        st.markdown("### 📜 SAVED TRADES")
        trades = load_json(SAVE_FILE)
        if isinstance(trades, list) and trades:
            st.dataframe(trades[::-1], use_container_width=True)
            st.download_button("📥 Download Trades", json.dumps(trades, indent=2), "maphotla_trades.json")
        else:
            st.info("No trades yet. Fire first shot!")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← BACK TO MARKETS"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("🏠 RESTART"):
            st.session_state.started = False
            st.session_state.step = 1
            st.rerun()
