Attribute VB_Name = "Module1"
Sub GetACM(ACMFile As String, ACMFlo As Object, ACMSim As Object)
    ' Receive a string for the file name;
    ' Return objects for the ACM Flowsheet and Simulation
 
    Dim FileName As String
    Dim i As Integer
    Dim WinName As String
    
    On Error Resume Next
    
    'Check to see that ACM file actually open
    'Gets just the file name
    i = InStrRev(ACMFile, "\")
    FileName = Right(ACMFile, Len(ACMFile) - i)
    
    'Possible ACM window titles
    WinName = FileName & " - Aspen Custom Modeler V11 - aspenONE"
    
    If FindWindow(vbNullString, WinName) Then
        Set ACMSim = GetObject(ACMFile)
        If Err <> 0 Then
            MsgBox "Selected ACM file does not exist", vbOKOnly, "I need a valid ACM file"
            Err = 0
        Else
            Set ACMFlo = ACMSim.Flowsheet
        End If
    Else
        MsgBox ("Make sure ACM file " & FileName & " is open")
        End
    End If
End Sub
