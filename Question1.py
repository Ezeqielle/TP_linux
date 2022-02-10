import subprocess

# content with "x"
cmd = "ls erc/x11/ | grep '[x]'"
data = subprocess.getoutput(cmd)
print(f"content an x: \n{data}")

# begin with "x"
cmd = "ls erc/x11/ | grep '^x'"
data = subprocess.getoutput(cmd)
print(f"begin with x: \n{data}")

# content "x" or "X"
cmd = "ls erc/x11/ | grep '[xX]'"
data = subprocess.getoutput(cmd)
print(f"content x or X: \n{data}")

# begin with "x" or "X"
cmd = "ls erc/x11/ | grep '^[xX]'"
data = subprocess.getoutput(cmd)
print(f"begin with x or X: \n{data}")

# begin with "x" or "X" and content number
cmd = "ls erc/x11/ | grep '^[xX][0-9]'"
data = subprocess.getoutput(cmd)
print(f"begin with x or X and content number: \n{data}")

# begin with "x" or "X" and end by a number
cmd = "ls erc/x11/ | grep '^[xX][0-9]$'"
data = subprocess.getoutput(cmd)
print(f"begin with x or X and end by a number: \n{data}")