list2=[2,4,6,8,10]

def fl(list):
    return [list[0],list[len(list)-1]]

print(fl(list2))


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
def lt5(list3):
    for value in list3:
        if (value<5):
            print(value)
            new_list.append(value)

lt5(a)
print (new_list)

nn=input("enter a number:")
nn2=int(nn)
def llt5(list4):
    for value in list4:
        if nn2> value:
            print(value)
llt5(a)
    

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list2=[]
def new(lit5,list6):
    for value in list5:
        for value1 in list6:
            if value==value1 and value not  in new_list2:
                new_list2.append(value)
