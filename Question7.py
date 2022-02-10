import subprocess

cmd = 'grep "ssh" /etc/services'
list_all_port = []

data = subprocess.getoutput(cmd)
data = data.split('\n')

x = 0
while x < len(data):
    list_all_port.append(data[x])
    x += 1
x = 0
#print(list_all_port)

# clean data
z = 0
list_all_proc = [x.split() for x in list_all_port]
while '' in list_all_proc:
    list_all_port.remove('\t')
#print(list_all_proc)
#while z < len(list_all_proc):
#print(len(list_all_proc))
print(f"SSH port is: {list_all_proc[0][1]}")
