import sys
import subprocess

def runProcess(args:list) -> bool:
    """Run the specified command and return True 
    if the returncode is 0, False otherwise.
    """
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    print(result.stdout)
    return result.returncode == 0