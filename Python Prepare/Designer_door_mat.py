entrada = input().split()
N = int(entrada[0])
M = int(entrada[1])
char = ".|."
ind = 1

for i in range(N):
  print((char * ind).center(M, "-")) if i != N // 2 else print("WELCOME".center(M,"-"))
  if (i < N // 2):
    ind += 2
  else:
    ind -= 2