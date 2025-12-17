[Setup]
AppName=ML Desktop App
AppVersion=1.0
DefaultDirName={pf}\MLDesktopApp
DefaultGroupName=MLDesktopApp
OutputDir=.
OutputBaseFilename=MLDesktopAppInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ML Desktop App"; Filename: "{app}\app.exe"
Name: "{commondesktop}\ML Desktop App"; Filename: "{app}\app.exe"

[Run]
Filename: "{app}\app.exe"; Description: "Lancer l'application"; Flags: nowait postinstall skipifsilent
