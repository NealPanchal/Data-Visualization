import streamlit as st
import numpy as np
import random
import pandas as pd
import time
import plotly.express as px


st.set_page_config(
    page_title='Data Visualization',
    page_icon='✅',
    layout='wide'
)

st.title("Data Visualization")

csv_url = st.text_input("Enter the CSV file URL")

if csv_url:
    df = pd.read_csv(csv_url)

    filter_cols = st.multiselect("Select columns to filter by", options=list(df.columns))

    if filter_cols:

        df = df[filter_cols]
        group_col = st.selectbox("Select column to group by", options=list(df.columns))

        if group_col:
            grouped_df = df.groupby(group_col)

            chart_type = st.selectbox("Select chart type", options=["Bar", "Histogram", "Violin", "Line", "Box", "Scatter","Funnel", "Strip", "ECDF", "Bar Polar", "Line Polar", "Area", "Density Contour", "Density HeatMap" ])

            if chart_type:
                with st.spinner("Generating chart..."):

                    if chart_type == "Bar":
                        fig = px.bar(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Violin":
                        fig = px.violin(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Histogram":
                        fig = px.histogram(data_frame=df, x=group_col)

                    elif chart_type == "Line":
                        fig = px.line(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Box":
                        fig = px.box(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Scatter":
                        fig = px.scatter(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Funnel":
                        fig = px.funnel(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Strip":
                        fig = px.strip(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "ECDF":
                        fig = px.ecdf(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Bar Polar":
                        fig = px.bar_polar(data_frame=df, r=np.random.rand(len(df)))


                    elif chart_type == "Line Polar":
                        fig = px.line_polar(data_frame=df, r=np.random.rand(len(df)))

                    elif chart_type == "Area":
                        fig = px.area(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Density Contour":
                        fig = px.density_contour(data_frame=df, x=group_col, y=np.random.rand(len(df)))

                    elif chart_type == "Density HeatMap":
                        fig = px.density_heatmap(data_frame=df, x=group_col, y=np.random.rand(len(df)))



                    st.plotly_chart(fig)

                st.markdown("### Detailed Data View")
                st.dataframe(df)
