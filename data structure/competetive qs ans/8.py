
def solution(N, K):
    sum= 0
    count = 0
    for i in range(1,N+1):
        sum = sum + i
    # print(sum)
    if sum >= K:
     
        for j in range(N, 0,-1):
            print(j)
            if K >= j:
                K = K - j
                sum = sum -j
                count += 1
                # print("count is",count)
            elif(sum == K):
                K = K - j
                sum = sum -j
                count += 1
                # print("count is",count)
            elif K !=0:
                continue
            
            if(K == 0 or sum == 0):
                return count
                break

                
                  
    else:
        return -1
    
print(solution(4,10))