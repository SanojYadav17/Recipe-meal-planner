import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    h1 {
        color: #D97757;
    }
    h2 {
        color: #6B7280;
    }
    .link {
        color: #3498db;
        text-decoration: none;
    }
    .link:hover {
        color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🍴 Recipe & Meal Planner")

# Subheading
st.subheader("Plan Your Meals and Discover New Recipes!")

# Social media links
st.markdown("""
Here are the links to my social media profiles and other platforms where I share my work:

- [GitHub](https://github.com/SanojYadav17)  
- [LinkedIn](https://linkedin.com/in/sanoj-yadav-3356aa2b7)    
- [Instagram](https://www.instagram.com/mey_sanoj27/)  

""", unsafe_allow_html=True)

# Links Section
st.subheader("🔗 Useful Resources:")
st.markdown("""
Here are some helpful links to get started with meal planning and recipe exploration:

- [Healthy Recipes](https://www.eatingwell.com/recipes/)  
- [Vegan Meal Plans](https://www.greenchef.com/eat/vegan-meal-delivery)  
- [Quick & Easy Recipes](https://www.allrecipes.com/recipes/1947/everyday-cooking/quick-and-easy/)  
""", unsafe_allow_html=True)

# Call to Action
st.markdown("""
Ready to plan your next meal? Explore delicious recipes and make meal planning effortless!  
Feel free to share your feedback and let us know what you'd like to see in future updates.
""")
