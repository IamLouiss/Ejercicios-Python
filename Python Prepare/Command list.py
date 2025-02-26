if __name__ == '__main__':
    N = int(input())


list = []
for i in range(N):
    line = (input()).split()

    if("insert" in line):
        list.insert(int(line[1]), int(line[2]))
    elif("print" in line):
        print(list)
    elif("remove" in line):
        list.remove(int(line[1]))
    elif("append" in line):
        list.append(int(line[1]))
    elif("sort" in line):
        list.sort()
    elif("pop" in line):
        list.pop()
    elif("reverse" in line):
        list.reverse()