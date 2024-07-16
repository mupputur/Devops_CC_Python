# Read the data from the file sample.txt
# and filterout the words which are start with 'a' and write in a_wrords.txt file
# also filter out the words which are start with 'c' and write in c_words.txt file
'''
<fileobject> open(filepath, mode)
read() , readlines()
write(str_data),   writelines(list_data)
close()
'''
path = "C:\\Users\\91998\\PycharmProjects\\CrashCourse\\config\\sample.txt"
#f = open('sample.txt', 'r')
f = open(path, 'r')
resp = f.read()
f.close()
print("-"*100)
print(resp)
print("-"*100)


