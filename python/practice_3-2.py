print("2016113519 유지훈")

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("The example of recursikon")
tri_recursion(6)