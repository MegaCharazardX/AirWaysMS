@echo off

:: Attempt to find Python installation path
for /f "delims=" %%P in ('where python') do set PYTHON_PATH=%%P

:: Check if the Python path points to WindowsApps (Microsoft Store alias)
echo Python path found at: %PYTHON_PATH%
echo.
if "%PYTHON_PATH%" == "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" (
    echo Detected Microsoft Store alias. Proceeding with Python 3.12.2 installation...
    set PYTHON_PATH=
)

if not defined PYTHON_PATH (
    echo Python not found. Installing Python 3.12.2...

    :: Download Python installer
    curl -O https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe

    :: Install Python silently and add to PATH
    python-3.12.2-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

    :: Check again for the Python path
    for /f "delims=" %%P in ('where python') do set PYTHON_PATH=%%P
    if not defined PYTHON_PATH (
        echo Python installation failed. Please check the installer or network connection.
        goto :end
    )
)

echo Using Python found at: %PYTHON_PATH%
echo Running your Python script...

:: Run your script using the Python path
%PYTHON_PATH% py_files\index.py   :: Adjust relative path as needed

:end
pause
