
#lambda
hap3 = lambda num1 = 10, num2 = 20 : num1 + num2
hap3(10,20)
print(hap3(10,20))

#map()
myList = [10,20,30]
youlist = lambda num1 : num1 + 10
myList = list(map(youlist, myList))
print(myList)

myList = [10,20,30]
myList = list(map(lambda num : num + 10, myList))
print(myList)

#recursion function
def count(num):
    if num >= 1:
        print(num, end=' ')
        count(num-1)
        
    else:
        return
count(10)
count(20)

#generator function
def genFunc(num):
    for i in range(0, num):
        yield i
        print('generator function')
for data in genFunc(3):
    print(data)





