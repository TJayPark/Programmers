t# N, M을 공백을 기준으로 입력 받기
n, m = map(int, input().split())

arr = []
minVal = 0
for i in range(n):    
	arr.append(list(map(int, input().split())))

maxNum = None
for i in arr:
  num = None
  for j in i:
    if(num==None):
      num = j
    else:
      if(j<num):
        num = j
  if(maxNum == None):
    maxNum = num
  else:
    if(num>maxNum):
      maxNum = num
            
print(maxNum)  
      
