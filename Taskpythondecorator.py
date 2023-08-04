def decor1(main):
    pass
    def helper(x): 
        for i in range(1,x):
            yield i
    return helper

@decor1
def fun1(a):
    list1 = [j for j in range(1,a+1)]
    print(list1)
fun1(10)
