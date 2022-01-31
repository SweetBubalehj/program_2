import re
# Number 1
string = str(input("Enter the string: "))
print(string[::-1])
# Самый быстрый способ

string = "".join(reversed(string))
print(string)
# Более медленный способ

# Number 2
ip = str(input("Enter the IP Address: "))

if re.match('[0-9]+(.[0-9]+){3}', ip):
    ip = ip.replace(".", "[.]")
    print(ip)
else:
    print("Invalid IP Address!")
