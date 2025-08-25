# JARVIS Dashboard - Basic Command Interface

## Overview
The JARVIS Dashboard is a clean Electron-based desktop application that provides a direct command interface for interacting with the JARVIS AI backend system.

## Quick Start
1. Navigate to the dashboard directory: `C:\Users\frenc\OneDrive\Desktop\dashboard`
2. Run: `npm start`
3. The dashboard window will open automatically

## Core Functions

### 🧠 Command Interface
- **Primary Function**: Text input area for sending commands to JARVIS
- **Backend Connection**: Connects to `localhost:5001/command` API endpoint
- **Response Display**: Shows AI replies in a formatted output area
- **Processing Status**: Displays "Processing..." during command execution

### 🧾 Backend Status Monitor
- **Function**: `getStatusReport()`
- **Monitored Elements**:
  - **Backend Connection**: "Connected", "Offline", or "Error"
  - **Last Checked**: Timestamp of last connectivity check

## File Structure
```
dashboard/
├── app-bundle.js             # Main React application bundle
├── index.html                # Electron window HTML
├── main.js                   # Electron main process
└── package.json              # Node.js dependencies and scripts
```

## Technical Implementation

### Frontend Architecture
- **Framework**: React 18 with Electron 27
- **Rendering**: CDN React with Babel transpilation
- **Styling**: Dark terminal theme (black/green)
- **State Management**: React useState hooks

### Backend Integration
- **API Endpoint**: POST requests to `localhost:5001/command`
- **Payload Format**: `{ "prompt": "user_input" }`
- **Response Format**: `{ "reply": "ai_response" }`
- **Error Handling**: Shows connection errors when backend unavailable

## Usage Instructions

### Starting the Dashboard
1. Navigate to dashboard directory: `cd "C:\Users\frenc\OneDrive\Desktop\dashboard"`
2. Run: `npm start`
3. Dashboard window opens automatically

### Sending Commands
1. Type command in the text area
2. Click "Execute" button
3. View response in the "🧠 Response" section
4. Monitor backend status in "🧾 System Status"

## Troubleshooting

### Backend Connection Errors
- **Error Message**: "Error: Could not reach Jarvis core."
- **Solution**: Start JARVIS backend on localhost:5001 before using dashboard
- **Check**: Ensure command_server.py is running

### Missing Dependencies
- **Run**: `npm install` in dashboard directory
- **Required**: electron, react, react-dom packages

## Ready for Module Integration
This basic dashboard provides a clean foundation for adding JARVIS modules one by one:
- Command interface tested and working
- Backend connectivity verified
- UI ready for additional panels/features
- No placeholder functionality to interfere with real modules