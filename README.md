
---

# 🎓 LearnTube — Your AI Study Companion for YouTube Lectures

> "Turn YouTube lectures into interactive learning sessions. Ask. Explore. Understand."

---

## 📘 Overview

**LearnTube** is a multimodal AI chatbot designed to help students explore and understand **educational YouTube content** more effectively. It enables users to:

* ❓ Ask natural-language questions about video content
* 🧠 Get accurate, context-aware answers and summaries
* 🌍 Translate content into multiple languages

---

## 👥 Team Members

* **Reema Alabisi**
* **Sahar Sheshah**

---

## 🎯 Objective

To develop a **smart, multimodal chatbot** that enables students to learn more effectively by interacting with YouTube lecture content. The system transforms passive video watching into an **interactive educational experience**.

### 📌 Goals

* Transform long lectures into searchable knowledge
* Use AI to simplify complex content
* Provide accurate answers and video-based summaries
* Support flexible, self-paced learning

---

## 🧠 Technologies Used

| Component             | Technology                          |
| --------------------- | ----------------------------------- |
| Speech-to-Text        | OpenAI Whisper (via Faster-Whisper) |
| NLP & LLMs            | OpenAI APIs (via LangChain)         |
| Vector Search         | Pinecone                            |
| Interface             | Streamlit                           |
| Agents & Tool Routing | LangChain Agent                     |

---

## 🏗️ Architecture Overview

1. **Input**: A YouTube playlist with AI-related educational videos
2. **Audio Pipeline**:

   * Download videos using `yt-dlp`
   * Extract and chunk audio with `pydub`
   * Transcribe with OpenAI’s Whisper
3. **Text Pipeline**:

   * Split transcript into chunks (`RecursiveCharacterTextSplitter`)
   * Generate embeddings (OpenAI) and store in FAISS vector DB
4. **Retrieval-Augmented Generation (RAG)**:

   * Use LangChain `RetrievalQA` to fetch relevant context
   * Generate grounded responses via OpenAI LLM
5. **User Interface** (Streamlit):

   * Ask questions and get answers
   * Summarize content
   * Translate responses

---

## 🔄 System Flow

1. User enters YouTube video or playlist
2. System processes audio and creates searchable chunks
3. User interacts with chatbot via text
4. LangChain Agent chooses appropriate tool:

   * Q\&A
   * Summarization
   * Translation
5. OpenAI generates the response
6. Response is returned to the user as readable text

---

## ✨ Project Presentation

[📽️ View Project Slides]()
https://drive.google.com/file/d/1NzBP9CcZDpvFGxOTViNmELQ5jE7Xj6c7/view?usp=drive_link

---
## ✨ Project Demo (streamlit)

https://drive.google.com/file/d/1NzBP9CcZDpvFGxOTViNmELQ5jE7Xj6c7/view?usp=drive_link
---
## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 3: Download Main Script

Download the `ةmain.py` and place it in your project directory.

### Step 4: Launch the Application

```bash
streamlit run LearnTubeDeploy.py
```

---

## 💡 Usage Example

**Question**: What is the difference between weak and strong AI?
**Answer**: Weak AI refers to systems designed for specific tasks without true understanding (like chatbots or recommendation engines). Strong AI would be capable of human-level cognition, reasoning, and consciousness — a concept still theoretical.

---

## 🎓 Potential Applications

* **Academic Study Companion**
* **AI Course Review Tool**
* **Accessible Learning for Non-English Speakers**

---

**Try it locally with Streamlit. Load a video. Ask. Learn. Repeat.**

---

هل تود مني أيضًا تحويل هذا إلى ملف `README.md` جاهز للنسخ أو التنزيل؟

