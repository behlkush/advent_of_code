

def calculate_sum_top_3_method1(file_handle):
    currSum = 0
    list_of_all_summs = []

    for line in file_handle:
        if (line!="\n"):
            currSum += int(line)
            
        else:
            list_of_all_summs.append(currSum)
            currSum = 0


    list_of_all_summs.sort()
    finalSum = list_of_all_summs[-1] + list_of_all_summs[-2] + list_of_all_summs[-3]
    print(finalSum)


f = open("8462.txt", "r")
calculate_sum_top_3_method1(f)