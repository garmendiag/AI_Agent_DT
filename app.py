import streamlit as st
import pandas as pd
from datetime import datetime

st.title("ES Trading Dashboard")
st.write("Log entries, reasoning, P&L—analyze edge.")

# Upload log (CSV from your trades.log)
uploaded_file = st.file_uploader("Upload trades.log as CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)  # Shows full table

    # P&L Calc
    df['P&L'] = pd.to_numeric(df['Outcome $'], errors='coerce')  # Assumes 'Outcome $' column
    total_pnl = df['P&L'].sum()
    hit_rate = (df['Hit/Miss'] == 'Hit').mean() * 100 if 'Hit/Miss' in df.columns else "Add column"
    st.metric("Total P&L", f"${total_pnl:.2f}")
    st.metric("Hit Rate", f"{hit_rate:.1f}%")

    # Reasoning Analysis (top patterns)
    if 'Reasoning' in df.columns:
        common_reasons = df['Reasoning'].value_counts().head(5)
        st.bar_chart(common_reasons)

    # Effectiveness Chart
    st.line_chart(df.set_index('Timestamp')['P&L'].cumsum())  # Cumulative P&L
else:
    st.info("Upload CSV: Columns—TS, Direction, Confidence, Reasoning, Entry, Stop, Target, Outcome $, Hit/Miss.")

# Quick Log Entry
with st.expander("New Entry"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    direction = st.text_input("Direction + Confidence")
    reasoning = st.text_area("Reasoning")
    entry = st.number_input("Entry Price")
    stop = st.number_input("Stop")
    target = st.number_input("Target")
    outcome = st.number_input("Outcome $")
    if st.button("Log It"):
        new_row = pd.DataFrame({"TS": [ts], "Direction": [direction], "Reasoning": [reasoning], "Entry": [entry], "Stop": [stop], "Target": [target], "Outcome $": [outcome], "Hit/Miss": ["Hit" if outcome > 0 else "Miss"]})
        new_row.to_csv("trades.csv", mode='a', header=False, index=False)
        st.success("Logged! Refresh upload.")
