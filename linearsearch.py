def linearsearch (arr,x):
    for i in range(len(arr)):
        if arr [i]==x:
            return i
        return-1
    arr=[2,5,7,9,11]
    x=9
    result=linear search (arr,x)
    if(result==-1):
        print("Element not found")
        else:
            print("element fount at index:",result)
