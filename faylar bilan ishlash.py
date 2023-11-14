with open('../server/pi.txt') as fayl:
    pi = fayl.read()
# print(pi)
fayl.close()

pi = pi.rstrip()
pi = pi.replace('\n','')
pi = float(pi)
print(pi)