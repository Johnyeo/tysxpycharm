;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("��", "","Edit1")

; Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)

; The work directory current exe
dim $path = @WorkingDir & "\Bicyle.xlsx"

; Set the File name text on the Edit field
ControlSetText("��", "", "Edit1", $path)

Sleep(2000)

; Click on the Open button
ControlClick("��", "","Button1");