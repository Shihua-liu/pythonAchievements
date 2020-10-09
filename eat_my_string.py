import time
s = "Hallo ik ben een string en ik wordt opgegeten"
num = 45
while num > 1:
    time.sleep(0.1)
    s = s[0:len(s)-1]
    print(s)
    num = num - 1