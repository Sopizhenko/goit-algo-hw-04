import random
import timeit

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left, right)

def merge(left, right):
	sorted_arr = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			sorted_arr.append(left[i])
			i += 1
		else:
			sorted_arr.append(right[j])
			j += 1
	sorted_arr.extend(left[i:])
	sorted_arr.extend(right[j:])
	return sorted_arr

def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr

# Генеруємо випадкові дані для тестування
data_sizes = [1000, 5000, 10000, 20000]
data = {size: [random.randint(1, 1000) for _ in range(size)] for size in data_sizes}

# Виміряємо час виконання для кожного алгоритму сортування
for size, arr in data.items():
	print(f"Array size: {size}")
	# Злиттям
	merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
	print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")

	# Вставками
	insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
	print(f"Insertion Sort Time: {insertion_sort_time:.6f} seconds")

	# Timsort
	timsort_time = timeit.timeit(lambda: sorted(arr.copy()), number=1)
	print(f"Timsort (sorted) Time: {timsort_time:.6f} seconds")
	print()
