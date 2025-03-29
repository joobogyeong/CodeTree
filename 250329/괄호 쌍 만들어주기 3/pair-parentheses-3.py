array=input()
cnt=0
for i in range(len(array)):
    if array[i]=="(":
        for j in range(i+1, len(array)):
            if array[j]==")":
                cnt+=1
print(cnt)
    
        
            
