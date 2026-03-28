# 🎓 Student Learning Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/AI-LLM%20Powered-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Project-University%20Level-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

<p align="center">
  <b>An AI-powered educational assistant that helps students summarize notes, generate quizzes, ask academic questions, and learn smarter through an interactive Streamlit interface.</b>
</p>

---

## 📌 Project Description

**Student Learning Assistant** is an AI-powered educational web application built using **Python** and **Streamlit**.  
It is designed to make studying more efficient, interactive, and personalized for students.

This application allows users to:

- 📄 Upload study materials such as **text files or PDFs**
- 🧠 Generate **summaries** from lengthy notes
- ❓ Create **quiz questions** automatically
- 💬 Ask academic questions using an **AI chatbot**
- 📝 Generate **structured answers** for conceptual topics
- 🔑 Extract **important keywords**
- 📊 View learning activity through a **dashboard**

By integrating **Large Language Models (LLMs)** such as **Gemini** or **Hugging Face APIs**, the project provides intelligent academic assistance in a single platform.

---

## ✨ Features

- 💬 **AI Chatbot Support** – Ask academic questions and get intelligent responses
- 📄 **Text Summarization** – Convert long notes into concise summaries
- ❓ **Quiz Generation** – Automatically generate quiz questions from content
- 📝 **Answer Assistance** – Generate structured academic answers
- 📂 **File Upload & Text Extraction** – Upload and extract content from text/PDF files
- 🔑 **Keyword Extraction** – Identify important concepts from study materials
- 📊 **Interactive Dashboard** – Visualize learning activity and interactions
- 💾 **Export Functionality** – Save generated outputs or history
- 🎨 **Clean Streamlit UI** – Simple, modern, and easy-to-use interface

---

## 🛠️ Tech Stack

- **Frontend (GUI):** Streamlit
- **Backend:** Python
- **AI/LLM Integration:** Gemini API / Hugging Face API
- **Data Handling:** Pandas
- **Visualization:** Plotly
- **Environment Variables:** Python Dotenv

---

## 📥 Installation Guide

Follow these steps to set up the project locally:

### **1️⃣ Clone the Repository**
```bash
git clone <your-github-repository-link>
cd student_learning_assistant
```

### **2️⃣ Create a Virtual Environment (Recommended)**

**For Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure API Keys**
Create a `.env` file in the root directory and add:

```env
HUGGINGFACE_API_KEY=your_api_key_here
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Add only the API keys required by your implementation.

---

## ▶️ Usage Instructions

This section explains how your professor or any user can run the project locally.

### **Step 1: Open the Project Folder**
Navigate to the project directory in terminal or command prompt.

### **Step 2: Activate Virtual Environment**
Activate the virtual environment created during installation.

### **Step 3: Run the Streamlit Application**
```bash
streamlit run app.py
```

### **Step 4: Open in Browser**
After running the command, Streamlit will generate a local URL such as:

```bash
http://localhost:8501
```

Open this link in your browser.

### **Step 5: Start Using the Features**
Once the app opens, the user can:

- 📂 Upload notes, text files, or PDFs
- 📄 Generate summaries
- ❓ Create quizzes automatically
- 💬 Ask questions using the AI chatbot
- 🔑 Extract keywords
- 📝 Generate academic answers
- 📊 View dashboard insights
- 💾 Export results/history (if enabled)

> 🌐 **Important:** AI-based features require an active internet connection because the app communicates with external LLM APIs.

---

## 🏗️ System Architecture

The **Student Learning Assistant** follows a **frontend-backend architecture**:

- **Frontend:** Built using **Streamlit**, providing the GUI for user interaction
- **Backend:** Developed in **Python**, handling processing logic through modular utility files
- **LLM Layer:** Connects to **Gemini API / Hugging Face API** for intelligent response generation

### 🔄 Data Flow
**User Input (GUI)** → **Streamlit Frontend** → **Python Backend Modules** → **LLM API Processing** → **Response Generation** → **Streamlit Output**

---

## 📁 Folder Structure

```bash
student_learning_assistant/
│── app.py
│── requirements.txt
│── .env
│── README.md
│
├── utils/
│   ├── chatbot.py
│   ├── summarizer.py
│   ├── quiz_generator.py
│   ├── answer_generator.py
│   ├── file_handler.py
│   ├── keyword_extractor.py
│   ├── image_generator.py
│   ├── export_utils.py
│   └── gemini_helper.py
│
├── assets/
│   └── (optional images, icons, screenshots)
│
└── data/
    └── (optional uploaded/generated files)
```

### 📌 Folder Explanation
- **app.py** → Main Streamlit application entry point  
- **requirements.txt** → Project dependencies  
- **.env** → API keys and environment variables  
- **README.md** → Project documentation  
- **utils/** → Backend logic modules  
- **assets/** → UI images, icons, screenshots  
- **data/** → Uploaded/generated/exported files  

---

## 🚀 Future Enhancements

The project can be extended with the following improvements:

- 🔐 **User Authentication System** – Personalized login/signup
- 🗄️ **Database Integration** – Store history, quizzes, and progress
- 🎙️ **Voice Input/Output** – Speech-based interaction
- 🌍 **Multi-language Support** – Use the app in multiple languages
- 📈 **Advanced Analytics Dashboard** – Detailed learning insights
- 📄 **PDF Report Generation** – Export summaries/quizzes as PDF
- 🎯 **Study Recommendation System** – Suggest what to study next
- 🖥️ **Offline Model Integration** – Support local LLMs
- 🖼️ **Image-based Question Solving** – Solve from uploaded handwritten/printed images

---

## 🎯 Conclusion

The **Student Learning Assistant** is a practical and innovative educational project that demonstrates how **Generative AI** can enhance modern learning. By combining **Python**, **Streamlit**, and **LLM APIs**, the application delivers a smart, interactive, and user-friendly study experience.

It helps students:

- Save time ⏳
- Improve understanding 📘
- Practice actively 🧠
- Learn more effectively 🚀

This project not only showcases strong technical implementation but also highlights the real-world potential of AI in education.

---

## 📸 Optional Screenshots Section

> You can add screenshots of your project interface here for a more professional GitHub presentation.

Example:
```md
## 📸 Screenshots

### 🏠 Home Page
![Home Page](assets/homepage.png)

### 💬 Chatbot Interface
![Chatbot](assets/chatbot.png)

### 📊 Dashboard
![Dashboard](assets/dashboard.png)
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit and push
5. Open a Pull Request

---

## 📜 License

This project is created for **educational and academic purposes**.

You may use and modify it for learning, personal projects, or university demonstrations.

---

## 👨‍💻 Author

**Paras Mishra**  
🎓 University Project – Generative AI Based Student Learning Assistant

---
