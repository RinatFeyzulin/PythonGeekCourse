# # 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# # Задача - сформировать файл, содержащий сумму многочленов.

# # out
# # The contents of the files do not match!

# from asyncore import read


# def read_file(file):
#     res=''
#     with open(file,'r') as data:
#         res=data.readlines()
#     return(str(res))

# def record_file(list1,list2):
#     with open('poly3','a') as data:
#         for i in range(len(list1)):
#             if len(list1[i])==len(list2[i]):
#                 data.write(f'{list1[i]} + {list2[i]} = 0\n')
#             else:
#                 data.write('The contents of the files do not match!\n')

# def delete_excess(list1):
#     new_list = []
#     for i in range(3):
#         a = str(list1[i])
#         b=''
#         for q in range(len(a)-7):
#             b+=a[q]
#         new_list.append(b)
#     return new_list

# list_file_poly=read_file('poly.txt').split(',')
# list_file_poly2=read_file('poly2.txt').split(',')
# list1=delete_excess(list_file_poly)
# list2=delete_excess(list_file_poly2)
# record_file(list1,list2)


def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "r", encoding="utf-8") as my_f_2:
        first = my_f_1.readlines()
        second = my_f_2.readlines()

        if len(first) == len(second):
            with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
                for i, v in enumerate(first):
                    my_f_3.write(f"{v[:-5]} + {second[i]}")
        else:
            print("The contents of the files do not match!")


# poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
poly_sum("poly.txt", "poly2.txt")