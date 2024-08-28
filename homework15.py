# def test(a):
#     cnt=0
#     text="potato"
#     l=len(text)
#     for i in range(len(a)-l+1):
#         if a[i:i+l]==text:
#             cnt+=1
#     return cnt
# a=input()
# print(test(a))

# def test(a):
#     sum=0
#     for i in a:
#         if i>5:
#             sum+=i
#     return sum
# lst=list(map(int,input().split()))
# print(test(lst))

# def test(a):
#     print(f"{a[0:2]}... {a[0:2]}... {a}?")
# a=input()
# test(a)

# def test(a,b):
#     return a-(a*b/100)
# a=int(input())
# b=int(input())
# print(test(a,b))

# def test(a,b,c):
#     res=c//(a-b)
#     if c%(a-b)==0:
#         return res
#     else:
#         return res+1
# a=int(input())
# b=int(input())
# c=int(input())
# print(test(a,b,c))

# def test(a):
#     a=int(a)
#     lst=[]
#     a1=a//2
#     a2=a-a1
#     lst.append(a1)
#     lst.append(a2)
#     print(lst)
# a=input()
# test(a)

# def test(a,b):
#     if a==b:
#         print("True")
#     else:
#         print("False")
# lst=list(map(int,input().split()))
# lst1=list(map(int,input().split()))
# test(lst,lst1)

# def test(a):
#     print(a[1:])
# a=input()
# test(a)

# def test(a):
#     sum=0
#     for i in range(1,a+1):
#         sum+=1/i
#     return sum
# a=int(input())
# print(test(a))

# def test(a):
#     rev=""
#     for i in a[::-1]:
#         if i.islower():
#             rev+=i.upper()
#         else:
#             rev+=i.lower()
#     return rev
# a=input()
# print(test(a))