def climbStairs( n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

if __name__ == '__main__':
    print( climbStairs(4))