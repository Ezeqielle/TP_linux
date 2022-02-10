import subprocess

account_list = []
logged_list = []

# Search all account in "/etc/passwd" file
account = 'grep -E "(bash)$" /etc/passwd'
data = subprocess.getoutput(account)
dataz = data.split('\n')

x = 0
while x < len(dataz):
    tmp1 = dataz[x].split(':')
    output = tmp1[0]
    #print(f"output: {output}")
    account_list.append(output)
    x += 1
x = 0

# Search all account logged with "who" command
logged = 'who'
data2 = subprocess.getoutput(logged)
form = data2.split('\n')

i = 0
while i < len(form):
    tmp = form[i].split(' ')
    forma = tmp[0]
    #print(f"who: {forma}")
    logged_list.append(forma)
    i += 1
i = 0

# Parse data from "/etc/passwd" file and compare with "who" command
while x < len(logged_list):  
    if logged_list[i] in account_list:
        print(f"Account logged: {logged_list[i]}")
    i += 1
    x += 1