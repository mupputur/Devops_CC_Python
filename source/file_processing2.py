import sys
import os


current_dir = sys.path[1]
config_path = os.path.join(current_dir, "config")

file_path = os.path.join(config_path, 'sample.txt')
#print(file_path)
f = open(file_path, 'r')
resp = f.read()
f.close()
print("-"*100)
print(resp)

"""
path = "C:\\Users\\91998\\PycharmProjects\\CrashCourse\\config\\sample.txt"
f = open(path, 'r')
resp = f.read()
f.close()
print("-"*100)
print(resp)
print("-"*100)
"""