numOne = int(input('Enter The First Number : '))
numTwo = int(input('Enter The Second Number : '))
numOneDivisorList = {1}
numTwoDivisorList = {1}
gcd = []
numList = [numOne, numTwo]
for i in numList :
    for j in range(1, i+1) :
        if(i == numOne and i % j == 0) :
            numOneDivisorList.add(j)
        if(i == numTwo and i % j == 0) :
            numTwoDivisorList.add(j)
gcd = list(numOneDivisorList & numTwoDivisorList)
print('The GCD of',numOne,'and',numTwo,'is : ', gcd[-1])



