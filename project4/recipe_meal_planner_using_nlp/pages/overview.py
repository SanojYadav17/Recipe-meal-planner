import streamlit as st

st.title("ℹ️ About the Project")
st.divider()

st.markdown("""
This project focuses on creating a **Recipe & Meal Planner Bot** designed to provide users with tailored recipe suggestions and meal planning guidance. 
Using advanced **Natural Language Processing (NLP)** techniques and **Recommendation Systems**, the bot extracts user preferences to generate personalized meal plans and recipes.

The user-friendly interface, built with **Streamlit**, ensures accessibility and ease of interaction, allowing users to describe their dietary needs, preferences, and constraints while receiving meaningful recommendations.
""")

st.subheader("🔍 Project Breakdown:")

st.subheader("📊 Dataset:")
st.markdown("""
The dataset forms the backbone of this project, containing labeled data for training:
- **Intents**: The purpose of user input, such as:
  - Requesting recipes
  - Meal planning
  - Dietary information queries
- **Entities**: Specific information extracted from input, like:
  - Ingredients (e.g., chicken, broccoli)
  - Preferences (e.g., vegan, gluten-free)
  - Contextual details (e.g., number of servings, meal type)
- **Text**: Raw user input, such as _"Give me a vegan dinner recipe"_ or _"Plan a meal for four people."_.
""")

st.subheader("💻 Streamlit Interface:")
st.markdown("""
The **Streamlit** interface enables seamless interaction between users and the AI model:
- A **text input box** for users to describe their dietary preferences or constraints.
- A **response area** where the AI provides:
  - Recipe suggestions tailored to user preferences.
  - Complete meal plans for a specified number of days or meals.
- Integrated with the trained NLP model and recommendation engine for intelligent, real-time suggestions.
""")

st.subheader("✅ Conclusion:")
st.markdown("""
This project successfully combines **NLP** and **user-focused design** to build a **Recipe & Meal Planner Bot** that understands and responds to user input. 

### Key Achievements:
- Utilized NLP and recommendation systems to interpret and process input effectively.
- Built an intuitive interface using Streamlit, making it accessible to non-technical users.
- Demonstrated the potential for future enhancements, such as:
  - Expanding the dataset with international and regional cuisines.
  - Incorporating **deep learning models** for improved personalization.
  - Adding features like grocery list generation and calorie tracking.
  - Supporting multilingual queries for broader accessibility.

This project is a step forward in leveraging AI to enhance meal planning and healthy eating habits.
""")
