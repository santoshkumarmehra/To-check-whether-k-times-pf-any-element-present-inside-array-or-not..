def findk(arr,k):
	for ele in arr:
		if ele*k in arr:
			return True
	return False

arr=[5,4,6,8,3,9]
k=2
result=findk(arr,k)
print(result)