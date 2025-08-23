num_arr = input().split()
cost = 0
num = [int(x) for x in num_arr]
if num[0] < num[2] and num[1] < num[2]:
    cost += 1
else:
    for i in range(1,num[0]+1):
        if (num[0]%i==0):
            a_fac = i
            for j in range(0,num[1]+1):
                if (num[1]%j==0):
                    b_fac = j
                    if (num[0]/a_fac==num[1]/b_fac):
                        cost += 1
                        break
                    else:
                        continue
                else:
                    continue

        else:
            continue

if (cost==0):
    
