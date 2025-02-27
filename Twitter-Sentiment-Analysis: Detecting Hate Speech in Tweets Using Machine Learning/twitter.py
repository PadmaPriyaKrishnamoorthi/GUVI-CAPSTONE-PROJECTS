# import libraries
import pickle
import streamlit as slt
from streamlit_option_menu import option_menu

#setting up streamlit page
slt.set_page_config(layout="wide")
web=option_menu(menu_title="EMOTIONS ANALYSIS",
                options=["Tweet emotion analysis🤬😊"],
                orientation="horizontal"
                )

   
   
if web=="Tweet emotion analysis🤬😊":
    #open the model for prediction
    with open('XGBOOST.pkl','rb') as files:
       model_final=pickle.load(files)
    with open('vectorizer.pkl', 'rb') as vector_file:
       vector = pickle.load(vector_file)
    tweet=slt.text_input("Enter the tweet")
    slt.image(r"C:\Users\Vishwa\Desktop\GUVI captone\twitter\2329257_bird_twitter_twitter logo_website_icon.png",width=200)
    Submit=slt.button("Predict")
    # prediction of tweet
    if Submit:
        A = vector.transform([tweet])
        prediction=model_final.predict(A)
        if prediction[0]==0:
          slt.write("NOT HATE TWEET 😊")
          slt.image(r"C:\Users\Vishwa\Desktop\GUVI captone\twitter\thumbsup.jpg")
        else:                                       
          slt.write("HATE TWEET 🤬")
          slt.image(r"C:\Users\Vishwa\Desktop\GUVI captone\twitter\thumbsdown.jpg",width=350)
    
