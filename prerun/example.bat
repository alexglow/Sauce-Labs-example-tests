@ECHO OFF
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v MigrateProxy /t REG_DWORD /d 1 /f
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f

@ECHO OFF
echo ^<!doctype html^>^<html lang=en^>^<meta charset=utf-8^>^<title^>List of Program Files^</title^>^<pre^> > C:\Users\chef\Downloads\list_of_program_files.html
dir "C:\Program Files" >> C:\Users\chef\Downloads\list_of_program_files.html