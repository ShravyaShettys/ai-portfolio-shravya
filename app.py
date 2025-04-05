
# ✅ Load Gemini API Key from local secrets.toml file
import streamlit as st
import google.generativeai as genai

# ✅ Load Gemini API key from Streamlit Cloud secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# ✅ Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# 💬 Function to interact with Gemini
def get_response(user_input):
    prompt = f"""
You are an AI version of Shravya S Shetty, an AI and Data Science graduate with experience in ML, NLP, and Deep Learning. 
Respond in a friendly tone using bullet points or short paragraphs when appropriate.

Here’s your background:
📍 AI/ML Intern at Codelab Systems: Built ML models, automated pipelines, fraud detection system (92% accuracy)
📍 Intern at Adani Power: Spam filter (95% accuracy), Twitter sentiment analysis (10k+ tweets)
📍 Goldman Sachs Mentorship: Solved 100+ DSA problems, improved AI computation by 30%

📂 Projects:
- Health & Mental Wellness Platform (disease prediction: 90% accuracy)
- AI Resume Analyzer (95% accuracy)
- AI Voice-Based Recommendation System (real-time voice + Gemini API)
- Wellness Whisper App (AI-driven health insights)

🧠 Skills:
Python, SQL, HTML/CSS, TensorFlow, PyTorch, Scikit-learn, spaCy, Hugging Face, Gemini API, Git/GitHub, Statistical Analysis

🎓 B.E. in AI & Data Science (SMVITM), CGPA: 8.6

User asked: \"{user_input}\"
"""
    response = model.generate_content(prompt)
    return response.text

# 🌟 Streamlit UI
st.set_page_config(page_title="AI Portfolio - Shravya S Shetty", page_icon="🚀")
st.title("🚀 AI Chatbot: Ask Me Anything!")

st.markdown(
    """
    **Hi! I'm an AI version of _Shravya S Shetty_** 🤖✨  
    - 🧠 AI & Data Science Enthusiast  
    - 🔍 Explore my **projects**, **internships**, and **skills**  
    - 💬 Ask me anything about **my work, experience or journey**

    ---
    """
)

# 🚀 Input area
user_input = st.text_input("Ask me anything about Shravya!", placeholder="e.g. Tell me about your wellness app")

if st.button("Ask 🚀"):
    if user_input:
        with st.spinner("Thinking..."):
            response = get_response(user_input)
            st.success("Here's what I found:")
            st.markdown(response)
    else:
        st.warning("Please enter a question!")

# 🔗 Footer with links
st.markdown("---")
st.markdown("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/shravya-s-shetty-333427263)")
st.markdown("📁 [View GitHub Projects](https://github.com/ShravyaShettys)")
