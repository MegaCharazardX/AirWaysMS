@echo off

:: Attempt to get Python version
python --version 2>nul

:: Check if the previous command was successful
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
) else (
    echo Python is installed.
)

pause
