
fout = open('new_file.txt', 'w')
fout.write("Hello file\n")
# 11
fout.close()
fin = open('new_file.txt', 'r')
for line in fin:
    print(line)
fin.close()

with open('new_file.txt', 'r') as file_handler:
    for line in file_handler:
        print(line)

print(file_handler)

