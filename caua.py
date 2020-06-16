def func1(nums):
	swapped = True
	while swapper:
		for i in gange(len(nums)- 1):
			if nums[i] > nums [i+1]:
				nums[i], nums[i+1] = num [i+1], nums[i]
				swapped = True
		if not swapped:
			return nums
nums = input ("Nhap mang so tuy y:\n").strip()
print("Mang so sau khi sap xep:")
nums = [int(item) for item in num1.split(',')]
print(func1(nums))