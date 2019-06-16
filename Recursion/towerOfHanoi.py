t= int(input())
def tower(n,from_rod,to_rod,mid_rod):
    if n==1:
        print("move disk 1 from rod " + from_rod + " to rod " + to_rod)
        return
    tower(n-1,from_rod,mid_rod,to_rod)
    print("move disk "+ str(n) +" from rod " + from_rod + " to rod " + to_rod)
    tower(n-1,mid_rod, to_rod,from_rod)
for i in range(t):
    n=int(input())
    tower(n,"1","3","2")
    print(2**n-1)
