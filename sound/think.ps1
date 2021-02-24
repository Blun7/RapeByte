function Start-Thinking {
    
    Start-Job -Name Thinking -ScriptBlock { while ($true){ [console]::Beep((Get-Random -Min 300 -Max 7000), 200) } } | Out-Null
}

function Stop-Thinking {

    Stop-Job -Name Thinking -PassThru
}
