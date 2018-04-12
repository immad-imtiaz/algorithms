import numpy as np
import math


# # TODO: We aim to find the median of the two databases
# def find_median_for_join_database(database1, database2):
#     n = len(Database1)
#     k_db1 = k_db2 = int(n/2) - 1
#     levels = int(math.log(n, 2))
#
#     for i in range(2, levels+1):
#         print('level', i)
#         print(k_db1, k_db2)
#         median_db1 = query_database(database1, k_db1)
#         median_db2 = query_database(database2, k_db2)
#         print(median_db1, median_db2)
#         half = int(n / math.pow(2, i))
#         print('half',half)
#         if median_db1 > median_db2:
#             k_db1 -= half
#             k_db2 += half
#         else:
#             k_db1 += half
#             k_db2 -= half
#
#     return min(median_db1, median_db2)
#
#
def query_database(database, k):
    """
    This function just mimic of what the query database function would do
    :param database: Takes a database as input
    :param k: Takes value of position k
    :return: k smallest value in database
    """
    copy_database = database.copy()
    copy_database.sort()
    return copy_database[k-1]

# TODO: Two databases with n values each with no two values same, hence we have 2n values
Database1 = [5, 7, 3, 9, 13, 19, 20, 6]
Database2 = [11, 15, 1, 4, 17, 2, 10, 14]
# a = Database1.copy()
# a.sort()
# b = Database2.copy()
#
# # Initial Call
# median = find_median_for_join_database(Database1, Database2)
#
# print("The median for the join of databases is: %d" % median)
#


def check(database1, database2, start1, end1, start2, end2):
    mid1 = int(math.floor((end1 - start1)/2))
    mid2 = int(math.floor((end2 - start2) / 2))
    start1 = mid1 - start1 + 1
    end1 -= start1
    start2 = mid2 - start2 + 1
    end2 -= start2
    median_db1 = query_database(database1, mid1)
    median_db2 = query_database(database2, mid2)
    print(start1, mid1, end1)
    print(start2, mid2, end2)
    if start1 <= end1 and start2 <= end2:
        return min(median_db1, median_db2)

    if median_db1 < median_db2:
        check(database1, database2, mid1+1, end1, start2, mid2)
    else:
        check(database1, database2, start1, mid1, mid2+1, end2)

median = check(Database1, Database2, 0, len(Database1)-1, 0, len(Database2)-1)

print("The median for the join of databases is: %d" % median)







# In [4]: Database1
# Out[4]: [3, 5, 6, 7, 9, 13, 19, 20]
#
# In [5]: Database2
# Out[5]: [1, 2, 4, 10, 11, 14, 15, 17]

# level 2
# index 3,3
# med_1 7, 10


# In [4]: Database1
# Out[4]: [9, 13, 19, 20]
#
# In [5]: Database2
# Out[5]: [1, 2, 4, 10]

# level 3
# index 5,1
# med_1 7, 10
# med 13, 2



# In [4]: Database1
# Out[4]: [9]
#
# In [5]: Database2
# Out[5]: [4, 10]




