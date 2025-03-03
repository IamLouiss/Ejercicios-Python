def average(array):
  lista = set(array)
  return (sum(lista)/len(lista))

if __name__ == '__main__':
  n = int(input())
  arr = list(map(int, input().split()))
  result = average(arr)
  print(result)