import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
st.set_option('deprecation.showPyplotGlobalUse', False)

################## main #####################

st.subheader("Streamlit application on wordcloud")
st.text("Only for Text Data")

uploaded_file = st.file_uploader("Choose a file")

st.title("Word Cloud Generator")
st.sidebar.header("Word Cloud Settings")
max_words = st.sidebar.slider("Max Words", 100, 500, 200)
background_color = st.sidebar.color_picker("Background Color", "#ffffff")
st_option = st.sidebar.selectbox("Column", ['title', 'category'])

################# sidebar #####################

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if st_option in df.columns:
        text = " ".join(df[st_option].dropna().astype(str))  # Ensure the column exists and handle NaN values
        word_cloud = WordCloud(max_words=max_words, background_color=background_color, height=2000, width=2000)
        word_cloud = word_cloud.generate(text)
        plt.imshow(word_cloud, interpolation='bilinear')
        plt.title(f"Most common words in {st_option}")
        plt.axis('off')
        st.pyplot()
    else:
        st.error(f"The column '{st_option}' is not present in the uploaded file.")

if uploaded_file is not None and st.sidebar.checkbox("Display Data", value=False):
    st.write(df.head())