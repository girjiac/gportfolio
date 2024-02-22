import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2, gap="small")
with col1:

    st.image('images/GirijaAI4.jpg', width=75)
with col2:
    st.title('Girija Chinnaraj')
    content = """
    Hi, I am Girija! I am a Python learner, and founder of 6F. 
    I graduated in 2023 with a Master of Science in Computer Technologies from the University of Bharathiar in India with a focus on using Python for remote sensing.
    """
    st.info(content)
