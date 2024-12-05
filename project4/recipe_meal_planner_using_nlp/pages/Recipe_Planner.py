import os
import streamlit as st
import csv
import json
import pandas as pd

# Header for the Recipe & Meal Planner page
st.header("Recipe & Meal Planner - Conversation History")

# Check if the CSV file exists
if os.path.exists('chat_history.csv'):
    st.subheader("CSV Conversation History")
    with open('chat_history.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if len(row) >= 3:  # Ensure there are at least 3 elements in the row
                st.text(f"User: {row[0]}")
                st.text(f"Planner: {row[1]}")
                st.text(f"Timestamp: {row[2]}")
                st.markdown("---")
            else:
                st.warning("Row does not have enough data in CSV.")

else:
    st.warning("No CSV conversation history found.")

# Check if the JSON file exists
if os.path.exists('chat_history.json'):
    st.subheader("JSON Conversation History")
    with open('chat_history.json', 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        for entry in data:
            st.text(f"User: {entry['user']}")
            st.text(f"Planner: {entry['planner']}")
            st.text(f"Timestamp: {entry['timestamp']}")
            st.markdown("---")
else:
    st.warning("No JSON conversation history found.")

# Loading meal planner data from a CSV (if it exists)
st.subheader("Meal Planner History")
if os.path.exists('meal_planner.csv'):
    df = pd.read_csv('meal_planner.csv')
    for index, row in df.iterrows():
        if len(row) >= 3:  # Ensure there are at least 3 elements in the row
            st.text(f"Timestamp: {row[2]}")
            st.text(f"Meal: {row[0]}")
            st.text(f"Recipe: {row[1]}")
            st.markdown("---")
        else:
            st.warning("Row does not have enough data in Meal Planner CSV.")
else:
    st.warning("No meal planner data found.")
