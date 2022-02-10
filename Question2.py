import subprocess

cmd = "ls -la /dev/ | grep '\->' > devlinks.output"
data = subprocess.getoutput(cmd)
print(data)