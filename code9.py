"""n=2
for i in range(1,11):
     if i%2==0:
          if i==6:
               break
          print(n*i)"""


s = "Welcome to the NRI"

count = 0

for i in s:
    if i in "aeiouAEIOU":
        count = count + 1

print(count)
