import sys
from functools import lru_cache
import time

#set to a higher limit to run larger values in recursion
#method is used to set the maximum depth of the Python interpreter stack to the required limit. This limit prevents any program 
#from getting into infinite recursion, Otherwise infinite recursion will lead to overflow of the C stack and crash the Python.
sys.setrecursionlimit(10000)

#lru_cache() is one such function in functools module which helps in reducing the execution time of the 
#function by using memoization technique.
#@lru_cache
def ways_to_make_change_recursive(n:int,N:int, isodd:bool=True,coins:list=[1, 2,5, 20,10, 50,100,200])->int:
    """
    This function calculates the number of ways to make change for N cents,
    using only the denominations included in the passed `denominations_list`.

    parameters
    ----------
    n: int 
       count of number of coins
    N: int
        The target number of pence we wish to make change for.
    isodd: bool 
        If we need the odd combinations count.
    coins: list
        A list of denominations in pence that we can use to make change.
    """
 
    # If sum is 0 then return 0 or 1 based on isodd flag
    if (N == 0):
        if isodd:
            return 0
        else:
            return 1
 
    # If sum is less than 0, no solution exists
    if (N < 0):
        return 0

    # If there are no coins and the sum N is greater than 0, then no solution exist
    if (n <= 0):
        return 0
 

    # if we dont use the nth coin + if we do use the nth coin. We also pass in a flag isodd
    return ways_to_make_change_recursive( n - 1, N,isodd) + ways_to_make_change_recursive(n, N-coins[n-1],not isodd)
    
def coin_change(input_amount:str,coins:list =[1,2, 5, 10,20,50,100,200]) ->int:
    """                
    input_amount: a string represents money value in below format: £{Pound}-{Pence}                                                      
     For Example, £2-30  
    coins: list of coins available in pence. The coins used include 
     Two Pounds (200p), One Pound(100p), 50 p, 20 p, 10 p,
     5 p, 2 p and 1 p. The quantity of each type of coin is    
     unlimited. We represent this as a default list [1,2,5, 10,20,50,100,200]           

    Output: The order of coins does not matter, but the 
     change has to be in an odd number of coin counts that sum to the input_amount.            
    """

    input_amount = input_amount.split("-")
    pence = int(input_amount[1])
    pounds = int(input_amount[0].split("£")[1])
    #convert to total pence
    N = pounds*100 + pence
    #number of coins
    n=len(coins)
    print("n = ",n, " N = ",N)
    #print(f"Total_pence = {total_pence}p")
    total_odd_coin_change = ways_to_make_change_recursive(n,N)


    return total_odd_coin_change



if __name__ == "__main__":
    
    #Compute follow inputs: £0-50, £2-, £10-, (£100- for extra marks)
    total_amounts = ['£0-5','£0-7','£0-8','£0-10','£0-50','£2-0', '£10-0']
    #total_amounts = ['£100-0'] 
    for tot in total_amounts:
        start = time.time()
        ways_to_make_change  = coin_change(tot)
        print("\n")
        print(f"Total odd coin count that sum to {tot} = ",ways_to_make_change)
        end = time.time()
        print("The execution timw is :",round((end-start),3), "seconds")


#Total odd coin count that sum to £0-5 =  3

#Total odd coin count that sum to £0-7 =  3

#Total odd coin count that sum to £0-8 =  3

#Total odd coin count that sum to £0-10 =  5

#Total odd coin count that sum to £0-50 =  225

#Total odd coin count that sum to £2-0 =  36840

#Total odd coin count that sum to £10-0 =  160667940
