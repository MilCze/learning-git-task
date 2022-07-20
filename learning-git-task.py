shopping_list = {
    'piekarnia' : ['chleb' , 'bułki' ,  'pączek'] , 
    'warzywniak' : ['marchew' , 'seler' , 'rukola']
                 }


for element in shopping_list.values():
  for i in range(len(element)):
    element[i] = element[i].capitalize()


print(shopping_list)


shop_piekarnia = 'piekarnia'
shop_piekarnia_capitalize = shop_piekarnia.capitalize()

shop_warzywniak = 'warzywniak'
shop_warzywniak_capitalize = shop_warzywniak.capitalize()


print("Idę do" ,shop_piekarnia_capitalize , "kupuję tu następujące rzeczy:" , shopping_list['piekarnia'])
print("Idę do" ,shop_warzywniak_capitalize , "kupuję tu następujące rzeczy:" , shopping_list['warzywniak'])
print("W sumie kupuję 6 produktów.")