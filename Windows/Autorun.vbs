Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
userHome = WinScriptHost.ExpandEnvironmentStrings("%userprofile%")
WinScriptHost.CurrentDirectory = userHome & "\AppData\Local\Autoscreener"
WinScriptHost.Run Chr(34) & "screener-startup.bat" & Chr(34), 0
Set WinScriptHost = Nothing
