def max_and_min(lst):
    """Returns max and min of given list."""

    #return tuple containing max and min of list
    return (max(lst), min(lst))

def main():
    list1 = [10, -1, -34, 56]
    maxandmin = max_and_min(list1)

    #first, take a look at the type
    print(type(maxandmin))

    #get max from tuple
    max = maxandmin[0]
    #get min from tuple
    min = maxandmin[1]
    print(max, min)

    #another way to do this
    #double variable assignment, to get tuple values directly
    maxv2, minv2 = max_and_min(list1)
    print(maxv2, minv2)

if __name__ == '__main__':
    main()