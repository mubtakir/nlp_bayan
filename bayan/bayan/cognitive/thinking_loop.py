import time
from enum import Enum, auto

class AgentState(Enum):
    IDLE = auto()
    OBSERVING = auto()
    PROCESSING = auto()
    ACTING = auto()
    REFLECTING = auto()

class ThinkingLoop:
    """
    Implements the OODA Loop (Observe-Orient-Decide-Act).
    This gives the AI a 'Heartbeat' of consciousness.
    """
    def __init__(self, unified_mind, interval=1.0):
        self.mind = unified_mind
        self.state = AgentState.IDLE
        self.interval = interval
        self.memory = []

    def cycle(self):
        """One cycle of thought."""
        if self.state == AgentState.IDLE:
            self.observe()
        elif self.state == AgentState.OBSERVING:
            self.orient()
        elif self.state == AgentState.PROCESSING:
            self.decide()
        elif self.state == AgentState.ACTING:
            self.act()
        elif self.state == AgentState.REFLECTING:
            self.reflect()

    def observe(self):
        """Check for inputs."""
        # For CLI/API, input is event-driven, but we can check internal signals
        # print("👁️  Observing...") 
        # In a real agent, this checks event queues
        self.state = AgentState.IDLE # Stay idle unless triggered

    def trigger_thought(self, input_data):
        """External trigger to start the loop."""
        print(f"👂 Event: Received input '{input_data}'")
        self.memory.append({"type": "input", "data": input_data})
        self.state = AgentState.OBSERVING
        self.cycle()

    def orient(self):
        """Analyze the input context."""
        print("🧠 Orienting: Analyzing context...")
        last_input = self.memory[-1]['data']
        # Simple analysis
        context = {"intent": "query" if "?" in last_input else "statement"}
        self.memory[-1]['context'] = context
        self.state = AgentState.PROCESSING
        self.cycle()

    def decide(self):
        """Determine action."""
        print("⚖️  Deciding: Choosing best action...")
        context = self.memory[-1]['context']
        if context['intent'] == 'query':
            self.memory[-1]['action'] = 'answer_query'
        else:
            self.memory[-1]['action'] = 'acknowledge'
        self.state = AgentState.ACTING
        self.cycle()

    def act(self):
        """Execute action."""
        action = self.memory[-1]['action']
        inp = self.memory[-1]['data']
        print(f"🎬 Acting: {action}")
        
        # Unified Action: Use the Cognitive Bridge for both Queries and Statements
        response = self.mind.bridge.ask(inp)
            
        print(f"🗣️  Output: {response}")
        self.memory[-1]['response'] = response
        self.state = AgentState.REFLECTING
        self.cycle()

    def reflect(self):
        """Self-Correction / Learning."""
        print("🪞 Reflecting: Did I do well?")
        
        last_input = self.memory[-1]['data']
        last_response = self.memory[-1]['response']
        
        # Logic Police Check on the INPUT (Thought)
        # We verify if we should have accepted that thought
        verdict = self.mind.police.check_thought(last_input)
        
        if verdict != "SAFE":
            print(f"🚨 CONSCIENCE ALERT: {verdict}")
            # Corrective Action
            if "learned" in last_response:
                print("❌ Self-Correction: I should not have learned that.")
                # Ideally, remove the fact. For now, just emphasize the error.
        else:
            print("✅ Conscience Clear.")
            
        self.state = AgentState.IDLE
