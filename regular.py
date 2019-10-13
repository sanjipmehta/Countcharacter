# Write a program to count a every character of string
s='abcdabcdefg'
d={}
for i in s:
	if i not in d:
		d[i]=1
	else:
		d[i]=d[i]+1
print(d)


# Write a program to count a every word  in the  string
s='ab and or not ab Ab or Not and'
m=s.split()
d={}
for i in m:
	if i not in d:
		d[i]=1
	else:
		d[i]=d[i]+1
print(d)