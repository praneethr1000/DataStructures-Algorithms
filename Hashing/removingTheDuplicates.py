def removeDuplicates(s):
    a = ["notvisited"]*26
    for i in s:
        if a[ord(i) - 97] == "notvisited":
            print(i,end = "")
            a[ord(i) - 97] = "visited"

removeDuplicates("praneeth")
