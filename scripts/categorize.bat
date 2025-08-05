@echo off
REM Navigate one level above the script location
cd /d "%~dp0\.."

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run program
python qsep_feedback_subject_classifier/main.py

REM Pause to see results (optional - remove if running in CI)
pause