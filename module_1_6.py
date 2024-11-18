# Работа со словарем
my_dict={'Ivan':1990,'Alex':1992,'Anton':1995}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('ZHenya'))
my_dict.update({'Sasha':1989,
                   'Misha':1993})
print(my_dict)
my_dict.pop('Alex')
print(my_dict['Ivan'])
print(my_dict)

#Работа с множеством
my_set={2,3,66,7,'aaa',False,'aaa',3,66,1}
print(my_set)
print(my_set.add('bbbb'))
print(my_set.add('True'))
print(my_set)
print(my_set.discard('aaa'))
print(my_set)