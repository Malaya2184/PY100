# str = "malayamalayarrrrrrrrrrrmalayaxxmalaya"
# pattern = "malaya"


# def countfreq(str, pattern):
#     x= len(str)
#     y= len(pattern)
#     count = 0

#     for i in range (x-y + 1):
#         j=0
#         # here while condition will break if first element will not match so there is a break so that it can iterate to the next element for next iteration
#         # if first element matches then j increases so that it will check the contigous string
#         while j< y:
#             if (str[i+j] != pattern[j]):
#                 break
#             j +=1

#         if (j == y):
#             count +=1
#             j = 0
#     return count



# print(countfreq(str, pattern))

# id_in_func = {
#     1:'one',
#     2:'two',
#     3:'three',
#     4:'four',
#     5:'five',
#     6:'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
#     10: 'ten'
# }
# ids_to_be_deleted = [1,3,4]
# for i in ids_to_be_deleted:
#     del id_in_func[i]

# print(id_in_func)

# =============================================================
# id_in_func = {
#     1:'one',
#     2:'two',
#     3:'three',
#     4:'four',
#     5:'five',
#     6:'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
#     10: 'ten'
# }
# ids_to_be_deleted = [1,3,4]
# length = len(ids_to_be_deleted)
# for i in range (length):
#     n = ids_to_be_deleted[i]
#     del id_in_func[n]

# print(id_in_func)

# ================================================================

# import re
# DNA ="TACCTACCTACCTACCTACCTACCTACCTACCAUGGGGGGGGTACCTACCTACCTACCTACCTACCUGTACCTACCTACCTACCTACCTACCAUGTACCTACCTACCTACCTACC"
# SSR = re.finditer(r"(TACC){5,50}", DNA)
# # print (SSR)
# count = 0
# for i in SSR:
#     print(i.group())
#     print(len(i.group())//4)
#     count += 1

# print(count)


# import re
# DNA ="TACCTACCTACCTACCXXXXXXXXXXXTACCTACCTACCTACCTACC"
# SSR = re.search(r"(TACC){5,50}", DNA)
# if  SSR:
#     print('yeahh i got it')
# else:
#     print('opps not found')