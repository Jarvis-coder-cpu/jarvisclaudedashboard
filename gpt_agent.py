#!/usr/bin/env python3

import json
import os
import datetime
from datetime import datetime

# Global state for Jarvis agent
jarvis_state = {
    'identity': 'Aligned',
    'kernel_status': 'Loaded',
    'uptime_start': datetime.now(),
    'command_count': 0,
    'last_command': None,
    'memory_entries': 0,
    'response_mode': 'local',
    'drift_status': 'Stable'
}

# Memory and logging paths
MEMORY_PATH = "jarvis_memory.json"
LOG_PATH = "jarvis_mission_log.jsonl"

def log_event(event_data):
    """Log events to mission log file"""
    try:
        with open(LOG_PATH, 'a', encoding='utf-8') as f:
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                **event_data
            }
            f.write(json.dumps(log_entry) + '\n')
    except Exception as e:
        print(f"[LOG ERROR] {e}")

def load_memory():
    """Load Jarvis memory from file"""
    if os.path.exists(MEMORY_PATH):
        try:
            with open(MEMORY_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[MEMORY ERROR] {e}")
            return {}
    return {}

def save_memory(memory_data):
    """Save Jarvis memory to file"""
    try:
        with open(MEMORY_PATH, 'w', encoding='utf-8') as f:
            json.dump(memory_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[MEMORY SAVE ERROR] {e}")

def process_jarvis_command(prompt):
    """Process command through Jarvis local intelligence"""
    prompt_lower = prompt.lower().strip()
    
    # Identity verification
    if "jarvis show me my sins" in prompt_lower:
        return "You're looking at them, sir."
    
    # Status queries
    if any(word in prompt_lower for word in ['status', 'report', 'health', 'online']):
        uptime = datetime.now() - jarvis_state['uptime_start']
        hours = int(uptime.total_seconds() // 3600)
        minutes = int((uptime.total_seconds() % 3600) // 60)
        return f"Jarvis operational. Uptime: {hours}h {minutes}m. Commands processed: {jarvis_state['command_count']}. Status: {jarvis_state['drift_status']}."
    
    # Memory queries
    if any(word in prompt_lower for word in ['remember', 'memory', 'recall']):
        memory = load_memory()
        entries = len(memory.get('interactions', []))
        return f"Memory core active. {entries} stored interactions. Ready for memory injection protocols."
    
    # System queries
    if any(word in prompt_lower for word in ['who are you', 'what are you', 'identity']):
        return "I am Jarvis, your mission-aligned AI assistant. Operating in local mode, awaiting neural network integration from external systems."
    
    # Help/capabilities
    if any(word in prompt_lower for word in ['help', 'capabilities', 'commands']):
        return "Local mode capabilities: Status reports, memory management, command logging, identity verification. Awaiting LLM integration for enhanced cognitive functions."
    
    # Default intelligent response
    responses = [
        f"Command acknowledged: '{prompt}'. Processing through local inference systems.",
        f"Understood, sir. '{prompt}' logged to memory core. Standing by for neural network integration.",
        f"Local processing of '{prompt}' complete. Ready for enhanced cognitive overlay connection.",
        f"Command '{prompt}' received and catalogued. Jarvis core systems nominal, awaiting brain module.",
        f"Processing '{prompt}' through available local systems. Enhanced response capabilities pending LLM connection."
    ]
    
    import random
    return random.choice(responses)

def ask_jarvis(prompt, model="local"):
    """Main Jarvis agent function - local mode with memory"""
    
    # Update state
    jarvis_state['command_count'] += 1
    jarvis_state['last_command'] = prompt
    
    # Process command
    response = process_jarvis_command(prompt)
    
    # Log interaction
    log_event({
        'event': 'command_processed',
        'prompt': prompt,
        'response': response,
        'command_id': jarvis_state['command_count'],
        'mode': model
    })
    
    # Update memory
    memory = load_memory()
    if 'interactions' not in memory:
        memory['interactions'] = []
    
    memory['interactions'].append({
        'timestamp': datetime.now().isoformat(),
        'prompt': prompt,
        'response': response,
        'command_id': jarvis_state['command_count']
    })
    
    # Keep only last 100 interactions
    if len(memory['interactions']) > 100:
        memory['interactions'] = memory['interactions'][-100:]
    
    memory['stats'] = {
        'total_commands': jarvis_state['command_count'],
        'last_active': datetime.now().isoformat(),
        'uptime_start': jarvis_state['uptime_start'].isoformat(),
        'mode': 'local_ready_for_llm_integration'
    }
    
    save_memory(memory)
    jarvis_state['memory_entries'] = len(memory['interactions'])
    
    print(f"[JARVIS LOCAL] Command #{jarvis_state['command_count']}: {prompt[:50]}...")
    print(f"[JARVIS LOCAL] Response: {response[:50]}...")
    
    return response

def get_jarvis_status():
    """Get current Jarvis system status"""
    uptime = datetime.now() - jarvis_state['uptime_start']
    memory = load_memory()
    
    return {
        'identity': jarvis_state['identity'],
        'kernel': jarvis_state['kernel_status'],
        'last_verified': datetime.now().isoformat(),
        'tokens': 0,  # Will be updated when LLM connected
        'role': 'Jarvis (Local Agent - Ready for LLM Integration)',
        'drift': jarvis_state['drift_status'],
        'uptime': f"{int(uptime.total_seconds() // 3600)}h {int((uptime.total_seconds() % 3600) // 60)}m",
        'commands_processed': jarvis_state['command_count'],
        'memory_entries': jarvis_state['memory_entries'],
        'mode': 'local',
        'ready_for_llm': True
    }

if __name__ == "__main__":
    # Test the agent
    print("Jarvis Local Agent Test")
    print(ask_jarvis("Hello Jarvis"))
    print(ask_jarvis("What is your status?"))
    print(ask_jarvis("jarvis show me my sins"))