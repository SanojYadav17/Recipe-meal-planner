import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Streamlit app title and setup
st.title("🍴 Recipe & Meal Planner")
st.divider()

# Configure SSL and NLTK
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load recipes from the JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'recipes.json')

if not os.path.exists(file_path):
    st.error(f"recipes.json not found. Please place the file in: {file_path}")
    st.stop()

try:
    with open(file_path, "r") as file:
        recipes = json.load(file)
except json.JSONDecodeError:
    st.error("Invalid JSON format in recipes.json. Please check the file structure.")
    st.stop()
except Exception as e:
    st.error(f"Error loading recipes.json: {e}")
    st.stop()

# Prepare data for training
tags = []
patterns = []
for intent in recipes:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)

# Train the model
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
x = vectorizer.fit_transform(patterns)
y = tags
clf = LogisticRegression(random_state=0, max_iter=10000)
clf.fit(x, y)

# Recipe recommender function
def recommend_recipe(input_text):
    input_vector = vectorizer.transform([input_text])
    tag = clf.predict(input_vector)[0]
    for intent in recipes:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "I'm sorry, I couldn't find a recipe matching your input. Please try again!"

# Chat history file setup
chat_history_file = 'meal_plan_history.csv'
if not os.path.exists(chat_history_file):
    with open(chat_history_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['User Input', 'Suggested Recipe', 'Timestamp'])

# Chat interface
st.subheader("**🥗 Isanoj Here!!**")
st.write("Tell me the ingredients you have or the type of meal you want, and I'll suggest a recipe for you!")

# Chat input
user_input = st.text_input("You:", key="user_input")

if user_input:
    response = recommend_recipe(user_input)
    st.text_area("Isanoj_:", value=response, height=120, max_chars=None, key="recipe_response")

    # Save chat history
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(chat_history_file, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([user_input, response, timestamp])

    # Thank the user
    if response.lower() in ["thank you", "thanks"]:
        st.write("You're welcome! Enjoy your meal planning!")
