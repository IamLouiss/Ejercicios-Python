if __name__ == '__main__':
  students = []
  for _ in range(int(input())):
    name = input()
    score = float(input())
    student = [name, score]
    students.append(student)

  menor = segunda_menor = float('inf')
  for i in range(len(students)):
    if students[i][1] < menor:
      segunda_menor = menor
      menor = students[i][1]
    elif students[i][1] < segunda_menor and students[i][1] != menor:
      segunda_menor = students[i][1]

  segundos_students = []
  for i in range(len(students)):
    if students[i][1] == segunda_menor:
      segundos_students.append(students[i][0])

  segundos_students = sorted(segundos_students)
  for student in segundos_students:
    print(student)