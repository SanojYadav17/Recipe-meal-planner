import streamlit as st

# st.title("🍲 Isanoj Recipe Meal Planner AI Chatbot")

# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## Welcome to Your Personal Recipe Meal Planner!
    
    _Isanoj_ AI_ is here to assist you with:
    - Discovering new meal ideas
    - Offering recipe suggestions based on your preferences
    - Providing step-by-step cooking instructions
    
    ### How to Use
    1. Enter your meal preferences or ingredients in the chat box below.
    2. Get personalized recipe suggestions based on your input.
    3. Explore new cuisines and meal ideas to try!
    
    **Note:** 
    - All recipes are based on general ingredients and cooking methods.
    - Always adjust recipes based on your dietary needs and preferences.
    """)
    
with col2:
        # Optional: Add a food-related image or icon
        st.image("https://cdn-icons-png.freepik.com/256/562/562678.png?semt=ais_hybrid", width=250)
    
# Chat input
st.link_button("Start Planning Meals", "https://recipe-planner-v1.streamlit.app/meal", icon="💬", type="primary", help="At your own convenience")
