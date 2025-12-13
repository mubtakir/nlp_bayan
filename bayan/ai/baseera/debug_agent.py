
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

try:
    from advanced.revolutionary_intelligent_agent import RevolutionaryIntelligentAgent
    print("Import successful")
    agent = RevolutionaryIntelligentAgent()
    print(f"Agent type: {type(agent)}")
    print(f"Has process_task: {hasattr(agent, 'process_task')}")
    print(f"Has execute_task: {hasattr(agent, 'execute_task')}")
    
    if hasattr(agent, 'process_task'):
        print("Calling process_task...")
        print(agent.process_task("test"))
        
except Exception as e:
    print(f"Error: {e}")
