# Arya Kuttiyan
# Computer Science in Healthcare
# 4/23/2024
# The purpose of this code is to assemble dna from pieces

import random
import math
from collections import defaultdict

def split_sequence(dna_sequence):
    split_sequence = []
    num_splits = len(dna_sequence) * 4

    print("num splits", num_splits)
    for i in range(int(num_splits)):
        #print(i)

        start = random.randrange(0, len(dna_sequence) - 1)
        end = random.randrange(start, len(dna_sequence))
        #print(start)
        #print(end)
        while start == end or (end - start) < 3:
            start = random.randrange(0, len(dna_sequence) - 1)
            end = random.randrange(start, len(dna_sequence))

        split_piece = dna_sequence[start : end]
        #print(split_piece)
        split_sequence.append(split_piece)

    #print(split_sequence)

    return split_sequence



def find_index(dna_1, dna_2):
    index = 0
    i = 0

    overlap_list = []
    
    '''
    group_size = len(dna_1)
    for i in range(len(dna_2) - group_size + 1):
        if dna_1 == dna_2[i : group_size]:
            overlap_list = [i, group_size]
            return overlap_list
        else:
            group_size += 1
    '''
    '''
    elif dna_2 in dna_1:
        group_size = len(dna_2)
        for i in range(group_size - 1):
            if dna_2 == dna_1[i : group_size]:
                overlap_list = [dna_2, [i, group_size]]
                return overlap_list
      else:

        
            parent = max(dna_1, dna_2)
            child = min(dna_1, dna_2)            else:
                group_size += 1
    '''

'''
        for nucleotide_1 in dna_1:
            for nucleotide_2 in dna_2:
                if nucleotide_1 == nucleotide_2:
                start_index = dna_2.index(nucleotide)
            
            end_index = 
'''




def find_similarities(dna_1, dna_2):
    i = 0
    j = 0
    f = 0
    k = 1
    index = []
    

       
    parent = max(dna_1, dna_2)
    child = min(dna_1, dna_2)


    for i in range(len(child) - 2):
        print("hello")
        for j in range(len(parent) - 2):
            
            #print(child[i : i + 3])
            #print(parent[j : j + 3])
            if child[i : i + 3] == parent[j : j + 3]:
                print("testing")
                
                index = [parent, child, [i, i + 2], [j, j + 2]]
                #print(index)
                for f in range(i + 3, len(child)):
                    #print("child", child[i : f + 1])
                    #print("parensf", parent[j : j + 3 + k])
                    if child[i : f + 1] == parent[j : j + 3 + k]:
                        index = [parent, child, [i, f], [j, j + 2 + k]]
                        #return index
                    k += 1
                #print("yes")
                print("index", index)
                return index


                



#dict = find_similarities(dna_1, dna_2, over_lap_dict)

#print("dict", dict)

def find_overlap(dna_split_sequence):
    i = 0
    over_lap_dict = defaultdict(list)
    dna_groups = []
    j = 0


    for i in range(len(dna_split_sequence)):
        for split in dna_split_sequence:
            if split != dna_split_sequence[i]:
                test_dna = dna_split_sequence[i]
                overlap_info = find_similarities(test_dna, split[0])
                print(overlap_info)
                if overlap_info is not None:
      
                    #print("overlap info" ,  overlap_info)
                    over_lap_dict[dna_split_sequence[i]].append([overlap_info[1], overlap_info[2], overlap_info[3]])

    return over_lap_dict
    
    '''
    test_dna = dna_split_sequence.pop(0)

    while dna_split_sequence:
        for split in dna_split_sequence:
            overlap_info = find_similarities(test_dna, split)

            if overlap_info is not None:
                j += 1
                print("overlap info" ,  overlap_info)
                over_lap_dict[overlap_info[0]].append([overlap_info[1], overlap_info[2], overlap_info[3]])
                dna_split_sequence.pop(0)
        if dna_split_sequence:
            test_dna = dna_split_sequence.pop(0)
    
    print(j)
    return over_lap_dict
    '''


                
#dictionary = find_overlap(dna_split_sequence)
#items = dictionary.items()


#print(dictionary.items())



def combine_splits(over_lap_dict, key):
    new_over_lap_dict = dict()
    combined_split = []
    all_combined_splits = []
    final_list = []
    j = 0

    combined_split.append(key)

    for value in over_lap_dict:
        print("new value", value)


        print(combined_split[0])
        
        print("val", len(value[0]))
        print("value", value[0])
        if combined_split[0] in value[0]:
            combined_split = value[0]
                
        elif value[0] in combined_split[0]:
            print("do nothing")
            print(combined_split)
        elif (value[1][1] + 1) < len(value[0]):
            splice = len(value[0]) - value[1][1] - 1
            combined_split = combined_split[0] + value[0][splice : len(value[0])]
            print("test", combined_split[0])
        elif value[1][0] > 0 and value[2][0] == 0:
            print("yes")
            splice = value[1][0] - value[2][0]
            
            #print(value[0][0 : splice])
            print(combined_split[0])
            combined_split = value[0][0 : splice] + combined_split[0]

            j +=1
    return combined_split


#overlaps = dict()
#overlaps["CTAGAT"] = [["GATCCC", [0, 2], [3, 5]], ["GAT", [0, 3], [3, 5]], ["CTACTA", [3, 5], [0, 2]]]





#combined_split = combine_splits(overlaps["CTAGAT"], "CTAGAT")

#print("combined split", combined_split)




              
'''

    dna_split_sequence_two = dna_split_sequence
    for split in dna_split_sequence:
        #print("split" + split)
        dna_split_sequence_two.remove(split)
        #print("sequence", dna_split_sequence_two)
    for i in range(1, len(dna_split_sequence)):
        for dna in dna_split_sequence[i : len(dna_split_sequence)]:
            overlap_dict[dna] = []
            for split in dna_split_sequence:
            #print(dna)
                if split in dna:
                    #print("yes")
                    overlap_dict[dna].append([split, find_index(split, dna)])
                #print(overlap_dict)
                
          
                elif dna in split:
                overlap_dict[split] = [find_index(split, dna)]
                print(overlap_dict)

            else:
                #print("not match")
                
    #print("overlap", overlap_dict)
    return overlap_dict

'''

'''
def piece_together(overlap_dict):
    for (parent, child) in overlap_dict.values():

    
    for (parent, child) in overlap_dict.values():
        del parent[child[1][0] : child[1][1]]
        parent.extend(child[0])

overlap_dict = find_overlap(dna_split_sequence)
#print(find_overlap(dna_split_sequence))

parents = overlap_dict.keys()

print(parents)

'''
dna = "ATGCCCCAACTA"

dna_split_sequence = split_sequence(dna)
print(dna_split_sequence)

over_lap_dict = find_overlap(dna_split_sequence)
dna_split_sequence = []
final_sequence = ["a", "b"]

print("length", len(final_sequence))
print(over_lap_dict.items())
while len(final_sequence) > 1:
    for key in over_lap_dict.keys():

        dna_split_sequence.append(combine_splits(over_lap_dict[key], key))
    final_sequence = dna_split_sequence
    print(dna_split_sequence)
    over_lap_dict = find_overlap(dna_split_sequence)
    dna_split_sequence = []

print(final_sequence)





