
# import libraries
import pickle
import streamlit as slt
from streamlit_option_menu import option_menu

#setting up streamlit page
slt.set_page_config(layout="wide")
web=option_menu(menu_title="EMOTIONAPP",
                options=["Home","Tweet emotion analysis🤬😊"],
                orientation="horizontal"
                )
if web=="Home":
   slt.title("Twitter-Sentiment-Analysis:")
   slt.header("Detecting Hate Speech in Tweets Using Machine Learning")
   slt.subheader(":blue[skills:]  ●	Natural Language Processing (NLP) ●	Text Classification")
   slt.subheader(":blue[Objective:]")
   slt.markdown('''The objective of this task is to detect hate speech in tweets. For the sake of simplicity, 
                we say a tweet contains hate speech if it has a racist or sexist sentiment associated with it. 
                So, the task is to classify racist or sexist tweets from other tweets''')
   slt.subheader(":blue[Developed-by:]  Padma priya")
   
if web=="Tweet emotion analysis🤬😊":
    #open the model for prediction
    with open('XGBOOST.pkl','rb') as files:
       model_final=pickle.load(files)
    with open('vectorizer.pkl', 'rb') as vector_file:
       vector = pickle.load(vector_file)
    tweet=slt.text_input("Enter the tweet")
    Submit=slt.button("Predict")
    # prediction of tweet
    if Submit:
        A = vector.transform([tweet])
        prediction=model_final.predict(A)
        if prediction[0]==0:
          slt.write("NOT HATE TWEET 😊")
        else:                                       
          slt.write("HATE TWEET 🤬")
        slt.image("Untitled-6_477407.gif",width=350)
    

