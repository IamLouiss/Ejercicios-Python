def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

line = input()
print(split_and_join(line))