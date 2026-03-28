# 🎓 GenAI Study Assistant

## 📌 Project Overview
**GenAI Study Assistant** is a university-level **Generative AI powered educational web application** built using **Python** and **Streamlit**.  
The application is designed to help students improve productivity, learning efficiency, and academic performance by combining multiple AI-powered tools in one platform.

This project solves a real-world problem faced by students:  
> **managing study material, understanding long notes, generating quizzes, extracting important keywords, and getting AI-based academic assistance quickly.**

Instead of using multiple different tools, students can use this single smart platform for:
- Chat-based AI assistance
- Text summarization
- Quiz generation
- Answer generation
- Keyword extraction
- File text extraction
- AI image generation (if enabled)

---

## 🚀 Problem Statement
Students often struggle with:
- Large amounts of study material
- Difficulty identifying important concepts
- Lack of quick revision tools
- Time-consuming manual note preparation
- Limited access to interactive AI-based study support

### ✅ Solution
This application provides an **all-in-one AI study assistant** that can:
- Summarize lengthy content into concise notes
- Generate quiz questions for self-practice
- Produce answers for academic questions
- Extract important keywords from notes/documents
- Read uploaded files and process their text
- Offer chatbot-based educational support
- Generate images from prompts (optional feature)

This makes learning **faster, smarter, and more interactive**.

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (Frontend + App Interface)
- **Pandas**
- **Plotly** (for visualizations if used)
- **Generative AI APIs** (Gemini / Hugging Face / OpenAI, depending on your implementation)
- **Pillow (PIL)** for image handling
- **dotenv** for environment variables

---

## 📂 Project Structure
```bash
GenAI-Study-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── utils/
│   ├── chatbot.py
│   ├── summarizer.py
│   ├── quiz_generator.py
│   ├── answer_generator.py
│   ├── keyword_extractor.py
│   ├── file_handler.py
│   ├── image_generator.py
│   ├── export_utils.py
│   └── gemini_helper.py
│
└── assets/
    └── (optional images/icons)