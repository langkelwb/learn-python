# 计算由a到b的阶乘
def jiecheng(a, b):
    result = 1
    for n in range(a, b + 1):
        result = result * n
    print(result)
    return result


jiecheng(1, 2)
jiecheng(2, 3)
jiecheng(1, 3)
jiecheng(2, 4)
test = [1, 2, 3, 4]
test.append(5)
print(test)
test.insert(4, "ANT")
print(test)
test.pop(4)
print(test)
sit = ['uii', 'ki']
test = [1, 2, 3, sit, 4]
print(test)
mint = [6, 3]
test[3] = mint
print(test)
l = len(test)
print(l)
print(test)
print(test[2])
print(test[3])

#s = input('birth: ')
#birth = int(s)
# if birth < (2000):
#   print('00前')
# else:
#   print('00后')


names = ['12', '13', '14']
for name in names:
    print(name)

sum = 0 
for x in range(101):
    sum = sum + x
print(sum)
