x,y,w,h = map(int,input().split())

a = min(w-x,x-0)
b = min(h-y,y-0)

if a>b:
    print(b)
else:
    print(a)