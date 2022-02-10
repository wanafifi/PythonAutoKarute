import os
import time
from time import sleep

program_directory = "C:\\Users\\afifizain\\Desktop\\Program\\Program\\TAP 28 29 33-520 020 - GROUP B\\PLC\\"
data = program_directory.replace("\\", "/")
print(data)
with open("ProgramVersionHistory.txt", "r") as file:
    print(file.readlines())

os.chdir(data)
print("sucessful change directory")

# print(os.listdir(program_directory)[0])

list_file = []
list_last_modified = []
for file_name in os.listdir(program_directory):
    ti_m = os.path.getmtime(file_name)
    m_ti = time.ctime(ti_m)
    modification_time = time.strftime("%d.%m.%Y",time.localtime(ti_m))
    list_file.append(file_name)
    list_last_modified.append(modification_time)
    # print(os.listdir(program_directory)[file])

# print(list_file)
print(list_last_modified)
print("\n")
# print(len(list_file))

list_file_name = []
for file_name in list_file:
    fileSplit = file_name.split("--")
    list_file_name.append(fileSplit)

fileStrip = []
print(list_file_name)
print("\n")


with open("History_file.txt", mode="w", encoding="utf-8") as file:
    count = 0
    while count < len(list_file_name):
        suspended_item = list_file_name[count][0][-4:] 
        if suspended_item == ".bak" or suspended_item == ".txt" or len(list_file_name[count]) != 3:
            count += 1
        else:
            print(list_file_name[count][2][-4:])
            suspended_item2 = list_file_name[count][2][-4:]
            if suspended_item2 == ".bak" or suspended_item2 == ".opt":
                count += 1
            else:
                file.write(f"{list_last_modified[count]}\t\t\t{list_file_name[count][1]}\t\t\tPANEL NAME\t\t\tAFIFI\t\t\t{list_file_name[count][2][:-4]}\n")
                count += 1


