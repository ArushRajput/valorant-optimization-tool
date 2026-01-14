@echo off
setlocal
title Valorant Config Reset Tool

echo ========================================================
echo       VALORANT CONFIG RESET TOOL
echo              (Fixes Stutter/Lag)
echo ========================================================
echo.

:: Define the target config directory
set "CONFIG_PATH=%LOCALAPPDATA%\VALORANT\Saved\Config"

:: Check if the directory exists
if not exist "%CONFIG_PATH%" (
    echo [ERROR] Valorant config folder not found at:
    echo %CONFIG_PATH%
    echo.
    echo Please make sure Valorant is installed and has been run at least once.
    pause
    goto :EOF
)

echo [INFO] Found config folder.
echo.
echo [WARNING] This will DELETE all local config files.
echo           You will need to re-adjust your video settings in-game.
echo.

:: Delete config files
echo [ACTION] Deleting config files...
del /Q /F /S "%CONFIG_PATH%\*" >nul 2>&1
for /d %%p in ("%CONFIG_PATH%\*") do rmdir "%%p" /s /q 2>nul

echo.
echo ========================================================
echo [SUCCESS] Valorant Config has been reset!
echo ========================================================
echo.
echo Instructions:
echo 1. Launch Valorant.
echo 2. Go to Settings - Video.
echo 3. Re-configure your graphic settings.
echo 4. Enjoy smoother gameplay!
echo.
pause
