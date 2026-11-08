@echo off
title Banh Canh Ga Hang Gon - Dev Server
echo ====================================================================
echo   DANG KHOI DONG LOCAL SERVER - BANH CANH GA HANG GON
echo   - Desktop: http://localhost:3333/#menu
echo   - Web App / Dien Thoai (Wi-Fi): http://192.168.1.98:3333/#menu
echo ====================================================================
echo.
python -m http.server 3333
