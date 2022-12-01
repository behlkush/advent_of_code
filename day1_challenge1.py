

f = open("8462.txt", "r")
maxSum = 0
currSum = 0
top3list = [0, 0, 0]
dict_index = 0
dict_of_all = {}

for line in f:
    if (line!="\n"):
        currSum += int(line)
        
    else:
        dict_of_all[dict_index] = currSum
        currSum = 0
        dict_index += 1

final_list = []
for keys in dict_of_all.keys():
    final_list.append(dict_of_all[keys])

final_list.sort()
print(final_list)
finalSum = final_list[-1] + final_list[-2] + final_list[-3]
print(finalSum)