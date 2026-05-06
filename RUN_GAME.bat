@echo off
REM Pentis 0.8.1 - Game Launcher for Windows

echo ==================================================
echo.        PENTIS 0.8.1 BETA - Game Launcher
echo ==================================================
echo.

REM Check Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Download from: https://www.python.org/
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo %PYTHON_VERSION% found
echo.

REM Check Pygame is installed
python -c "import pygame" >nul 2>&1
if errorlevel 1 (
    echo Error: Pygame is not installed
    echo Install with: pip install pygame
    pause
    exit /b 1
)

echo Pygame is installed
echo.

REM Navigate to game directory
cd /d "%~dp0pentis" || exit /b 1

REM Run the game
echo Starting Pentis 0.8.1...
echo.

python pentis_081_local.py
pause
