a=10

if a > 5:
    print("a는 5보다 큽니다.")
elif a <= 5:
    print("a는 5보다 작거나 같습니다.")
else:
    print("a는 5입니다.")
    
a=10
b=5

if a > 5 and b < 10:
    print("a는 5보다 크고, b는 10보다 작습니다.")

a = [1, 2, 3, 4, 5]
print(a)

for i in a:
    print(i, end=" ")
    
for i in range(1, 10, 2):
    print(i)
    
i = 1
while i < 10:
    print(i)
    i += 1
    
for i in range(5):
    if i%2==1:
        continue
    print(i)
    
def add(x, y):
    s = x + y
    a = s/2
    return a, s

sum, avg = add(10, 30)
print(sum, avg)

a=1
while (a<=3):
    print("안녕", a)
    a = a + 1