import psutil
import subprocess

for proc in psutil.process_iter():
    # check if process is started from scoop with folder containing ga_
    try:
        if "scoop" in proc.exe() and "ga_" in proc.cwd():
            
            proc.terminate()
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        continue

subprocess.run("reldplay quitall", shell=True)