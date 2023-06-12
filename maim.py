# n = 10
# #n
# count = 0
# for i in range(n): # 10 ед вр
#     print(i)
#     count += 1
# print("count",count)

# # n**2
# count = 0
# for i in range(n): # 10 ед вр
#     for j in range(n):
#         print(f'i-{i}   j-{j}')
#         count += 1

# print("count", count)


# input -> aabc         output ->   a-2  b-1 c-1


# # решение за  N**2
# def str_count(data):
#     for sym in data:# 5
#         count = 0 
#         for sym_2 in data:# 5
#             if sym == sym_2:
#                 count += 1
#         print(sym, count)



# str_count("aabcd")


# # решение за  N*M
# # N - длина строки    M - кол-во уникалных символов
# def str_count(data):
#     for sym in set(data):# 4
#         count = 0 
#         for sym_2 in data:# 5
#             if sym == sym_2:
#                 count += 1
#         print(sym, count)



# str_count("aabcd")


# решение за  N
# N - длина строки   
def str_count(data):
    str_count = {}
    for sym in data: # 5
        str_count[sym] = str_count.get(sym,0) + 1

    print(str_count)




# https://github.com/  - зарегистрироваться
# https://gitforwindows.org/    -скачать
# https://desktop.github.com/   -скачать
str_count("aabcd")





# git init
# 











# family = {}
# family["dad"] = 1 # добавил
# family["mam"] = 1
# print(family)
# family["child"] = 1
# print(family)
# #                     получить детей, если детей нет то по дефолту ставим 0
# family["child"] = family.get("child",0) + 1 # обновил
# print(family)

















#  set - множество ,неупорядоченный тип данных который содержит только уникальные значения




# x = {1,1,2,3} # set
# print(x)



# y = set()
# print(y)


# b = {}# dict
# print(type(b))

# l = [1,1,2,2,3,4]
# l = list(set(l))
# print(l)





