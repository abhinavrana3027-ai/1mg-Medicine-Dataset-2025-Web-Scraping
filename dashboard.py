#!/usr/bin/env python3
"""
1mg Medicine Dataset - Interactive Dashboard
Author: Abhinav Rana
Date: November 2025

Usage: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="1mg Medicine Dataset Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('onemg.csv')

df = load_data()

# Sidebar
st.sidebar.title("🏥 1mg Medicine Dashboard")
st.sidebar.markdown("---")
st.sidebar.markdown("""
**Project by:** Abhinav Rana  
**Dataset:** 1mg.com Medicine Data  
**Records:** {} medicines
""".format(len(df)))

# Navigation
page = st.sidebar.radio("Navigate to:", ["Overview", "Data Explorer", "Visualizations", "About"])

if page == "Overview":
    st.title("📊 1mg Medicine Dataset - Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())
    with col4:
        st.metric("Duplicates", df.duplicated().sum())
    
    st.markdown("---")
    st.subheader("📁 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 Data Types")
    dtypes_df = pd.DataFrame({
        'Column': df.dtypes.index,
        'Data Type': df.dtypes.values.astype(str)
    })
    st.dataframe(dtypes_df, use_container_width=True)

elif page == "Data Explorer":
    st.title("🔍 Data Explorer")
    
    # Search functionality
    search = st.text_input("🔎 Search medicines:", "")
    if search:
        filtered = df[df.astype(str).apply(lambda x: x.str.contains(search, case=False, na=False)).any(axis=1)]
        st.write(f"Found {len(filtered)} results")
        st.dataframe(filtered, use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)
    
    st.download_button(
        label="💾 Download Dataset (CSV)",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='1mg_medicines.csv',
        mime='text/csv'
    )

elif page == "Visualizations":
    st.title("📊 Data Visualizations")
    
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if numeric_cols:
        selected_col = st.selectbox("Select column to visualize:", numeric_cols)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Distribution")
            fig = px.histogram(df, x=selected_col, nbins=30, title=f"{selected_col} Distribution")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Box Plot")
            fig = px.box(df, y=selected_col, title=f"{selected_col} Box Plot")
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No numeric columns available for visualization")

elif page == "About":
    st.title("ℹ️ About This Project")
    
    st.markdown("""
    ## 🏥 1mg Medicine Dataset Analysis Project
    
    ### 📊 Project Overview
    This comprehensive data science project demonstrates:
    - **Web Scraping**: Data collection from 1mg.com
    - **Data Analysis**: Statistical analysis and insights
    - **Interactive Visualization**: Streamlit dashboard
    - **Production Code**: Professional structure and documentation
    
    ### 🛠️ Technologies Used
    - Python 3.8+
    - Pandas for data manipulation
    - Streamlit for web dashboard
    - Plotly for interactive visualizations
    - Matplotlib & Seaborn for static plots
    
    ### 🎯 Skills Demonstrated
    ✅ Web scraping and data collection  
    ✅ Data cleaning and preprocessing  
    ✅ Exploratory data analysis  
    ✅ Interactive dashboard development  
    ✅ Production-quality code  
    ✅ Professional documentation  
    
    ### 📧 Contact
    **Abhinav Rana**  
    GitHub: [@abhinavrana3027-ai](https://github.com/abhinavrana3027-ai)  
    
    💼 Available for Data Science & Analytics roles in Germany (Berlin preferred)
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
<small>Built with ❤️ using Streamlit</small>
""", unsafe_allow_html=True)
