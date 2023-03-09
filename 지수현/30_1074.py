import sys

count=0

def recursive(x,y,N):
    global count
    if x==r and y==c:
        print(count)
        exit(0)
    
    if N==0:
        count+=1
        return
    
    recursive(x,y,N-1)
    recursive(x,y+2**(N-1),N-1)
    recursive(x+2**(N-1),y,N-1)
    recursive(x+2**(N-1),y+2**(N-1),N-1)
    
N,r,c = map(int,sys.stdin.readline().split())
recursive(0,0,N)

# import sys

# count=0

# def recursive(x,y,N):
#     global count

#     if x==r and y==c:
#         return 
    
#     if N==0:
#         count+=1
#         return
    
#     if x <=r<2**(N-1) and y <=c<2**(N-1):
#         recursive(x,y,N-1)
#     elif x <=r<2**(N-1) and 2**(N-1) <= c < 2**N:
#         recursive(x,N//2,N-1)
#     elif 2**(N-1) <= r < 2**N and y <=c<2**(N-1):
#         recursive(N//2,y,N-1)
#     else:
#         recursive(N//2,N//2,N-1)
    
# N,r,c = map(int,sys.stdin.readline().split())
# recursive(0,0,N)
# print(count)