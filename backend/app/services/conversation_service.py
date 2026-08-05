conversation_history = []

def add_message(role: str, content: str):
    """
    save one message.
    """

    conversation_history.append({
        "role": role,
        "content": content
    })

def get_history():
    """
    return conversation history
    """

    return conversation_history

def clear_history():
    """
    Clear conversation.
    """

    conversation_history.clear()
