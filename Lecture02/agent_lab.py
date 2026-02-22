# agent_lab.py
# main entry point
#!/usr/bin/env python3
"""
Lab 2: ReAct Loop - Entry Point
Run this file to execute the agent simulation.
"""

from agent import run_agent

def main():
    # 🎯 Define the user's goal
    goal = "What is the weather in Dubai?"
    
    # 🚀 Run the agent
    print(f"\n🏁 GOAL: {goal}\n")
    run_agent(goal)

if __name__ == "__main__":
    main()