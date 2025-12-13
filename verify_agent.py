#!/usr/bin/env python3
"""
Verify Agentic Self (Unified Mind)
Tests the complete integration of Phase 7.
"""
import sys
import os

# Ensure import paths
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from bayan.bayan.unified_mind import UnifiedMind

def verify():
    print("🧪 Testing Agentic Capabilities...")
    
    # Initialize the Mind
    mind = UnifiedMind()
    
    # Test 1: Simple Question (Observe -> Orient -> Decide -> Act -> Reflect)
    print("\n--- Interaction 1 ---")
    mind.interact("Is the sun hot?")
    
    # Test 2: Another Question
    print("\n--- Interaction 2 ---")
    mind.interact("Who is Ali?")
    
    # Verification is visual based on the Thinking Loop logs
    print("\n✅ Agent Verification Complete (Check logs above for OODA Loop steps).")

if __name__ == "__main__":
    verify()
