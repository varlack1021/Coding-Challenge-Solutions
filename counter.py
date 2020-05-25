from collections import Counter
text = "lolololabai";
#return sum(1 for _, n in Counter(text.lower()).items() if n > 1)
x = Counter(text)
print(sum (value for key, value in x.items())
)



from collections import Counter

    
print(x)
print("_")
for key in x:
	print(key)