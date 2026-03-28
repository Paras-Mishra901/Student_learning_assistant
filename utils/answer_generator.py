from utils.chatbot import get_chatbot_response


def generate_answer(question, support_text=""):
    try:
        prompt = f"""
        Write a well-structured university-level answer.

        Question:
        {question}

        Supporting Notes:
        {support_text}

        Requirements:
        - Introduction
        - Main explanation
        - Key points
        - Conclusion (if needed)
        """
        return get_chatbot_response(prompt)

    except Exception as e:
        return f"Answer Generator Error: {str(e)}"