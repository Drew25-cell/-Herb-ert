
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

if "history" not in st.session_state:
    st.session_state.history = []
    
if herb:
    # ✅ Save herb to history
    st.session_state.history.append(herb)

    try:
        # ✅ OpenAI call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert herbalist..."},
                {"role": "user", "content": f"What is {herb} used for in herbal medicine?"},
            ],
        )

        answer = response.choices[0].message["content"]

    # ✅ Show response
        st.markdown(f"### ✳️ {herb.title()}")
        st.write(answer)

# Show history
        st.sidebar.subheader("Recent Herbs Searched")
for past in reversed(st.session.state.history[-5:]):
    st.sidebar.write(past)
    
    except Exception as e:
        st.error("Something went wrong.")

