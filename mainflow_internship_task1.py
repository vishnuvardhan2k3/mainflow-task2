a_list=[1 , 2, 3, 4, 5]
b_dict={'k':1, 'l':2, 'm':3}
c_set={1, 2, 3, 4, 5}

#list basic operations
a_list.append(6)
print('list after adding 6:',a_list)

a_list.remove(5)
print('list after removing 5:',a_list)

a_list[2]=99
print('list after modifing the element 3 to 99:',a_list)

#dictionary basic operations
b_dict['n']=4
print('dictionary after adding n:',b_dict)

del b_dict["l"]
print('dictionary after removing l:',b_dict)

b_dict["m"]=7
print('dictionary after modifing m to 7:',b_dict)

#set basic operations
c_set.add(9)
print('Set after adding 9:',c_set)

c_set.remove(4)
print('set after removing 4:',c_set)

c_set.discard(3)
c_set.add(10)
print('set after changing an element 3 to 10:',c_set)
