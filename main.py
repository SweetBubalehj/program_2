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

if re.search("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", ip):
    ip = ip.replace(".", "[.]")
    print(ip)
else:
    print("Invalid IP Address!")

# Number 3
arr = []

n = int(input("Enter length of array: "))

for i in range(0, n):
    temp = int(input('Enter number: '))
    arr.append(temp)
print("Array: ", arr)

arr.sort()
print("Array: ", arr)

arr.sort(reverse=True)
print("Array: ", arr)
