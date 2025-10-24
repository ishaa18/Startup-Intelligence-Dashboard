# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.title("🚀 Startup Growth Intelligence Dashboard")

# df = pd.read_csv('startupdashboard/data/transactions.csv', parse_dates=['date'])
# df['month'] = df['date'].dt.to_period('M')

# mrr = df.groupby('month')['amount'].sum().reset_index()

# fig = px.line(mrr, x='month', y='amount', title='Monthly Recurring Revenue')
# st.plotly_chart(fig)

# st.metric("Total Revenue", f"${df['amount'].sum():,.0f}")
# st.metric("Total Transactions", f"{len(df):,}")
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚀 Startup Growth Intelligence Dashboard")

# Load data
# df = pd.read_csv('startupdashboard/data/transactions.csv', parse_dates=['date'])
df = pd.read_csv(r"C:\Users\ishap\OneDrive\Desktop\clg\tutpy\startupdashboard\data\transactions.csv", parse_dates=['date'])

# Ensure the file and columns exist
if 'date' not in df.columns or 'amount' not in df.columns:
    st.error("❌ CSV must contain 'date' and 'amount' columns.")
else:
    df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()

    # Compute MRR
    mrr = df.groupby('month', as_index=False)['amount'].sum()

    # Plot MRR
    fig = px.line(mrr, x='month', y='amount', title='Monthly Recurring Revenue')
    st.plotly_chart(fig, use_container_width=True)

    # Display KPIs
    st.metric("Total Revenue", f"${df['amount'].sum():,.0f}")
    st.metric("Total Transactions", f"{len(df):,}")
