a = list(map(int,input().split()))

a_sort = sorted(a)
a_rever = sorted(a,reverse=True)


if a == a_sort:
    print("ascending")

elif a == a_rever:
    print("descending")
    
else:
    print("mixed")