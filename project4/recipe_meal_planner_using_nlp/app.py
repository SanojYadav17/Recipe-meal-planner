import streamlit as st

# Add custom styling
st.html(
    '''
    <style>
    h1{
    color:Gray;
    }

    hr {
        border-color: green;
    }
    p,li{
        color:#333;
    }
    h3,h2{
        color:#D97757;
    }
    </style>
    '''
)

# Define pages for the meal planner
Home = st.Page(
    page="Pages/welcome.py",
    title="Home",
    icon="🏠"
)

Recipe_Planner = st.Page(
    page="Pages/symp.py",
    title="Recipe Planner",
    icon="🍴"
)

Meal_History = st.Page(
    page="Pages/Recipe_Planner.py",
    title="Meal History",
    icon="📝"
)

About = st.Page(
    page="Pages/overview.py",
    title="About",
    icon="🧑‍🍳"
)

Socials = st.Page(
    page="Pages/socials.py",
    title="Socials",
    icon="🌐"
)


# Navigation for the pages
pages = st.navigation([Home, Recipe_Planner, Meal_History, About, Socials])

# Run the selected page
pages.run()
