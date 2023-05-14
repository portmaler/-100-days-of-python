def plusMinus(arr):
    n = len(arr)
    pos_count = sum(1 for i in arr if i > 0)
    neg_count = sum(1 for i in arr if i < 0)
    zero_count = sum(1 for i in arr if i == 0)

    pos_ratio = pos_count / n
    neg_ratio = neg_count / n
    zero_ratio = zero_count / n

    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
