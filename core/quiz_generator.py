from core.chatbot import get_chatbot_response


def generate_quiz(text):
    try:
        prompt = f"""
        Create a university-level quiz from the following topic/text.

        Requirements:
        - 5 to 10 questions
        - Include MCQs + short answer if possible
        - Exam practice style
        - Clean formatting

        Topic/Text:
        {text}
        """
        return get_chatbot_response(prompt)

    except Exception as e:
        return f"Quiz Generator Error: {str(e)}"