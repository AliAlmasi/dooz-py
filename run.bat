@echo off
setlocal

where python >nul 2>&1
IF ERRORLEVEL 0 (
    python main.py
    
    for /d /r %%d in (__pycache__) do (
        if exist "%%d" (
            rd /s /q "%%d"
        )
    )
) ELSE (
    echo Python is not installed. Make sure to install and add it to your PATH.
    exit
)
