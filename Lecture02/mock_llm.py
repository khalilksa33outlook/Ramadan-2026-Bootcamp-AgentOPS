# mock_llm.py

def mock_llm(history):
    """
    Simulates an LLM's decision making process based on the current context.
    It returns a JSON-like dictionary.
    """
    history_str = str(history).lower()

    # SCENARIO: User asks "What is the weather in Dubai?"
    if "weather in dubai" in history_str and "rainy" not in history_str and "sunny" not in history_str:
        return {
            "thought": "The user wants Dubai weather. I should use the weather tool.",
            "tool": "get_weather",
            "tool_input": "Dubai",
            "final_answer": None
        }
    
    # SCENARIO: We have tool output (observation), so we can answer.
    elif "sunny, 40°c" in history_str:
         return {
            "thought": "I have the weather data. I can answer the user.",
            "tool": None,
            "tool_input": None,
            "final_answer": "The weather in Dubai is Sunny and 40°C."
        }

    # FALLBACK
    return {
        "thought": "I don't know what to do.",
        "tool": None,
        "tool_input": None,
        "final_answer": "I am confused."
    }