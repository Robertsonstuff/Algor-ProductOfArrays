# O(n**2) time - O(n) Space OR O(n) time - O(n) space 

# the idea is to multiply all the integers in the given array with the exception of each integer at a given time. example 1*4*2 then 5*4*2 then 5*1*2 etc.
# we are given the added constraint of not being able use division to solve this problem.
# this solution and all solutions should start out with the brute-force approach!!
# the question you want to ask is:
# is (i) and (j) at the same point? if so, do nothing
# if it isn't, use that integer to multiply another integer that may pop up.
# has (i) finished through the loop? if so, your done! 

#brute-force
def ProductOfArray(array):
    # this will create an array in products. All the integers will be 1 for the amount of integers that are in the given array. example [1,1,1,1]
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
        runningProject = 1
        for j in range(len(array)):
            #this checks our first question, if (i) and (j) are at the same point, do nothing and continue.
            #if (i) is NOT == to (j)
            # grab the variable from above and multiply the integer that is at position (j)
            if i != j:
                runningProject *= array[j]
        # this concludes the loop and checks that it is now back at the start.
        products[i] = runningProject
    
    return products

result = ProductOfArray([5,1,4,2])
print(result)

# better solution
# def ProductOfArray(array):
#     products = [1 for _ in range(len(array))]
#     Lproducts = [1 for _ in range(len(array))]
#     Rproducts = [1 for _ in range(len(array))]
		
#     LRunningProduct = 1
#     for i in range(len(array)):
#         Lproducts[i] = LRunningProduct
#         LRunningProduct *= array[i]

#     RRunningProduct = 1
#     for i in reversed(range(len(array))):
#         Rproducts[i] = RRunningProduct
#         RRunningProduct *= array[i]

#     for i in range(len(array)):
#          products[i] = Lproducts[i] * Rproducts[i]

#     return products
    

# result = ProductOfArray([5,1,4,2])
# print(result)