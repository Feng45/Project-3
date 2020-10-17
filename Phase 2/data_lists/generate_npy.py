import numpy as np
a = open('all_file_names.txt')
lines = a. readlines()
last_line = lines[-1]
lines = lines[:-1]
b = {}
index = 0
for line in lines:
    num = index // 26
    b[line[:-1]] = num
    index = index + 1

b[last_line] = 9

print(b)

np.save('TIMIT_labels.npy', b)

c = np.load('TIMIT_labels.npy',allow_pickle=True)
print(c)
