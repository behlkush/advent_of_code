def calculate_sum_top_3(file_handle):
    currSum = 0
    list_of_all_summs = []

    for line in file_handle:
        #The elves items are separated with an empty line
        if (line!="\n"):
            currSum += int(line)
        else:
            #Add the sums of each items belonging to that elf
            list_of_all_summs.append(currSum)
            currSum = 0

    #Reverse = true can be used as well but python gives us a way to do backward indexing
    list_of_all_summs.sort()
    finalSum = list_of_all_summs[-1] + list_of_all_summs[-2] + list_of_all_summs[-3]
    return(finalSum)

# can use with open as well but i want to keep the code to a beginner level
f = open("8462.txt", "r")
print(calculate_sum_top_3(f))