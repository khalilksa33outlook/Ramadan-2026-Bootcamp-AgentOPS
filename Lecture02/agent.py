# agent.py
from mock_llm import mock_llm
from tools import get_weather, calculator

def run_agent(user_query):
    # 1. Initialize State
    history = [f"User: {user_query}"]
    step_count = 0
    max_steps = 5  # SAFETY LIMIT (Circuit Breaker)

    print(f"🏁 GOAL: {user_query}\n")

    while step_count < max_steps:
        step_count += 1
        print(f"--- Step {step_count} ---")

        # 2. REASON: Call the 'LLM' to allow it to think
        response = mock_llm(history)
        
        print(f"💭 THOUGHT: {response['thought']}")

        # 3. CHECK: Are we done?
        if response['final_answer']:
            print(f"✅ FINAL ANSWER: {response['final_answer']}")
            return

        # 4. ACT: Execute the selected tool
        tool_name = response['tool']
        tool_arg = response['tool_input']
        
        observation = "Error: Tool not found"
        
        print(f"🛠️ ACTION: Calling {tool_name}('{tool_arg}')")

        if tool_name == "get_weather":
            observation = get_weather(tool_arg)
        elif tool_name == "calculator":
            observation = calculator(tool_arg)

        print(f"👀 OBSERVATION: {observation}")

        # 5. UPDATE STATE: Append result to history so LLM knows what happened
        history.append(f"Observation: {observation}")
        print(" ") # formatting

    print("❌ Failed to reach goal within step limit.")

# --- Run It ---
if __name__ == "__main__":
    run_agent("What is the weather in Dubai?")