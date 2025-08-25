@echo off
echo ===============================================
echo           JARVIS LOCAL AGENT SYSTEM
echo ===============================================
echo.

echo [1/2] Starting Jarvis Backend Server...
echo Backend will run on http://localhost:5001
start "Jarvis Backend" cmd /k "cd /d %~dp0 && python command_server.py"

echo.
echo Waiting for backend to initialize...
timeout /t 5 /nobreak >nul

echo [2/2] Starting Jarvis Dashboard...
echo Dashboard launching in Electron...
start "Jarvis Dashboard" cmd /k "cd /d %~dp0 && npm run build-and-start"

echo.
echo ===============================================
echo Jarvis system is starting up...
echo.
echo Backend Server: http://localhost:5001
echo Dashboard: Electron app (launching)
echo.
echo Both processes running in separate windows.
echo Close those windows to stop Jarvis.
echo ===============================================
echo.
pause