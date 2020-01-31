; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "FinalCif"
#define MyAppVersion "44"
#define MyAppPublisher "Daniel Kratzert"

; Remember, first run pyInstaller script!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{3B40F796-CFCE-4C05-9587-2EACA3C1AACC}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={pf}\{#MyAppName}
OutputBaseFilename={#MyAppName}-setup-x64-v{#MyAppVersion}
Compression=lzma2/fast
SolidCompression=yes
SetupLogging=True
CloseApplications=False
RestartApplications=False
ShowLanguageDialog=no
ChangesAssociations=True
RestartIfNeededByRun=False
ChangesEnvironment=True
DisableFinishedPage=True
DisableReadyPage=True
DisableReadyMemo=True
DisableWelcomePage=True
AlwaysShowDirOnReadyPage=True
InternalCompressLevel=fast
EnableDirDoesntExistWarning=True
DirExistsWarning=no
UninstallLogMode=new
VersionInfoVersion={#MyAppVersion}
MinVersion=0,6.1
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
AppendDefaultGroupName=True
AppContact=dkratzert@gmx.de
AppCopyright=Daniel Kratzert
AppSupportPhone=+49 761 203 6156
VersionInfoProductName={#MyAppName}
AlwaysShowComponentsList=False
ShowComponentSizes=False
SetupIconFile="..\icon\finalcif2.ico"
SignTool=signtool
ArchitecturesInstallIn64BitMode=x64

[UninstallRun]


[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

; adds a new page to the setup where you can choose if the path should be added
;Excludes: "*.pyc"

[Run]

[Icons]
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"; IconFilename: "{app}\icon\finalcif2.ico"
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppName}.exe"; WorkingDir: "{app}"; IconFilename: "{app}\icon\finalcif2.ico"; Check: IsWin64

[UninstallDelete]
Type: files; Name: "{app}\*.pyc"
Type: files; Name: "{app}\*.*"
Type: filesandordirs; Name: "{app}\*"

[InstallDelete]

[Tasks]

[Files]
Source: "..\dist\{#MyAppName}\*"; DestDir: "{app}"; Flags: ignoreversion createallsubdirs recursesubdirs

[Dirs]
Name: "{app}\displaymol"; Permissions: everyone-full
Name: "{app}\gui"; Permissions: everyone-full

[Code]


