#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    print('weights ',weights)
    print('limit ',limit)

    for index in range(length):
        if weights[index] < limit:
             hash_table_insert(ht,weights[index], index)

    for index,weight in enumerate(weights):
        needed = limit-weight
        if hash_table_retrieve(ht, needed):
            if weight>needed:
                print((index,hash_table_retrieve(ht,needed)),weight,needed,limit)
                return (index,hash_table_retrieve(ht,needed))
            else:
                return (hash_table_retrieve(ht, needed),index)
        
    print('exiting')
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
