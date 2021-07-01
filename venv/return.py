t = [1, 2]

for v in range(2):
    t.insert(-1, t[v])

print(t)

#def func1 (a):
#    return None

#def func2 (a):
 #   return func1(a) * func1(a)

#print(func2(2))

print(1//2)

#def func(a, b):
#    return b ** a
#print(func(b=2, 2))

#z = 0
#y = 10
#x = y < z and z > y or y > z and z < y
#print(x)

list = [x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(list))

#x = 1
#y = 2
#x, y, z = x, x, y
#z, y, z = x, y, z

#print(x, y, z)

#a = 1
#b = 0
#a = a ^ b
#b = a ^ b
#a = a ^ b
#print(a, b)

#def fun(x):
  #  if x % 2 == 0:
  #      return  1
 #   else:
 #       return 2

#print(fun(fun(2)))

#nums = [1, 2, 3]
#vals = nums
#del vals[:]
#print(nums, vals)

#x = int(input())
#y = int(input())
#x = x % y
#x = x % y
#y = y % x
#print(y)

#y = input()
#x = input()
#print(x + y)

#print("a", "b", "c", sep="sep")

#x = 1 // 5 + 1 / 5
#print(x)


#tuples[1] = tuples[1] + tuples[0]

#w = float(input())
#t = float(input())
#print(t ** (1 / w))

#dct = {'uno':'dos', 'tres':'uno', 'dos':'tres'}
#v = dct['tres']

#for k in range(len(dct)):
#    v = dct[v]

#print(v)

#lst = [i for i in range(-1, -2)]
#lst.count(i)

#def asd(a, b, c=0):
 #   return

#asd(a=0, b=0)

#def cvb(x, y):
 #   if x == y:
  #      return x
   # else:

    #    return cvb(x, y-1)


#print(fun(0, 3))

#i = 0
#while i < i + 2:
 #   i += 1
  #  print("*")
#else:
 #   print("*")

#tuo = (1, 2, 4, 8)
#tuo = tuo[-2:-1]
#tuo = tuo[-1]
#print(tuo)

#dd = {"1":"0", "0":"1"}
#for x in dd.vals():
 #   print(x, end="")



def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))