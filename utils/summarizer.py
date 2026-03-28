from utils.chatbot import get_chatbot_response


def summarize_text(text):
    try:
        prompt = f"""
        Summarize the following academic content clearly and concisely.
        Keep only important study points.

        Text:
        {text}
        """
        return get_chatbot_response(prompt)

    except Exception as e:
        return f"Summarizer Error: {str(e)}"