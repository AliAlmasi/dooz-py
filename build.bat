@echo off
setlocal

echo.
echo ==================================
echo     Dooz Game EXE Build Script
echo ==================================
echo.

echo Checking for PyInstaller...

REM Check if PyInstaller exists, install if missing
pyinstaller --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo PyInstaller not found. Installing...
    pip install -U pyinstaller
)

echo.

echo Removing previous builds...

REM Removing previous builds
IF EXIST build rd /s /q build

echo.

echo Building the EXE file using PyInstaller...

REM Build EXE
pyinstaller ^
  --onefile ^
  --windowed ^
  --icon=ui\icon.ico ^
  --collect-submodules ui ^
  --collect-submodules game ^
  --add-data "ui\icon.ico;ui" ^
  --add-data "ui\fonts\vazirmatn.ttf;ui\fonts" ^
  main.py >nul 2>&1

echo.

echo Cleaning up...

REM Cleanup
IF EXIST build rd /s /q build
IF EXIST main.spec del /f /q main.spec

for /d /r %%d in (__pycache__) do (
    if exist "%%d" (
        rd /s /q "%%d"
    )
)

echo.

echo.
echo Build finished. EXE file in dist folder.
