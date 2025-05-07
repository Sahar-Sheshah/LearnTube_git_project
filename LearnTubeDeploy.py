import streamlit as st
from langchain.agents import initialize_agent
from langchain_core.tools import Tool
from langchain_openai import OpenAI
from LearnTubeAgent import answer_question_tool, summarize_tool, translation_tool

# LLM Configuration
llm = OpenAI(temperature=0.2, max_tokens=150)

# Define tools
tools = [
    Tool(name="AnswerQuestion", func=answer_question_tool, description="Answer a general question based on context."),
    Tool(name="SummarizeVideo", func=summarize_tool, description="Summarize a video transcript."),
    Tool(name="SmartTranslator", func=translation_tool, description="Translate text into the language specified in a natural instruction, e.g., 'Translate this to Italian'.")
]

# Initialize the agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #291e50;
    }
    .sidebar .sidebar-content {
        background-color: #2e3a59;
    }
    .stTextArea textarea {
        background-color: #fafafa;
        border-radius: 8px;
        color: #003366;
        font-weight: bold;
        caret-color: red; /* لون مؤشر الكتابة */
        cursor: text;     /* شكل المؤشر عند المرور */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add logo image
st.image('learntubeLogo.jpg', use_container_width=True)

# Interactive introduction
st.markdown("""
    ### 🤖 **LearnTube AI Assistant**
    🧑‍🏫 Ask me anything related to your videos, and I'll help you learn more!
    - 📄 **Summarize** videos  
    - 🌍 **Translate** text  
    - ❓ **Answer** your questions based on video content
""")

# Input interface
user_input = st.text_area("Enter your question or command:", height=150)

# Initialize session state
if "response" not in st.session_state:
    st.session_state.response = ""
if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = False

# LearnTubeDeploy.py

if st.button("🔍 Get Response"):
    if user_input.strip() != "":
        with st.spinner('AI is thinking...'):
            # Call the tool directly instead of agent.run()
            st.session_state.response = answer_question_tool(user_input)
            st.session_state.feedback_given = False
            st.success('Done!')
    else:
        st.warning("Please enter a question or command before clicking the button.")

# Show response
if st.session_state.response:
    st.text_area("Response:", st.session_state.response, height=200)

    # Friendly feedback buttons
    if not st.session_state.feedback_given:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍 That was helpful"):
                st.success("We're glad it helped! 😊")
                st.session_state.feedback_given = True
        with col2:
            if st.button("🤔 Could be improved"):
                st.info("Thanks! We'll keep getting better. 🚀")
                st.session_state.feedback_given = True
