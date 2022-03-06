# numbers=["4", "45", "36", "25", "200"]
# numbers=list(map(int, numbers))
# numbers[3]=numbers[3]+5
# print(numbers[3])

# def sq(a):
#     return a*a
# num =[2,3,85,2,85,52,8,1,74,7]
# square= list(map(sq, num))
# print(square)

# num =[2,3,85,2,85,52,8,1,74,7]
# square= list(map(lambda x:x*x, num))
# print(square)

def square(a):
    return a*a
def cube(a):
    return a*a*a
func =[square, cube]
for i in range(0,5):
    val= list(map(lambda x:x(i), func))
    print(val)