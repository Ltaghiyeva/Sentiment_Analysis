import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle


# Set page title and favicon
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon=":smiley:",
    layout="wide"
)

# Define page layout
def page_layout():
    st.markdown("<h1 style='text-align: center;'>Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.write("")
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.write("")
    with col2:
        user_input = st.text_input("Enter text for sentiment analysis:", value='', max_chars=None, key=None, type='default')
        st.write("")
        if st.button('Analyze', key="analyze_button"):
            sentiment = analyze_sentiment(user_input)
            if sentiment == 'Positive':
                st.success("Sentiment: Positive! 👍")
            elif sentiment == 'Negative':
                st.error("Sentiment: Negative! 👎")
            else:
                st.warning("Sentiment: Neutral! 😐")
    with col3:
        st.write("")
    st.write("")

# Define sentiment analysis function
def analyze_sentiment(input_text):


    # Function to analyze sentiment
    # Replace with your actual sentiment analysis code
    # This is just a sample code that randomly assigns sentiment

    filename='/Users/lamantaghiyevaltaghiyeva/Desktop/Stream/Sentiment_pipeline.pkl'
    with open(filename,'rb') as file:
        text_clf = pickle.load(file)
    sentiment = text_clf.predict([input_text])[0]
    sentiments.append(sentiment)
    return sentiment
        
    

# Define chart function
def plot_sentiment_chart(sentiments):
    df = pd.DataFrame(sentiments, columns=['Sentiment'])
    fig = px.histogram(df, x='Sentiment', color='Sentiment', color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(
        title="Sentiment Distribution",
        xaxis_title="Sentiment",
        yaxis_title="Count",
        font=dict(size=18),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    return st.plotly_chart(fig)

def plot_sentiment_pie(sentiments):
    df = pd.DataFrame(sentiments, columns=['Sentiment'])
    fig = px.pie(df, names='Sentiment', color='Sentiment', color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(
        title="Sentiment Distribution",
        font=dict(size=18),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    return st.plotly_chart(fig)

# Define page footer
def page_footer():
    st.write("")
    st.write("---")
    st.write("")
    


    col1, col2 = st.columns(2)
    with col1:
        plot_sentiment_chart(sentiments)
    with col2:
        plot_sentiment_pie(sentiments)
    st.write("")

# Define app
def app():
    page_layout()
    page_footer()

# Run app
if __name__ == '__main__':
    sentiments = []
    app()
