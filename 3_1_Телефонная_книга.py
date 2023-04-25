phoneBook = {}

for i in range(int(input())):
    query = input().split()
    if query[0] == "add":
        phoneBook[query[1]] = query[2]
    elif query[0] == "find":
        print(phoneBook.get(query[1], "not found"))
    elif query[0] == "del":
        if query[1] in phoneBook:
            del phoneBook[query[1]]