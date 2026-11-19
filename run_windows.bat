@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo NVIDIA AI Agent
if "%NVIDIA_API_KEY%"=="" (
 echo [ERROR] NVIDIA_API_KEY is not set.
 echo Run: set NVIDIA_API_KEY=your_key
 pause
 exit /b 1
)
python harness.py
pause
