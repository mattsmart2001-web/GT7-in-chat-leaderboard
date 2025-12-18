@echo off
REM ===================================================================
REM YouTube Chat Leaderboard - Auto Tracker Starter
REM ===================================================================
REM This batch file starts the Python script that converts Streamerbot
REM chat data to the leaderboard format.
REM
REM Simply double-click this file to start tracking!
REM ===================================================================

echo.
echo ========================================
echo YouTube Chat Leaderboard Tracker
echo ========================================
echo.
echo Starting automatic chat tracking...
echo This window must stay open while streaming!
echo.
echo Press Ctrl+C to stop
echo.
echo ========================================
echo.

REM Run Python script in watch mode
python convert_to_leaderboard.py --watch

pause
