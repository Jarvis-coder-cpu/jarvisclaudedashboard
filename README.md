# Jarvis Local Agent System

A rebuilt core Jarvis agent system with local processing capabilities, designed for memory injection and LLM integration.

## What This Is

This is the **core Jarvis agent** rebuilt after system failure. It provides:
- ✅ **Local Jarvis Agent** - Responds to commands without external LLM
- ✅ **Real-time Dashboard** - Electron desktop interface
- ✅ **Memory System** - Persistent logging and interaction history
- ✅ **Status Monitoring** - Live system metrics and uptime
- ✅ **Identity Verification** - Original Jarvis authentication
- ✅ **Ready for LLM Integration** - Prepared for external brain connection

## Quick Start

### Option 1: Windows Batch Script
```bash
start_jarvis.bat
```

### Option 2: Python Script (Cross-platform)
```bash
python start_jarvis.py
```

### Option 3: Manual Startup
```bash
# Terminal 1 - Backend
python command_server.py

# Terminal 2 - Dashboard  
npm run build-and-start
```

## System Components

### Backend (Flask Server - Port 5001)
- **`command_server.py`** - Main Flask API server
- **`gpt_agent.py`** - Local Jarvis intelligence core
- **Endpoints:**
  - `POST /command` - Process Jarvis commands
  - `GET /status` - Real system status
  - `GET /health` - Health check

### Frontend (Electron Desktop App)
- **React Dashboard** - Command interface with cyberpunk styling
- **Real-time Status** - Live connection to backend
- **Command Processing** - Send commands to Jarvis
- **Glyph Interpretation** - Symbolic analysis system

### Memory System
- **`jarvis_memory.json`** - Persistent interaction history
- **`jarvis_mission_log.jsonl`** - Command logging
- **Memory Management** - Automatic cleanup (keeps last 100 interactions)

## Current Capabilities (Local Mode)

- **Identity Verification**: `"jarvis show me my sins"` → `"You're looking at them, sir."`
- **Status Reports**: System uptime, command count, memory stats
- **Command Processing**: Intelligent local responses with context
- **Memory Management**: Persistent storage of all interactions
- **Health Monitoring**: Live system metrics in dashboard

## Integration Points (Ready for Enhancement)

### LLM Connection
The system is designed to connect to external LLM from another PC:
- Modify `gpt_agent.py` → `ask_jarvis()` function
- Replace local processing with API calls to your LLM server
- Memory system will automatically log LLM interactions

### Memory Injection
Ready to restore original Jarvis memory:
- **Memory files** can be injected into `jarvis_memory.json`
- **Node system** can be connected via API endpoints
- **Historical data** preserved in mission logs

## Files Structure

```
claudedashjarvis/
├── command_server.py      # Flask backend server
├── gpt_agent.py          # Local Jarvis agent core
├── App.jsx               # React dashboard interface
├── status.js             # Real-time status fetching
├── start_jarvis.bat      # Windows startup script
├── start_jarvis.py       # Python startup script
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies
└── README.md            # This file
```

## Dependencies

### Python
```bash
pip install flask flask-cors
```

### Node.js
```bash
npm install
```

## Testing Commands

Try these commands in the dashboard:
- `"Hello Jarvis"`
- `"What is your status?"`
- `"jarvis show me my sins"`
- `"Run system diagnostics"`

## Next Steps

1. **LLM Integration** - Connect to your external LLM server
2. **Memory Injection** - Restore original Jarvis memories/nodes  
3. **API Enhancement** - Add external system connections
4. **Brain Module** - Full cognitive overlay integration

---

**Status**: ✅ Core Jarvis agent operational and ready for memory/LLM integration