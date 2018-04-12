import math

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def mergesort(list):
    if len(list) < 2:
        return list

    middle = math.floor(len(list)/2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)

A = [3, 4, 5, 1, 2, 8, 2, 3, 7, 6, 3, 5, 6]


def merge_dup(left, right):
    """
    :param left: Expects left split of the array as input
    :param right: Expects right split of the array as input
    :return result: Combined Array of left and right split with duplicates removed
    """
    if not len(left) or not len(right):
        return left or right
    l_idx,r_idx = 0,0
    k = len(right)-1
    result = []
    while l_idx < len(left):
        if left[l_idx] == right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
            r_idx += 1
        elif left[l_idx] == right[k]:
            result.append(left[l_idx])
            l_idx += 1
            k -= 1
        else:
            result.append(left[l_idx])
            l_idx += 1
    if l_idx == len(left):
        result.extend(right[r_idx:k+1])
    return result


def remove_duplicates(input_list):
    """
    This method splits the problem in to two sub problems each of size n/2
    :param input_list: Expects an input list with duplicates
    :return list: It returns list without duplicates
    """
    if len(input_list) < 2:
        return input_list
    middle = math.floor(len(input_list) / 2)
    left = remove_duplicates(input_list[:middle])
    right = remove_duplicates(input_list[middle:])
    return merge_dup(left, right)


print('Input Array: %s' % str(A))
print('Array Without Deuplicates: %s' % str(remove_duplicates(A)))