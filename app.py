import streamlit as st
import pandas as pd
import plotly.express as px  # Lightweight charts
from datetime import datetime
import secrets  # For simple password

# Page Config & Dark Chic Theme (Design Tune)
st.set_page_config(page_title="ES Dashboard", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>
.main {background-color: #ffffff;}
.stApp {background-color: #ffffff; color: #000000;}
.sidebar .sidebar-content {background-color: #f0f2f6;}
.metric-container {background-color: #e8f4fd; color: #000000;}
h1 {font-family: 'Arial', sans-serif; color: #1f77b4; font-size: 2rem;}
.stMetric {font-family: 'Arial', sans-serif; font-size: 1.2rem;}
</style>
""", unsafe_allow_html=True)

# Simple Password Gate (Security)
if 'password' not in st.session_state:
    st.session_state.password = ''
if st.session_state.password != 'your_secret_pass':  # Change to something secure like "esEdge2025!"
    st.session_state.password = st.text_input("Enter Password to View", type="password")
    if st.session_state.password == 'your_secret_pass':
        st.rerun()
    st.stop()

st.title("FIBO TRADING LLC")
st.write("Log entries, reasoning, P&L—analyze edge. Tuned for perf: 10s refresh, masked IDs.")

# Sidebar (Always Visible)
with st.sidebar:
    st.header("Auto Status")
    status = st.selectbox("Status", ["● ON (GREEN)", "● OFF (RED)"])
    if status == "● ON (GREEN)":
        col1, col2 = st.columns(2)
        col1.button("KILL SWITCH", type="primary")
        col2.button("RESUME")
    st.subheader("Trading Window")
    st.text("RTH 09:30–16:00 ET • Holidays: NYSE")
    st.subheader("Risk Limits")
    st.text("1% per trade • Daily stop −2R • Lock +3R")
    st.subheader("Circuit Breakers")
    st.checkbox("News")
    st.checkbox("Wide-Spread")
    st.checkbox("Data Outage")
    st.checkbox("Broker")
    st.subheader("Health Mini")
    st.text("MD WS:OK • USER WS:OK • REST:OK • CPU 22% • Mem 48% • Disk 3G")
    st.subheader("Nav")
    st.radio("View", ["Dashboard", "Trades", "Edge & Drift", "Risk", "Health", "Review"])

# Sticky KPIs (Top Bar)
col1, col2, col3, col4 = st.columns(4)
col1.metric("P&L Today", "+1.6R / $420", delta="+0.4R", delta_color="normal")
col2.metric("Max DD", "−0.6R", delta="−0.2R", delta_color="inverse")
col3.metric("Trades", "2 / 3")
col4.metric("Expectancy", "+0.28R")
col5, col6 = st.columns(2)
col5.metric("Utilization", "14%")
col6.metric("Risk State", "▓ GREEN")

# Market Context & Execution (Split Columns)
col_left, col_right = st.columns(2)
with col_left:
    st.subheader("Market Context (ES/NQ)")
    st.text("Auction State: IMBALANCED ↑ Confidence: 72%")
    st.text("Profile: VAH 6751 • POC 6742 • VAL 6733")
    st.text("VPOC drift: ↑↑ (last 5 bars)")
    st.text("Δ / Volume z: 5m +1.1 | 1m +1.7")
    st.text("vWAP bands • IB • ONH/ONL badges")
    fig = px.line(pd.DataFrame({"x": [1,2,3], "y": [6733,6742,6751]}), x="x", y="y", title="ES 5m Chart (Last 20 Bars)")
    st.plotly_chart(fig, use_container_width=True)  # Lightweight tune
with col_right:
    st.subheader("Execution (MES/MNQ)")
    st.text("Positions: MES +1 MNQ 0")
    st.text("Working Orders: 1")
    st.text("Slippage (avg): 0.8 ticks")
    st.text("Markouts: +30s +0.3R | +5m +0.2R")
    st.text("Latency: sig→order 140ms →fill 320ms")
    df_orders = pd.DataFrame({"Order": ["Buy MES"], "Fill": ["6738.25"], "Reject": ["None"]})
    st.dataframe(df_orders)

# Autonomy Gates (Visual Tune: Simple Checkboxes)
st.subheader("Autonomy Gates (All True for New Orders)")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Trading Window", "✅ Open")
col2.metric("Risk", "✅ ≠ RED")
col3.metric("Data/Broker", "✅ OK")
col4.metric("No Breaker", "✅ Active")
col5.metric("Strategy Gate", "❌ Passed")

# State & Regime + Risk Guardrails (Split)
col_left, col_right = st.columns(2)
with col_left:
    st.subheader("State & Regime")
    st.text("State: IMBALANCED_UP (edge: VAL reclaim)")
    st.text("Regime: OpenDrive → Normalizing")
    st.text("Evidence: vol_z1m 1.8 • delta_z1m 1.5")
    st.text("POC shifts: 3 up")
with col_right:
    st.subheader("Risk & Guardrails")
    st.text("Per-trade: 1% Daily: −2R / +3R")
    st.text("Exposure timeline (contracts)")
    st.text("Circuit trips today: News(10:01)")
    st.text("Three-strikes: 1/3")

# Live Event Stream (Perf Tune: Button Refresh)
st.subheader("Live Event Stream")
if st.button("Refresh Events (10s Poll)"):  # Avoids CPU spike
    st.text("14:15:00Z signal ES state=imbalanced_up conf=0.72 plan: L 6738 / SL 6730")
    st.text("14:15:02Z order MES buy 1 @ 6738.00 client_id=***")  # Masked for security
    st.text("14:15:02Z fill MES 6738.25 slip=1t lat=320ms")
    st.text("14:20:00Z signal take TP1 +1R at 6746 move BE-1t")

# Trade Cards + Edge Quality (Split)
col_left, col_right = st.columns(2)
with col_left:
    st.subheader("Trade Cards (Today)")
    st.text("#2 Long @ VAL reclaim")
    st.text("Entry 6738 • SL 6730 • TP1 +1R hit • TP2 +2R")
    st.text("Rationale: vol_z5m 1.1 / vol_z1m 1.8 • Δ +1.5σ")
    st.text("VPOC ↑")  # Cut screenshot for perf
with col_right:
    st.subheader("Edge Quality & Drift")
    st.text("Cohorts: VAL rej | VAH rej | IB br")
    st.text("Hit 62% Exp +0.31R N=46 (30d)")
    st.text("Reliability: Pred conf vs realized")
    st.text("Drift: CUSUM steady")
    fig_bar = px.bar(pd.DataFrame({"Patterns": ["VAL rej", "VAH rej"], "Hit %": [62, 55]}), x="Patterns", y="Hit %")
    st.plotly_chart(fig_bar, use_container_width=True)

# Auto-pull from GitHub (fresh on load)
@st.cache_data(ttl=3600)  # Cache 1 hour for perf
def load_csv():
    url = "https://raw.githubusercontent.com/garmendiag/AI_Agent_DT/main/trades.csv"
    try:
        return pd.read_csv(url)
    except:
        st.info("CSV not found—add trades.csv to repo.")
        return pd.DataFrame()

df = load_csv()
if not df.empty:
    st.success("Auto-loaded fresh CSV!")
    search_term = st.text_input("Search Reasoning (e.g., 'VAL probe')")
    if search_term:
        filtered_df = df[df['Reasoning'].str.contains(search_term, case=False, na=False)]
        st.dataframe(filtered_df)
    else:
        st.dataframe(df)
    # Metrics (same as before)
    df['P&L'] = pd.to_numeric(df['Outcome $'], errors='coerce')
    total_pnl = df['P&L'].sum()
    hit_rate = (df['Hit/Miss'] == 'Hit').mean() * 100 if 'Hit/Miss' in df.columns else 0
    st.metric("Total P&L", f"${total_pnl:.2f}")
    st.metric("Hit Rate", f"{hit_rate:.1f}%")
    if 'Reasoning' in df.columns:
        common_reasons = df['Reasoning'].value_counts().head(5)
        st.bar_chart(common_reasons)
    st.line_chart(df.set_index('TS')['P&L'].cumsum())
    if st.button("Export CSV"):
        df.to_csv("download.csv", index=False)
        st.download_button("Download", data=open("download.csv", "rb"), file_name="trades_export.csv", mime="text/csv")
else:
    st.info("Upload manually or push CSV to repo.")
