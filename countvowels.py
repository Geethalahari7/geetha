s=input("Enter a string:")
v=0
for i in s:
	if i in "aeiouAEIOU":
		v+=1
print(v)
