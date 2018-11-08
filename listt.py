val=''
a=['a','b','c']
for i in range(len(a)):
	if i==(len(a)-1):
		val+=('and '+a[i])
	else:
		val+=(a[i]+', ')
print(val)
