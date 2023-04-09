import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import random
import pandas as pd
import time
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_title='Data Visualization',
    page_icon='✅',
    layout='wide'
)

st.title("Data Visualization")

job_filter = st.selectbox("Select the Job", pd.unique(df['job']))

placeholder = st.empty()

df = df[df['job'] == job_filter]

for seconds in range(200):

    df['age_new'] = df['age'] * np.random.choice(range(1, 5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1, 5))

    avg_age = np.mean(df['age_new'])

    count_married = int(df[(df["marital"] == 'married')]['marital'].count() + np.random.choice(range(1, 30)))

    balance = np.mean(df['balance_new'])

    with placeholder.container():

        fig_col1, fig_col2 = st.columns(2)
        fig_col3, fig_col4 = st.columns(2)
        fig_col5, fig_col6 = st.columns(2)
        fig_col7, fig_col8 = st.columns(2)
        fig_col9, fig_col10 = st.columns(2)
        with fig_col1:
            st.markdown("### Density Chart")
            fig = px.density_heatmap(data_frame=df, y='age_new', x='marital')
            st.write(fig)
        with fig_col2:
            st.markdown("### Histogram Chart")
            fig2 = px.histogram(data_frame=df, x='age_new')
            st.write(fig2)
        with fig_col3:
            st.markdown("### Line Chart")
            fig3 = px.line(data_frame=df, y='age_new', x='marital')
            st.write(fig3)
        with fig_col4:
            st.markdown("### Bar Chart")
            fig4 = px.bar(data_frame=df, y='age_new', x='marital')
            st.write(fig4)
        with fig_col5:
            st.markdown("### Area Chart")
            fig5 = px.area(data_frame=df, y='age_new', x='marital')
            st.write(fig5)
        with fig_col6:
            st.markdown("### Funnel Chart")
            fig6 = px.funnel(data_frame=df, y='age_new', x='marital')
            st.write(fig6)
        with fig_col7:
            st.markdown("### ECDF Chart")
            fig7 = px.ecdf(data_frame=df, y='age_new', x='marital')
            st.write(fig7)
        with fig_col8:
            st.markdown("### Strip Chart")
            fig8 = px.strip(data_frame=df, y='age_new', x='marital')
            st.write(fig8)
        with fig_col9:
            st.markdown("### Violin Chart")
            fig9 = px.violin(data_frame=df, y='age_new', x='marital')
            st.write(fig9)
        with fig_col10:
            st.markdown("### Scatter Chart")
            fig10 = px.scatter(data_frame=df, y='age_new', x='marital')
            st.write(fig10)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)