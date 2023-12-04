# Specify the path to the Python script
$pythonScriptPath = ".\main.py"

# Run the Python script and capture the output
Write-Output python3 $pythonScriptPath

# Print the Python script output in the PowerShell console
Write-Output "Python Script Output:"
Write-Output $output