def commonelement(list1,list2):
    i=0; j=0
    common=[]
    while i<len(list1) and j<len(list2):
        if list1[i]==list2[j]:
            common.append(list1[i])
            i+=1
            j+=1
        elif list1[i]>list2[j]:
            j+=1
        else:
            i+=1
    return common

list1=list(map(int,input("Enter first list: ").split()))
list2=list(map(int,input("Enter second list: ").split()))
common=commonelement(list1,list2)
print("Common elements:",common)
