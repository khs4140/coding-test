# print("'Hello'")


# print('Hello\nWorld')


# print('"Hello World"')


# print("\"!@#$%^&*()'")


# print("\"C:\Download\\'hello'.py\"")



# print("print(\"Hello\\nWorld\")")


# a1 = input()
# a2 = input()


# a = float(input())

# for _ in range(3):
#     print(a)


# a, b = input().split()
# print(int(a))
# print(int(b))


# a, b = input().split(' ')
# print(b)
# print(a)


# a= input()

# print(a)

# y, m, d = input().split('.')

# print(f"{d}-{m}-{y}")


# f, b= input().split('-')

# print(f+b)

# a = input()

# a = input()

# print(a[:2], a[2:4], a[4:])


# a= input().split(':')
# print(a[1])


# a = input().split(' ')
# print(a[0]+a[1])


# ans = int(input())
# sum_nums = 0
# nums = 1

# while sum_nums <= ans :
#     sum_nums += nums
    
#     nums += 1

# print(sum_nums)


# n, m = input().split(' ')


# n = int(n)
# m = int(m)


# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, ' ', j)


## 369게임
# ans = int(input())


# s = ''

# i = 1
# while i <= ans:
#     if i % 10 in (3, 6, 9):
#         s += 'X ' 

#     else:
#         s += str(i) + ' '
    
#     i += 1
    
# print(s)


# r, g, b = input().split(' ')

# r = int(r)
# g = int(g)
# b = int(b)

# count = 0
# for r_ in range(r):
#     for g_ in range(g):
#         for b_ in range(b):
#             print(r_, g_, b_)
#             count += 1
# print(count)



# h, b, c, s = input().split(' ')

# result = int(h) * int(b) * int(c) * int(s) / (8 * 1024 * 1024)
# print('%.1f MB' % result)


# w, h, d = map(lambda x : int(x), input().split(' '))

# result = w * h*d / (8 * 1024 * 1024)

# print('%.2f MB' % result)


# ans = int(input())

# i = 1
# sum_nums = 0
# while sum_nums < ans:
#     sum_nums += i
#     i += 1
# print(sum_nums)    



# ans = int(input())

# s = ''
# for i in range(1, ans+1):
#     if i % 3 == 0:
#         continue
#     s += str(i) + ' '

# print(s)
    

# a, m, d, n = map(lambda x: int(x),input().split())


# for _ in range(n-1):
#     a *= m
#     a += d

# print(a)

# a, b, c = map(lambda x: int(x), input().split())

# i = 1
# while True:
#     if i % a == 0 and i % b == 0 and i % c == 0:
#         print(i)
#         break
#     else:
#         i+=1


# n = int(input())
# ans = input().split()

# ans = list(map(lambda x : int(x), ans))

# for i in range(1, 24):
#     print(ans.count(i), end=' ')


# n = int(input())
# ans = list(map(lambda x: int(x), input().split()))
# result = list(reversed(ans))

# for i in result:
#     print(i, end=' ')


# n = int(input())
# ans = input().split()

# minimums = int(ans[0])
# for i in ans:
#     if int(i) <= minimums:
#         minimums = int(i)
# print(minimums)

## 6095
# d = []             

# for i in range(20): 
#     d.append([]) 
#     for j in range(20): 
#         d[i].append(0)

# n = int(input())
# for i in range(n):
#     x, y = map(int,input().split())
#     d[x][y] = 1 


# for i in range (1,20): 
#     for j in range (1,20): 
#         print(d[i][j], end =' ') 
#     print() 

## 6096
# a= [list(map(int,input().split())) for _ in range(19)] 
# n=int(input())

# for i in range (n):
#     x, y=map(int,input().split())
#     for j in range(19):
#         if a[x-1][j]==0: 
#             a[x-1][j]=1
#         else: 
#             a[x-1][j]=0

#     for j in range(19):
#         if a[j][y-1]==0:
#             a[j][y-1]=1
#         else:
#             a[j][y-1]=0

# for i in range(0,19):
#     for j in range(0,19):
#         print(a[i][j], end=' ')
#     print()


## 6097
# h, w = map(int, input().split())
# n = int(input())


# mat1 = [[0 for i in range(w)] for i in range(h)]


# for i in range(n):
#     l, d, x, y = map(int, input().split())
#     x -= 1
#     y -= 1

#     if d == 0:
#         for l_ in range(y, y+l):
#             mat1[x][l_] = 1
            
#     if d == 1:
#         for l_ in range(x, x+l):
#             mat1[l_][y] = 1


# for i in range(h):
#     for j in range(w):
#         print(mat1[i][j], end=' ')
#     print()


## 6098

mat1 = []
for _ in range(10):
    ans = list(map(int, input().split()))
    mat1.append(ans)
#--
# 0: 갈 수 있는 곳
# 1: 갈 수 없는 곳
# 개미가 이동하면 9로 변경

ma = mat1.copy()

x = 1
y = 1
d = 0 # 오른쪽 / 1이면 아랫쪽

ma[x][y] = 9
while not(x == 8 and y == 8) or ma[x][y] == 2:
    if d == 0:
        while d == 1:
            if ma[x][y+1] == 0:
                y += 1
                ma[x][y] = 9
            elif ma[x][y+1] == 1:
                d = 1
            elif ma[x][y] == 2:
                break
    elif d == 1:
        while d == 0:
            if ma[x+1][y] == 0:
                x += 1
                ma[x][y] = 9
            elif ma[x+1][y] == 1:
                d = 0
            elif ma[x][y] == 2:
                break
    
for i in range(10):
    for j in range(10):
        print(ma[i][j], end=' ')
    print()
