
import pytest
from itertools import islice

from ..odd_coin_combination import ways_to_make_change_recursive


def test_coin_series_1():
    """The total number of ways to make 5p from the coins [1,2,5,10,20,50,100,200]
       1. 1,1,1,1,1
       2. 1,1,1,2
       3. 1,2,2
       4. 5
       so we have three combinations that are odd
    """
    coins:list =[1,2, 5, 10,20,50,100,200]

    n=len(coins)
    N=5
    print("Number of coins = ",n," Total sum = ",N)
    assert ways_to_make_change_recursive(n,N,True,coins) == 3

def test_coin_series_2():
    """The total number of ways to make 7p from the coins [1,2, 5, 10,20,50,100,200]
       1. 1,1,1,1,1,1,1
       2. 1,1,1,1,1,2
       3. 1,1,1,2,2
       4. 2,2,2,1
       5. 5,1,1
       6. 5,2
       so we have three combinations that are odd
    """
    coins:list =[1,2, 5, 10,20,50,100,200]

    n=len(coins)
    N=7
    print("Number of coins = ",n," Total sum = ",N)

    assert ways_to_make_change_recursive(n,N,True,coins) == 3


def test_coin_series_3():
    """The total number of ways to make 8p from the coins [1,2, 5, 10,20,50,100,200]
       1. 1,1,1,1,1,1,1,1
       2. 1,1,1,1,1,1,2
       3. 1,1,1,1,2,2
       4. 1,1,2,2,2
       5. 2,2,2,2
       6. 5,2,1
       7. 5,1,1,1
       so we have three combinations that are odd
    """
    coins:list =[1,2, 5, 10,20,50,100,200]

    n=len(coins)
    N=7
    print("Number of coins = ",n," Total sum = ",N)

    assert ways_to_make_change_recursive(n,N,True,coins) == 3

def test_coin_series_3():
    """The total number of ways to make 10p from the coins [1,2, 5, 10,20,50,100,200]
       1. 1,1,1,1,1,1,1,1,1,1
       2. 1,1,1,1,1,1,1,1,2
       3. 1,1,1,1,1,1,2,2
       4. 1,1,1,1,2,2,2
       5. 1,1,2,2,2,2
       6. 2,2,2,2,2
       7. 5,2,2,1
       8. 5,2,1,1,1
       9. 5,1,1,1,1,1
      10. 5,5
      11. 10 
      so we have five combinations that are odd
    """
    coins:list =[1,2, 5, 10,20,50,100,200]

    n=len(coins)
    N=10
    print("Number of coins = ",n," Total sum = ",N)

    assert ways_to_make_change_recursive(n,N,True,coins) == 5
    