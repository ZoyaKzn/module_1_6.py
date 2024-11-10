# module_1_6.py
#Работа со словарями
my_dict = {'Anna' : 1968, 'Petr' : 1962, 'Fedor' : 2012}
print('my_dict:',my_dict)
print('Existing value: ',my_dict['Fedor'])
print(my_dict.get('Helen'))
my_dict.update({'Rosa': 1970, 'Goga': 1963})
print(my_dict)
#del my_dict['Petr']
#print(my_dict)
#print(my_dict.get('Petr'))
a = my_dict.pop('Petr')
print('Deleted value:',a)
print(my_dict)
#Работа с множествами
my_set = {1,1,2,3,4,5,3,'Дыня', False}
print(my_set)
my_set.update([6, 'Арбуз', (1,3,5)])
print(my_set)
my_set.discard('Дыня')
print('Modified my_set:', my_set)