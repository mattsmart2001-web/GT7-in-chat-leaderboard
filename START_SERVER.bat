@echo off
REM ================================================================
REM Start Local Web Server for Leaderboard
REM ================================================================
REM This starts a local web server so the leaderboard can load data.json
REM Keep this window open while viewing the leaderboard!
REM ================================================================

title GT7 Leaderboard Server

echo ================================================================
echo Starting Leaderboard Server...
echo ================================================================
echo.

REM Try Python 3 first, then Python
python start_server.py 2>nul
if %ERRORLEVEL% NEQ 0 (
    python3 start_server.py 2>nul
)

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
)
