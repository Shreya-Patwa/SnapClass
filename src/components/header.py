import streamlit as st

def header_home():
    logo="https://static.vecteezy.com/system/resources/previews/016/029/814/non_2x/male-graduate-glyph-round-corner-background-icon-vector.jpg"
    st.markdown(f"""
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px;margin-top:30px">
        <img src='{logo}' style='height:100px' />   
        <h1 style="text-align:centre; color:#E0E3FF;"> SNAP </br> CLASS</h1>   
    </div>
               """,unsafe_allow_html=True)
    
def header_dashboard():
    logo="https://static.vecteezy.com/system/resources/previews/016/029/814/non_2x/male-graduate-glyph-round-corner-background-icon-vector.jpg"
    st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:center;gap:10px ;margin-top:30px">
        <img src='{logo}' style='height:80px' />   
        <h2 style="text-align:left; color:#5865F2;"> SNAP </br> CLASS</h2>   
    </div>
               """,unsafe_allow_html=True)
  