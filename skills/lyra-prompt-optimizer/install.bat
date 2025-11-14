@echo off
REM Lyra Prompt Optimizer Installation Script for Windows
REM This script installs the lyra-prompt-optimizer skill for Claude Code

echo ==================================
echo Lyra Prompt Optimizer Installer
echo ==================================
echo.

set SKILLS_DIR=%USERPROFILE%\.claude\skills
set SKILL_NAME=lyra-prompt-optimizer
set INSTALL_PATH=%SKILLS_DIR%\%SKILL_NAME%

echo Target installation directory:
echo %INSTALL_PATH%
echo.

REM Create skills directory if it doesn't exist
if not exist "%SKILLS_DIR%" (
    echo Creating Claude skills directory...
    mkdir "%SKILLS_DIR%"
)

REM Check if skill already exists
if exist "%INSTALL_PATH%" (
    echo WARNING: Skill already exists at %INSTALL_PATH%
    set /p OVERWRITE="Do you want to overwrite it? (Y/N): "
    if /i not "%OVERWRITE%"=="Y" (
        echo Installation cancelled.
        exit /b 0
    )
    echo Removing existing installation...
    rmdir /s /q "%INSTALL_PATH%"
)

REM Copy skill files
echo Installing skill files...
mkdir "%INSTALL_PATH%"
xcopy /E /I /Y "%~dp0*" "%INSTALL_PATH%"

REM Remove installation scripts from the installation
del /q "%INSTALL_PATH%\install.sh" 2>nul
del /q "%INSTALL_PATH%\install.bat" 2>nul

echo.
echo Installation complete!
echo.
echo Skill installed to: %INSTALL_PATH%
echo.
echo Verification:
echo -------------
if exist "%INSTALL_PATH%\SKILL.md" (
    echo [OK] SKILL.md found
) else (
    echo [ERROR] SKILL.md not found
)

if exist "%INSTALL_PATH%\README.md" (
    echo [OK] README.md found
) else (
    echo [ERROR] README.md not found
)

if exist "%INSTALL_PATH%\examples" (
    echo [OK] examples\ directory found
) else (
    echo [ERROR] examples\ directory not found
)

if exist "%INSTALL_PATH%\templates" (
    echo [OK] templates\ directory found
) else (
    echo [ERROR] templates\ directory not found
)

echo.
echo Next steps:
echo 1. Restart Claude Code if it's currently running
echo 2. The skill will be automatically available for use
echo 3. Try: claude "Optimize this prompt: Help me write a background check SOP"
echo.
echo For more information, see the README.md file.
echo.
echo Quick Start:
echo    - View examples: %INSTALL_PATH%\examples\
echo    - View templates: %INSTALL_PATH%\templates\
echo    - Read docs: %INSTALL_PATH%\README.md
echo.

pause
