n = int(input())

def divideSum(num):
  sum = 0
  s_num = str(num)
  for i in range(len(s_num)):
    sum += int(s_num[i])
  return sum+num

com_num = 1
while True:
  if com_num > n :
    print(0)
    break
  if divideSum(com_num) == n:
    print(com_num)
    break
  else:
    com_num+=1