# Generative AI Study Assistant

## Problem Definition
Students often face difficulty in managing large amounts of study material, understanding lengthy notes, and preparing effectively for exams. Manually creating summaries, identifying important concepts, and generating practice questions can be time-consuming and inefficient.

This project solves this problem by providing an AI-powered study assistant that helps students interact with their learning material more effectively. The application can summarize notes, answer academic questions, generate quizzes, extract keywords, and provide intelligent study support through a simple web interface.

---

## System Architecture
The project follows a frontend-backend architecture.

- The **frontend** is built using **Streamlit**, which provides the graphical user interface (GUI) where users can upload files, enter questions, and access different learning features.
- The **backend** is developed in **Python** and handles the application logic using modular utility files.
- When the user performs an action (such as uploading notes, generating a summary, or asking a question), the frontend sends the input to the backend.
- The backend processes the request and communicates with the **Large Language Model (LLM)** through **Gemini API or Hugging Face API**.
- The LLM generates the required output, such as summaries, quiz questions, or answers.
- The processed result is then returned to the frontend and displayed to the user.

### Data Flow
User Input (GUI) -> Streamlit Frontend -> Python Backend -> LLM API -> Generated Response -> Streamlit Output

---

## Usage Instructions

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone <your-github-repository-link>
cd student_learning_assistant
```

### 2. Create and activate a virtual environment

**For Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**For macOS/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the required dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file for API keys
Add the required API key(s) in the root directory:

```env
HUGGINGFACE_API_KEY=your_api_key_here
GEMINI_API_KEY=your_api_key_here
```

> Note: Keep only the API key(s) that your project actually uses.

### 5. Run the Streamlit application
```bash
streamlit run app.py
```

### 6. Open the application in the browser
After running the command, Streamlit will generate a local URL such as:

```bash
http://localhost:8501
```

Open this link in your browser to use the project.

### 7. Use the application features
The professor can then:
- Upload study materials (text or PDF files)
- Generate summaries
- Create quizzes
- Ask questions using the chatbot
- Extract keywords
- Generate answers for study topics


> Important: An internet connection is required because the application communicates with external AI APIs.
