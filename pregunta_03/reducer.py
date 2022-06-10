
#Escriba el codigo del reducer a partir de este punto <<<
import sys
if __name__ == '__main__':
    list_of_lists=[]
    for line in sys.stdin:  
        new_list = [elem for elem in line.split("\t")]
        list_of_lists.append(new_list)        
    for data in sorted(list_of_lists,key = lambda x: x[1]):
        sys.stdout.write("{},{}".format(data[0], data[1]))

# import sys
# import collections

# if __name__ == '__main__':

#     counter = collections.Counter()
#     for line in sys.stdin:
#         line = line.strip()
#         key, val = line.split("\t")
#         val=int(val)
#         counter[key] += val

#     for data in sorted(counter.items(),key = lambda x: x[1]):
#             sys.stdout.write("{},{}\n".format(data[0], data[1]))

        
        