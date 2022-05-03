import random
import streamlit as st
import pandas as pd

st.title("Question Answering")
st.text("Hi, we are Frenki, Benjamin & Patrik and our goal is to build an application that ultimately answers")
st.text("ALL your questions regarding celebrities! :)  This application uses Deep Learning algorithms to automate this challenge!")


@st.cache
def load_data():
    df = pd.read_csv("https://media.githubusercontent.com/media/buscjona/StreamLit-Image-Captioning"
                     "/main/sample_data_oneMill.csv")
    return df


data_load_state = st.subheader("Loading data...")
df = load_data()

data_load_state.subheader("Generated questions and related answers about Michael Jackson:")


def get_image():
    column = random.randint(0, 999999)
    url = df.iloc[column]["URL"]
    st.image(url)
    st.write("real caption:")
    st.write(df.iloc[column]["TEXT"])
    st.write("URL:")
    st.write(url)


if st.button("Get a random image from the dataset."):
    get_image()
