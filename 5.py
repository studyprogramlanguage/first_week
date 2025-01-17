a = []
b = list()
a
b

x = [10, 20, 30, 40]
print(x)
print(x[0], x[3])
print(x[1:3])

x.remove(10)
print(x)
x.pop(2)
print(x)
x.clear()
print(x)

x = [10, 20, 30, 10, 10]
print(x.index(30))
print(x.count(10))

a = [10, 20, 30]
print("최솟값:", min(a))
print("최댓값:", max(a))
print("합계:", sum(a))

a = [10, 20, 30]
a = list(map(int, a))
print(a)
print(sum(a))

score = [[29, 28, 27, 30], [30, 29, 28, 27], [27, 28, 29, 30]]
for r in range(3):
    for c in range(4):
        print(score[r][c], end=" ")
    print()


score = []
while True:
    data = input("성적을 입력하세요: ")
    if data == "":
        break
    score.append(int(data))
    
print("성적 리스트:", score)
print("합계:", sum(score))