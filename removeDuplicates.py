def removeDuplicates_miSolucion(nums):
    aux = []
    for i in range(0, len(nums)):
        if not (nums[i] in aux):
            aux.append(nums[i])
    aux.sort()
    return aux

def removeDuplicates_conSet1(nums):
    mySet = set()
    for num in nums:
        mySet.add(num)
    return list(mySet)

def removeDuplicates_conSet2(nums):
    mySet = set(nums)
    return list(mySet)

print(removeDuplicates_miSolucion([1,2,5,3,2,3,4,5,1,1,6,6,7]))
print(removeDuplicates_conSet1([1,2,5,3,2,3,4,5,1,1,6,6,7]))
print(removeDuplicates_conSet2([1,2,5,3,2,3,4,5,1,1,6,6,7]))
