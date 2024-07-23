n=int(input())
rev=0
x=n
while n>0:
	rem=n%10
	rev=rev*10+rem
	n=n//10
if rev==x:
	print("palindrome")
else:
	print("not a palindrome")
