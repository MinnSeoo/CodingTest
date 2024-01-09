result = []
cnt = 0


for i in range(10):
    i = int(input())
    result.append(i)
    
divRst = list(set([j % 42 for j in result]))

        
print(len(divRst))