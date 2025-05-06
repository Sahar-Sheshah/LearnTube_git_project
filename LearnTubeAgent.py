#Agent
from langchain.agents import Tool, initialize_agent
from langchain_openai import OpenAI
from langchain.schema import Document
from main import cached_similarity_search, vectorstore, CFG   

# Initialize OpenAI model with specific settings (temperature controls creativity)
llm = OpenAI(temperature=0.2, max_tokens=150)

#Tool - Answer Questions Based on Context
# LearnTubeAgent.py

def answer_question_tool(query: str) -> str:
    try:
        docs_content = cached_similarity_search(query)
        if not docs_content or all(len(content.strip()) == 0 for content in docs_content):
            return "There is no information about that in the videos."

        context = "\n\n".join(docs_content)
        prompt = (
            "Answer the question using only the context below. "
            'If not found, reply: "There is no information about that in the videos."\n\n'
            f"Question: {query}\n\nContext:\n{context}"
            "\n\nAnswer:"
        )

        result = llm.invoke(prompt).strip()

        if not result:
            return "There is no information about that in the videos."
        return result

    except Exception as e:
        return f"An error occurred while answering the question: {e}"

#Tool - Summarization

from langchain.chains.summarize import load_summarize_chain

def summarize_tool(docs_input) -> str:
    try:
        # Convert raw strings to Document objects if necessary
        if docs_input and isinstance(docs_input[0], str):
            docs = [Document(page_content=d) for d in docs_input]
        else:
            docs = docs_input

        # Check if there are documents to summarize
        if not docs:
            return "No documents provided for summarization."

        # Load the summarization chain (map-reduce approach)
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(docs)
        return summary.strip()

    except Exception as e:
        return f"An error occurred while summarizing: {e}"


 #Smart Translation Tool (Auto Language Detection)

def translation_tool(input_text: str) -> str:
    """
    Automatically detects the target language from the input and translates the given text accordingly.
    For example, if the input is: 'Translate to French: Hello, how are you?', it will return the French translation.
    """
    try:
        # Prompt that instructs the LLM to detect the target language and translate accordingly
        prompt = f"""
You are a smart translator. Detect the target language and translate the given text.
If the user mentions the target language, use it. Otherwise, choose the most relevant language based on the context.

Text to translate:
{input_text}
""".strip()

        result = llm.invoke(prompt)
        return result.strip()

    except Exception as e:
        return f"An error occurred while translating: {e}"


#Register Tools and Initialize Agent

# Register tools for the agent
tools = [
    Tool(name="AnswerQuestion", func=answer_question_tool, description="Answer a general question based on context."),
    Tool(name="SummarizeVideo", func=summarize_tool, description="Summarize a video transcript."),
    Tool(name="SmartTranslator", func=translation_tool, description="Translate text into the language specified in a natural instruction, e.g., 'Translate this to Italian'.")
]

# Initialize LangChain agent with the tools and language model
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
