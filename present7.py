import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Bayesian Network for Heart Disease Diagnosis", layout="wide")

# ---------- BACKGROUND IMAGE ----------
def set_bg(image_file):

    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        h1,h2,h3,h4,h5,h6,p,li {{
            color:white;
        }}

        .slide-box{{
        height:80vh;
        display:flex;
        justify-content:center;
        align-items:center;
        }}

        .slide-content{{
        text-align:left;
        font-size:28px;
        margin-top:-110px;
        }}

        .slide-title{{
        text-align:center;
        font-size:48px;
        font-weight:bold;
        margin-bottom:25px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("stream3.png")


# ---------- SIDEBAR ----------
st.sidebar.title("Presentation Slides")

st.sidebar.markdown(
"""
### Project Link
[Open Colab Project](https://colab.research.google.com/drive/1QiA66JO9Ih8pezuM1I9ZSj3laZSdkelM#scrollTo=styyoEjOpe3z)

📊 **PPT Presentation**  
[Open PPT Presentation](https://onedrive.live.com/personal/7cf96e7fa5ee36e6/_layouts/15/doc.aspx?resid=f7c49e19-9dcc-4747-ad3a-79b1a537c457&cid=7cf96e7fa5ee36e6)

"""
)

slide = st.sidebar.radio(
    "Go to",
    [
        "Title",
        "Aim",
        "Purpose",
        "Bayesian Network Concept",
        "Working Principle",
        "Applications",
        "Advantages"
    ]
)


# -------- TITLE SLIDE --------
if slide == "Title":

    st.markdown("""
    <div style="
    height:80vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
    color:white;
    font-family:'Patrick Hand', cursive;
    ">

    <p style="font-size:45px;">	 
    Bayesian Network for Heart Disease Diagnosis <br>

    <h2>Machine Learning Algorithm Lab</h2>
	
    <h3>MSc DS & AI</h3>​ 
    
    <h3>Shyam Sundar V</h3> 

    <h3>Reg No: 253692301025</h3> 

    </p>

    </div>
    """, unsafe_allow_html=True)


# -------- AIM --------
elif slide == "Aim":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Aim</div>

    • To construct a Bayesian Network using a heart disease dataset <br>
    • To analyze relationships between medical attributes and heart disease <br>
    • To predict the presence of heart disease using probabilistic reasoning <br>
    • To understand Bayesian inference in medical diagnosis

    </div>
    </div>
    """, unsafe_allow_html=True)


# -------- PURPOSE --------
elif slide == "Purpose":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Purpose</div>

    • To understand probabilistic graphical models in machine learning <br>
    • To explore how Bayesian Networks represent dependencies among variables <br>
    • To apply Bayesian inference for predicting heart disease diagnosis

    </div>
    </div>
    """, unsafe_allow_html=True)


# -------- CONCEPT --------
elif slide == "Decision Tree Concept":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Bayesian Network Concept</div>

    • A Bayesian Network is a probabilistic graphical model <br>
    • It represents variables and their conditional dependencies <br>
    • Nodes represent variables such as age, blood pressure, and cholesterol <br>
    • Edges represent probabilistic relationships between variables

    </div>
    </div>
    """, unsafe_allow_html=True)


# -------- WORKING PRINCIPLE --------
elif slide == "Working Principle":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Working Principle</div>

    • A heart disease dataset is used to build the Bayesian Network <br>
    • The network models dependencies between medical features <br>
    • Conditional probabilities are calculated for each variable <br>
    • Bayesian inference predicts the probability of heart disease

    </div>
    </div>
    """, unsafe_allow_html=True)



# -------- APPLICATIONS --------
elif slide == "Applications":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Applications</div>

    • Medical diagnosis systems <br>
    • Risk assessment in healthcare <br>
    • Fault detection in engineering systems <br>
    • Decision support systems

    </div>
    </div>
    """, unsafe_allow_html=True)


# -------- ADVANTAGES --------
elif slide == "Advantages":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Advantages</div>

    • Handles uncertainty effectively <br>
    • Represents causal relationships between variables <br>
    • Useful for probabilistic reasoning and prediction <br>
    • Widely used in medical and diagnostic systems

    </div>
    </div>
    """, unsafe_allow_html=True)
