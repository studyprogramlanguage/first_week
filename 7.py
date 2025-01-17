import numpy as np

arr1 = np.array([1, 2, 3, 4])
print("1D 배열:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D 배열:\n", arr2)

print("배열의 형태:", arr2.shape)

arr3 = arr1 + 10
print("배열 덧셈:", arr3)

arr4 = arr1 * 2
print("배열 곱셈:", arr4)

mean = np.mean(arr1)
print("배열의 평균:", mean)

zeros_arr = np.zeros((3, 3))
print("0으로 채워진 배열:\n", zeros_arr)

ones_arr = np.ones((2, 4))
print("1로 채워진 배열:\n", ones_arr)

lin_space = np.linspace(0, 10, 5)
print("등차수열:", lin_space)

random_arr = np.random.rand(2, 3)
print("난수 배열:\n", random_arr)

transposed_arr = arr2.T
print("전치 배열:\n", transposed_arr)

arr5 = np.concatenate([arr1, arr4])
print("배열 결합:", arr5)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

element = arr2[1, 2]
print("특정 원소:", element)

sub_array = arr2[0:2, 1:3]
print("슬라이싱 결과:\n", sub_array)

row = arr2[1, :]
print("두 번째 행:", row)

col = arr2[:, 2]
print("세 번째 열:", col)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

sum_arr = arr1 + arr2
print("배열 덧셈:", sum_arr)

diff_arr = arr1 - arr2
print("배열 뺄셈:", diff_arr)

dot_product = np.dot(arr1, arr2)
print("배열의 내적:", dot_product)

sqrt_arr = np.sqrt(arr1)
print("배열의 제곱근:", sqrt_arr)
