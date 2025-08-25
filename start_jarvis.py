#!/usr/bin/env python3

import subprocess
import sys
import time
import os

def print_banner():
    print("=" * 50)
    print("        JARVIS LOCAL AGENT SYSTEM")
    print("=" * 50)
    print()

def start_backend():
    print("[1/2] Starting Jarvis Backend Server...")
    print("Backend will run on http://localhost:5001")
    
    if sys.platform == "win32":
        backend_process = subprocess.Popen([
            "cmd", "/c", "start", "Jarvis Backend", "cmd", "/k", 
            f"cd /d {os.getcwd()} && python command_server.py"
        ], shell=True)
    else:
        backend_process = subprocess.Popen([
            sys.executable, "command_server.py"
        ], cwd=os.getcwd())
    
    print("Backend starting...")
    return backend_process

def start_dashboard():
    print("\n[2/2] Starting Jarvis Dashboard...")
    print("Dashboard launching in Electron...")
    
    if sys.platform == "win32":
        dashboard_process = subprocess.Popen([
            "cmd", "/c", "start", "Jarvis Dashboard", "cmd", "/k",
            f"cd /d {os.getcwd()} && npm run build-and-start"
        ], shell=True)
    else:
        dashboard_process = subprocess.Popen([
            "npm", "run", "build-and-start"
        ], cwd=os.getcwd())
    
    return dashboard_process

def main():
    print_banner()
    
    # Start backend
    backend = start_backend()
    time.sleep(5)  # Wait for backend to initialize
    
    # Start dashboard
    dashboard = start_dashboard()
    
    print("\n" + "=" * 50)
    print("Jarvis system is starting up...")
    print()
    print("Backend Server: http://localhost:5001")
    print("Dashboard: Electron app (launching)")
    print()
    print("Both processes running.")
    if sys.platform == "win32":
        print("Close the cmd windows to stop Jarvis.")
    else:
        print("Press Ctrl+C to stop Jarvis.")
    print("=" * 50)
    print()
    
    if sys.platform != "win32":
        try:
            backend.wait()
            dashboard.wait()
        except KeyboardInterrupt:
            print("\nShutting down Jarvis...")
            backend.terminate()
            dashboard.terminate()

if __name__ == "__main__":
    main()