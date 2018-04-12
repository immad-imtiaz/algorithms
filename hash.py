import math
import numpy as np

hash_table = {i: [] for i in range(31)}

collisions = 0

for i in range(1, 1001):
    hash_key = math.floor(i * math.log(i, 2)) % 31
    if len(hash_table[hash_key]) > 0:
        collisions += 1
    hash_table[hash_key].append(i)

print('Total Collisions: %s' % collisions)

print('Items in Bucket')
[print('Key: %d, Items: %d' % (k,len(hash_table[k]))) for k in hash_table]

all_len = [len(hash_table[k]) for k in hash_table]

print('Mean Items in Bucket: %d' % np.mean(all_len))
print('Std of Items in Bucket: %d' % np.std(all_len))