
import streamlit as st
import openai

# Load your API key securely from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="🌿 Herbal Ingredient Explainer")
st.title("🌿 Herbal Ingredient Explainer")
st.write("Enter the name of an herb to get a clear, concise explanation.")

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

        except Exception as e:
            st.error("Something went wrong.")
            st.code(str(e))
