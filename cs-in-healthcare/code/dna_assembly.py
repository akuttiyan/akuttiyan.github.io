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

    #print("num splits", num_splits)
    for i in range(int(num_splits)):
        #print(i)

        start = random.randrange(0, len(dna_sequence) - 1)
        end = random.randrange(start, len(dna_sequence))
        #print(start)
        #print(end)
        while start == end or (end - start) < 3:
            start = random.randrange(0, len(dna_sequence) - 1)
            end = random.randrange(start, len(dna_sequence))

        split_piece = dna_sequence[start : end + 1]
        #print(split_piece)
        split_sequence.append(split_piece)

    #print(split_sequence)

    return split_sequence

#dna_split_sequence = split_sequence("ATCGGCGATACG")

#print(dna_split_sequence)


'''
def find_index(dna_1, dna_2):
    index = 0
    i = 0

    overlap_list = []
    
 
    group_size = len(dna_1)
    for i in range(len(dna_2) - group_size + 1):
        if dna_1 == dna_2[i : group_size]:
            overlap_list = [i, group_size]
            return overlap_list
        else:
            group_size += 1
  
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
    index = dict()
    

    #print("test1", dna_1)
    #print("test2", dna_2)

        
    if type(dna_1) == list:
        #print("list")
        #print(dna_1[0])
        parent = max(dna_1[0], dna_2)
        child = min(dna_2, dna_1[0])
    elif type(dna_2) == list:
        parent = max(dna_1, dna_2[0])
        child = min(dna_2[0], dna_1)
    elif type(dna_1) == list and type(dna_2) == list:
        parent = max(dna_1[0], dna_2[0])
        child = min(dna_2[0], dna_1[0])
    else:
        parent = max(dna_1, dna_2)
        child = min(dna_2, dna_1)
    


    for i in range(len(child) - 2):
        #print("hello")
        for j in range(len(parent) - 2):
            
            #print(child[i : i + 3])
            #print(parent[j : j + 3])
            if child[i : i + 3] == parent[j : j + 3]:
                #print("testing")
                
                #index = [parent, child, [i, i + 2], [j, j + 2]]
                if dna_1 == parent:
                    index[dna_1] = [j, j + 2]
                    index[dna_2] = [i, i + 2]
                    #index = [dna_1, dna_2, [i, i + 2], [j, j + 2]]
                elif dna_2 == parent:
                    index[dna_1] = [i, i + 2]
                    index[dna_2] = [j, j + 2]
                    #index = [dna_1, dna_2, [i, i + 2], [j, j + 2]]
                #print(index)
                for f in range(i + 3, len(child)):
                    #print("child", child[i : f + 1])
                    #print("parensf", parent[j : j + 3 + k])
                    if child[i : f + 1] == parent[j : j + 3 + k]:
                        if dna_1 == parent:
                            #index[dna_1] = [j, j + 3 + k]
                            index[dna_1] = [j, (j + 3 + k) - 1]
                            index[dna_2] = [i, f]
                        elif dna_2 == parent:
                            index[dna_1] = [i, f]
                            index[dna_2] = [j, (j + 3 + k) - 1]
                            #index[dna_2] = [j, j + 3 + k]
                        #return index
                    k += 1
                #print("yes")
                #print("index", index)
                return index

#test_dna = "ATCTGAATGTAT"
#other_dna = "CTGAATGT"

#similarities = find_similarities(test_dna, other_dna)
#print("function test", similarities)
                



#dict = find_similarities(dna_1, dna_2, over_lap_dict)

#print("dict", dict)



def find_overlap(dna_split_sequence):
    i = 0
    #over_lap_dict = defaultdict(list)
    dna_groups = []
    overlaps = dict()
    j = 0

    #print("test length", len(dna_split_sequence))


    for i in range(len(dna_split_sequence)):
        for split in dna_split_sequence:

            if split != dna_split_sequence[i]:
                test_dna = dna_split_sequence[i]
                #print("test_dna", test_dna)
                #print("split", split)
                overlap_info = find_similarities(test_dna, split)
                #print("overlap info", overlap_info)
                if overlap_info is not None:
      
                    #print("overlap info" ,  overlap_info)
                    #print("dna_split+sequence", dna_split_sequence[i])
                    #if type(dna_split_sequence) == list:
                    #over_lap_dict[dna_split_sequence[i][0]].append([overlap_info[1], overlap_info[2], overlap_info[3]])
                    #else:
                    #print(dna_split_sequence[i])
                    #try:
                    #    overlaps[dna_split_sequence[i]].append([overlap_info[1], overlap_info[2], overlap_info[3]])
                    #except:
                    #    overlaps[dna_split_sequence[i]] = [overlap_info[0], overlap_info[2], overlap_info[3]]
                    try:
                        overlaps[test_dna].append(split, overlap_info[test_dna], overlap_info[split])
                    except:
                        overlaps[test_dna] = [[split, overlap_info[test_dna], overlap_info[split]]]
                        break
                        #print(overlaps.items())
                    
                    #over_lap_dict[dna_split_sequence[i]].append([overlap_info[1], overlap_info[2], overlap_info[3]])
                    #print(dna_split_sequence[i])
    
    return overlaps

#test_split_sequence = ["ACTGG", "TGGC", "GGCA"]

#overlap = find_overlap(test_split_sequence)

#print("functioon test", overlap)

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

#dna_split_sequence = ["ATCG", "GCCC", "TCGAAA", "CCCTA"]
                
#dictionary = find_overlap(dna_split_sequence)
#items = dictionary.items()


#print(dictionary.items())



def combine_splits(over_lap_dict, key):
    new_over_lap_dict = dict()
    key_list = []
    all_combined_splits = []
    final_list = []
    j = 0

    key_list.append(key)

    combined_split = key_list[0]

    #print("combined split", combined_split[0])
    #print("over lap dict", over_lap_dict)
    '''
    for original_value in over_lap_dict:   
        for value in over_lap_dict[original_value]:
        # print("new value", value)


            #print(combined_split[0])
            
            #print("val", len(value[0]))
            #print("value", value[0])
            print("original value", original_value)
            print(value)
            if combined_split in value[0]:
                combined_split = value[0]
                #print("value", value[0][0 : splice])
                    
            elif value[0] in combined_split:
                print("do nothing")
                #print(combined_split)
                #print("value", value[0][0 : splice])
            elif (value[1][1] + 1) < len(value[0]):
                splice = len(value[0]) - value[1][1] - 1
                combined_split = combined_split + value[0][splice : len(value[0])]
                #print("test", combined_split[0])
                #print("value", value[0][0 : splice])
            elif value[1][0] > 0 and value[2][0] == 0:
                #print("yes")
                splice = value[1][0] - value[2][0]
                
                #print("overlap", value[0][0 : splice])
                #print(combined_split[0])
                #print("value", value[0][0 : splice])
                combined_split = value[0][0 : splice] + combined_split
                

                j +=1
            else:
                print("unknown case??")
            print("unknown", value, combined_split)
    '''
    
    for value in over_lap_dict[key]: 

    # print("new value", value)


        #print(combined_split[0])
            
        #print("val", len(value[0]))
        #print("original values", over_lap_dict[key])
        #print("value", value)
        dna_string = value[0]
        dna_string_index_2 = value[2][1]
        #print(dna_string_index_2)
        dna_string_index_1 = value[2][0]
        other_dna_string_index_1 = value[1][0]
        #print(dna_string)
        if combined_split in dna_string:
            combined_split = dna_string
                #print("value", value[0][0 : splice])
                    
        elif dna_string in combined_split:
            print("do nothing")
                #print(combined_split)
                #print("value", value[0][0 : splice])
        elif (dna_string_index_2 + 1) < len(dna_string):
            #splice = len(dna_string) - dna_string_index_2 + 1 #- 1
            splice = dna_string_index_2 + 1 
            combined_split = combined_split + dna_string[splice : len(dna_string)]
                #print("test", combined_split[0])
                #print("value", value[0][0 : splice])
        elif dna_string_index_1 > 0 and other_dna_string_index_1 == 0:
                #print("yes")
            #splice = other_dna_string_index_1 - dna_string_index_1
            splice = dna_string_index_1
                
                #print("overlap", value[0][0 : splice])
                #print(combined_split[0])
                #print("value", value[0][0 : splice])
            combined_split = dna_string[0 : splice] + combined_split
                

            j +=1
        else:
            print("unknown case??")
        #print("unknown", combined_split)
    return combined_split


#overlaps = dict()
#overlaps["CTAGAT"] = [["GATCCC", [0, 2], [3, 5]], ["GAT", [0, 2], [3, 5]], ["CTACTA", [3, 5], [0, 2]], ["TAGAT", [0, 4], [1, 5]], ["GACTACCCCCTA", [9, 11], [0, 2]]]

#test = combine_splits(dictionary, "CCCTA")

#print("function test", test)
#print("overlaps", overlaps)



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


dna = "TAATCGAGGCGAG"

dna_split_sequence = split_sequence(dna)

print(dna_split_sequence)

#dna_split_sequence = ["ATGC", "TGCCG", "GCC", "ATGC"]

#print(dna_split_sequence)

over_lap_dict = find_overlap(dna_split_sequence)
#print("test1", over_lap_dict)
dna_split_sequence = []
final_sequence = ["a", "b"]

'''
#print("length", len(final_sequence))
#print(over_lap_dict.items())
while len(final_sequence) != 1:
#for i in range(90):

    for key in over_lap_dict.keys():

        dna_split_sequence.append(combine_splits(over_lap_dict[key], key))
        print("dna_split_sequence", dna_split_sequence)
    final_sequence = dna_split_sequence
    
    #print("second", final_sequence)

    over_lap_dict = find_overlap(final_sequence)
    #print(over_lap_dict.items())
    
    dna_split_sequence = []
'''

  


while len(dna_split_sequence) != 1:
    dna_split_sequence = []
    for key in over_lap_dict.keys():

        dna_split_sequence.append(combine_splits(over_lap_dict, key))
        
        #print("dna_split_sequence", dna_split_sequence)
    

    final_sequence = dna_split_sequence
    #print(set(final_sequence))
    
    if len(set(final_sequence)) == 1: # studytonight.com
        final_sequence = final_sequence[0]
        print(final_sequence)
        break

    #equal = all(final_sequence)
    #if equal:
    #    print(final_sequence)
    #    break

    #print("second", dna_split_sequence)
    over_lap_dict = find_overlap(final_sequence)
    #print(over_lap_dict)
    #break
    #print(over_lap_dict.items())
print(final_sequence)





