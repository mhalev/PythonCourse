from random import randrange

def list_int_to_str(list_of_int):

	return list(map(str,list_of_int))

list_of_int = [randrange(1,10) for _ in range(randrange(5,10))]

print('Список чисел: ',list_of_int,'\n'+'\r','Список строк: ', list_int_to_str(list_of_int))