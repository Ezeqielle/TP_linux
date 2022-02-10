import re
import subprocess

cmd = "ps -U 0"
list_all_proc = []

# get all process
data = subprocess.getoutput(cmd)
data = data.split('\n')

x = 0
while x < len(data):
    list_all_proc.append(data[x])
    x += 1
list_all_proc.pop(0)
#print(list_all_proc[0])

# clean data
list_all_proc = [x.split() for x in list_all_proc]
while '' in list_all_proc:
    list_all_proc.remove('')
#print(list_all_proc)

# parse data
list_proc_cleaned = []
list_proc = []
i = 0
while i < len(list_all_proc):
    list_proc_cleaned.append(list_all_proc[i][3])
    i += 1
#print(list_proc_cleaned)
r = re.compile(".*d$")
list_proc = list(filter(r.match, list_proc_cleaned))
#print(list_proc)

# print clean list
x = 0
while x < len(list_proc):
    print(f"running process: {list_proc[x]}")
    x += 1