txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

languages = ['Python', 'Java', 'C++', 'French', 'C']
print('->'.join(languages))

even_num = [x for x in range(10) if x % 2 == 0]
print(even_num)

city = ["Seoul", "Tokyo", "New York"]
city2 = [cn for cn in city if cn != "Seoul"]
print(city2)

name = ["M", "N", "O", "P"]
no = [4, 5, 6, 7]
mapped = zip(name, no)
print(list(mapped))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
for x, y, z in zip(list1, list2, list3):
    print(x, y, z)