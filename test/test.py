from sys import argv
#filename = argv

f = open('a.txt')
f.seek(6)
print f.readline()
print f.readline()
print f.readline()
