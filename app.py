import streamlit as st


# Define pages for the meal planner
Home = st.Page(
    page="pages/welcome.py",
    title="Home",
    icon="🏠"
)
Recipe_Planner = st.Page(
    page="pages/symp.py",
    title="Recipe Planner",
    icon="🍴"
)
Meal_History = st.Page(
    page="pages/Recipe_Planner.py",
    title="Meal History",
    icon="📝"
)
About = st.Page(
    page="pages/overview.py",
    title="About",
    icon="🧑‍🍳"
)
Socials = st.Page(
    page="pages/socials.py",
    title="Socials",
    icon="🌐"
)
# Navigation for the pages
pages = st.navigation([Home, Recipe_Planner, Meal_History, About, Socials])

# Run the selected page
pages.run()
