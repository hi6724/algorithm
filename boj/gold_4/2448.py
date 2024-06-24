'''
3 1
6 2
12 3
24 4
48 5
96 6 

모든 문자열의 길이 = 2N-1
6 -1  3  
12 -1 6
24 -1 12
      24
      48
      96
'''
import math

N = int(input())
k = int(math.log2(N/3))+1

pattern = ["  *  ", " * * ", "*****"]
dp = [[], pattern]
for i in range(2, 12):
  row = []

  height = len(dp[i-1])*2
  width = (height*2)-1

  for j in range(height):
    try:
      blank = ''
      for d in range((width-len(dp[i-1][j]))//2):
        blank += ' '
      temp = blank+dp[i-1][j]+blank
      row.append(temp)
    except:
      temp = ''
      temp += dp[i-1][j-height]
      temp += ' '
      temp += dp[i-1][j-height]
      row.append(temp)

  dp.append(row)
for p in dp[k]:
  print(p)
