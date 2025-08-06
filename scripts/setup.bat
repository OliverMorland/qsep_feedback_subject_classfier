@echo off
echo Setting up QSEP Feedback Subject Classifier...

REM Navigate to project root from scripts folder
cd ..

REM Check if virtual environment already exists
if exist "venv" (
    echo Virtual environment already exists.
) else (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat

REM Upgrade pip first
python -m pip install --upgrade pip

REM Install the project and its dependencies
python -m pip install -e .

REM Install development dependencies
python -m pip install -e .[dev]

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo Setup completed successfully!
echo Virtual environment is ready at: %cd%\venv
echo To activate it manually, run: venv\Scripts\activate.bat
pause