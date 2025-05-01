def naveen(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j] == target:
                print(num[i],num[j])
        
nu= [2,3,4,1]
naveen(nu,3)


