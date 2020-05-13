def remove(string):
    stkptr = -1
    i = 0
    size = len(string)
    while i < size:
        if stkptr == -1 or string[stkptr] != string[i]:
            stkptr += 1
            string[stkptr] = string[i]
            i += 1
        else:
            while i < size and string[stkptr] == string[i]:
                i += 1
            stkptr -= 1
    stkptr += 1
    string = string[0:stkptr]
    print(string)

remove(list("careermonk"))

# def removeDuplicates(l1):
#     found = -1
#     newList = []
#     for i in range(len(l1)):
#         if len(newList) == 0:
#             newList.append(l1[i])
#         else:
#             if newList[-1] == l1[i]:
#                 found += 1
#                 newList.pop()
#             else:
#                 newList.append(l1[i])
#     if found == -1:
#         return ''.join(newList)
#     else:
#         return removeDuplicates(newList)