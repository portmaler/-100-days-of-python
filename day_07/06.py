def generate(numRows):
    result = []
    old = []
    for i in range(numRows):
        newlist = []
        for j in range(i + 1):
            if j == 0 or j == i:
                newlist.append(1)
            else:
                newlist.append(old[j - 1] + old[j])
        old = newlist
        result.append(newlist)
    return result


if __name__ == '__main__':
    print(generate(5))
