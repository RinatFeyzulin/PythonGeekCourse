from random import choices
def list_new(n,word):
    new_list= []
    for i in range(n):
        a=choices(word,k=3)
        new_list.append(''.join(a))
    return new_list

def list_search(my_list, key):
    if my_list.count(key)>1:
        print('yes')
        n=my_list.index(key)
        print(my_list.index(key, n+1))
    else:
        print(-1)
result=list_new(20,'abc')
print(result)
list_search(result,input())