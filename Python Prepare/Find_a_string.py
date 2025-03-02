def count_substring(string, sub_string):
  count = 0
  for i in range(len(string)):
    if string[i] == sub_string[0]:
      j = 0
      k = i
      while j < len(sub_string):
        if k == len(string): break
        print(f"{string[k]} : {sub_string[j]}")
        if string[k] != sub_string[j]: break
        j += 1
        k += 1
      else:
        count += 1
  return count
    

if __name__ == '__main__':
  string = input().strip()
  sub_string = input().strip()
    
  count = count_substring(string, sub_string)
  print(count)