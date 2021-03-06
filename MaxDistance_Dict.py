'''
Maximum Distance
Description
You will be given a list of repeated elements. You have to find the maximum distance between two same elements. The answer will be zero if there are no repeated elements.

----------------------------------------------------------------------
Input:
A non-empty list of integers.

Output:
A single integer denoting the maximum distance between two same integers.

----------------------------------------------------------------------
Sample input:
[1, 2, 3, 2, 5, 1, 2, 4, 6, 2, 7, 8, 6]

Sample output:
8

Explanation:
Max distance for 1: 5
Max distance for 2: 8
Max distance for 3: 0
Max distance for 4: 0
Max distance for 5: 0
Max distance for 6: 4
Max distance for 7: 0
Max distance for 8: 0
Execution Time Limit
Default.
'''

inputlist = [1, 2, 3, 2, 5, 1, 2, 4, 6, 2, 7, 8, 6]
maxIndex = 0
dict = {}
for index in range(0, len(inputlist)):
    cKey = inputlist[index]
    print("cKey: " + str(cKey))
    #if(dict.get(cKey)):
    if(cKey in dict):
        fistKeyIndex= dict[cKey]
        if((index - fistKeyIndex) > maxIndex):
            maxIndex = index - fistKeyIndex
    else:
        dict[cKey] = index
    print ("Dict: ", end = '')
    print(dict)
    print(maxIndex)
    print("*******")



print(maxIndex)
print (dict)


'''
Suggested Solution
#input has been taken for you
import ast
input_list= ast.literal_eval(input())

#start writing your code from here
#we will make a dictionary with keys as the elements of the list
#and values as a list of the indices of occurances of the the elements

d={}
for i in range(len(input_list)):
    if input_list[i] in d:
        d[input_list[i]].append(i)
    else:
        d[input_list[i]]=[i]

#now we just find the difference of first and last element of all the lists in d.values()
#the maximum difference will be out answer
answer=0

for v in d.values():
    difference=v[-1] - v[0]
    if difference > answer:
        answer=difference

print(answer)
'''