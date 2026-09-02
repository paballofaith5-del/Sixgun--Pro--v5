import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="SIX GUN PRO V5 - MAPHOTLA", page_icon="🔫", layout="wide")

# --- SAVE TRADES ---
SAVE_FILE = "trades_history.json"
LOGIN_FILE = "login_details.json"

def load_trades():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return []

def save_trade(trade):
    trades = load_trades()
    trades.append(trade)
    with open(SAVE_FILE, "w") as f:
        json.dump(trades, f, indent=2)

def load_login():
    if os.path.exists(LOGIN_FILE):
        with open(LOGIN_FILE, "r") as f:
            return json.load(f)
    return {}

def save_login(data):
    with open(LOGIN_FILE, "w") as f:
        json.dump(data, f, indent=2)

# --- HEADER ---
st.markdown("""
<h1 style='text-align:center;color:#00f2ff;'>🔫 SIX GUN PRO V5 • MAPHOTLA 🤖</h1>
<p style='text-align:center;'>AI Sniper Trading System - Made in Maphotla 🇿🇦</p>
""", unsafe_allow_html=True)

# --- STEP 1: CHOOSE PLATFORM ---
st.markdown("### 1️⃣ CHOOSE TRADING PLATFORM")
platform = st.selectbox("Select your broker:", 
    ["-- Choose --", "Razor Markets", "Deriv", "MT5 Synthetic", "Binance", "Exness", "Other"])

if platform != "-- Choose --":
    st.success(f"Selected: {platform}")
    
    # --- STEP 2: LOGIN DETAILS ---
    st.markdown(f"### 2️⃣ LOGIN DETAILS FOR {platform.upper()}")
    
    saved = load_login()
    
    with st.form("login_form"):
        if platform == "Razor Markets":
            account_id = st.text_input("Razor Markets Account ID", value=saved.get("account_id",""))
            api_key = st.text_input("Razor Markets API Key", value=saved.get("api_key",""), type="password")
            server = st.selectbox("Server", ["Live", "Demo"])
            password = st.text_input("Password", type="password")
        elif platform == "Deriv":
            account_id = st.text_input("Deriv API Token", value=saved.get("account_id",""), type="password")
            api_key = st.text_input("App ID", value=saved.get("api_key",""))
            server = st.selectbox("Server", ["Real", "Demo"])
            password = ""
        else:
            account_id = st.text_input("Account ID / Email", value=saved.get("account_id",""))
            api_key = st.text_input("API Key / Token", value=saved.get("api_key",""), type="password")
            server = st.text_input("Server", value=saved.get("server",""))
            password = st.text_input("Password", type="password")
        
        login_btn = st.form_submit_button(f"🔐 LOGIN TO {platform.upper()}", use_container_width=True)
        
        if login_btn:
            save_login({"platform": platform, "account_id": account_id, "api_key": api_key, "server": server})
            st.success(f"✅ Logged in to {platform}! Details saved!")
            st.balloons()

    # --- STEP 3: TRADING PANEL ---
    if saved.get("platform") == platform:
        st.markdown("### 3️⃣ SIX GUN TRADING PANEL")
        col1, col2, col3 = st.columns(3)
        with col1:
            symbol = st.selectbox("Symbol", ["Volatility 100", "Volatility 75", "Boom 1000", "Crash 1000", "XAUUSD", "EURUSD", "BTCUSD"])
        with col2:
            stake = st.number_input("Stake $", value=1.0, min_value=0.35)
        with col3:
            action = st.selectbox("Action", ["BUY", "SELL"])
        
        if st.button(f"🎯 FIRE {action} - SIX GUN SHOT!", use_container_width=True):
            trade = {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "platform": platform,
                "account": account_id[:4]+"****" if account_id else "N/A",
                "symbol": symbol,
                "action": action,
                "stake": stake,
                "result": "PENDING"
            }
            save_trade(trade)
            st.success(f"🔫 FIRED! {action} {symbol} ${stake} on {platform} - SAVED!")
        
        # --- SAVED TRADES ---
        st.markdown("### 4️⃣ SAVED TRADES HISTORY")
        trades = load_trades()
        if trades:
            st.dataframe(trades[::-1], use_container_width=True)
            st.download_button("📥 Download Trades JSON", json.dumps(trades, indent=2), "my_trades.json")
            if st.button("🗑️ Clear All Trades"):
                os.remove(SAVE_FILE)
                st.rerun()
        else:
            st.info("No trades saved yet. Fire your first shot!")
else:
    st.warning("👆 Please choose your trading platform to start!")

st.markdown("---")
st.caption("Built in Maphotla, Mpumalanga 🇿🇦 | SIX GUN PRO V5 | Trades saved automatically")
