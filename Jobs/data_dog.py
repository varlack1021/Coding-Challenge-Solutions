def same_string(a,b):

	s = a
	
	for i in range(len(a)):
		
		if a[i].isdigit():
			skip = a[i]
			b = b[:i] + skip + b[i+int(skip):]
	
	print(b)
	return b == a

a = "d3dog"
b  = "datadog"

print(same_string(a, b))

a = "d3dg"
b  = "datadogs"

print(same_string(a, b))

a = "d3d1g"
b  = "datadog"

print(same_string(a, b))

a = ""
b  = "datadog"

print(same_string(a, b))

a = ""
b  = ""

print(same_string(a, b))

a = "datadog"
b  = ""

print(same_string(a, b))