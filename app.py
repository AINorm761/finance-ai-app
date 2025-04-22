import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("💰 Smart Savings Planner AI")

# Sidebar Inputs
st.sidebar.header("Enter Your Monthly Info:")
income = st.sidebar.number_input("Monthly Income ($)", min_value=0)
expenses = st.sidebar.number_input("Monthly Expenses ($)", min_value=0)
savings_goal = st.sidebar.number_input("Monthly Savings Goal ($)", min_value=0)
initial_savings = st.sidebar.number_input("Current Savings ($)", min_value=0)
interest_rate = st.sidebar.slider("Annual Interest Rate (%)", 0.0, 10.0, 2.0)

# Calculations
leftover = income - expenses
can_save = leftover >= savings_goal
monthly_interest = (interest_rate / 100) / 12
months = 12

# Savings Projection
savings = []
current = initial_savings

for month in range(1, months + 1):
    if can_save:
        current += savings_goal
    current += current * monthly_interest
    savings.append(current)

# Display Summary
st.header("📊 Summary")
st.write(f"**Income:** ${income}")
st.write(f"**Expenses:** ${expenses}")
st.write(f"**Leftover:** ${leftover}")
st.write(f"**You {'can' if can_save else 'cannot'} meet your monthly savings goal of ${savings_goal}.**")

# Chart
st.markdown("---")
st.subheader("📈 Projected Savings Over 12 Months")
df = pd.DataFrame({
    "Month": list(range(1, months + 1)),
    "Projected Savings ($)": savings
})
st.line_chart(df.set_index("Month"))

# Tips
if income > 0:
    tip = np.random.choice([
        "Set up auto-transfers to your savings.",
        "Track daily spending for a week.",
        "Try meal prepping to save on food costs.",
        "Use cashback/rewards apps for everyday spending."
    ])
    st.markdown("💡 **Savings Tip:** " + tip)
