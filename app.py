
import streamlit as st
import openai

# Load your API key securely from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="🌿 HerbIntel — AI Ingredient Explainer", page_icon="🌱")

st.title("🌿 HerbIntel — AI Ingredient Explainer")
st.markdown(
    """
    Welcome to **HerbIntel**, your AI-powered herbal supplement assistant.  
    Type the name of any herbal ingredient to get a concise explanation, including:
    - Traditional uses
    - Scientific context
    - Known safety info

    _Built with OpenAI + Streamlit for ingredient transparency & wellness tech._
    """
)

# Input
herb = st.text_input("Herb name (e.g., Ashwagandha, Turmeric):")

if herb:
    with st.spinner("Searching..."):
        try:
            prompt = (
                f"You are a certified herbalist. Give a short, accurate explanation "
                f"of {herb}, including traditional use, scientific context, and any known safety concerns. "
                f"Keep it under 150 words. Avoid making medical claims."
            )

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success("Here’s what we found:")
            st.write(response.choices[0].message["content"])

if "history" not in st.session_state:st.session_state.history = []

# Save to history
st.session_state.history.append(herb)

# Show history
st.sidebar.subheader("Recent Herbs Searched")
for past in reversed(st.session.state.history[-5:]):st.sidebar.write(past)
    
        except Exception as e:
            st.error("Something went wrong.")
            st.code(str(e))
