import os
current = os.getcwd()

folder_1 = "VSC"
file_name = "Doc1.txt"
full_path = os.path.join (current, folder_1, file_name)
with open (full_path, encoding='utf-8') as file:
    res=file.readline()
    print(res)



with open (full_path, 'rt', encoding='utf-8') as file:
    cook_books = {}
    for line in file:
        dish_name=line.strip()
        number_of_ingridients = int(file.readline().strip())
        list_of_ingridients=[]
        for _ in range(number_of_ingridients):
            ingredient_name, quantity, measure  = file.readline().strip().split('|')
            list_of_ingridients.append({
                'ingredient_name':ingredient_name,
                'quantity':quantity,
                'measure': measure

            })
        file.readline()
        cook_books[dish_name]=list_of_ingridients
    
    #print(cook_books)

#dishes=[]




#person_count=int(input("Введите количество"))   

#print(dishes, person_count)

def get_shop_list_by_dishes(dishes, person_count):
    res={}   
    for x in range(len(dishes)):
        for l in range(len(cook_books[dishes[x]])):
            if cook_books[dishes[x]][l]['ingredient_name'] not in res:
                res[cook_books[dishes[x]][l]['ingredient_name']]={'measure':cook_books[dishes[x]][l]['measure'], 'quantity': int(cook_books[dishes[x]][l]['quantity'])*person_count}
            else:
                res[cook_books[dishes[x]][l]['ingredient_name']]['quantity']+=(int(cook_books[dishes[x]][l]['quantity'])*person_count)


    print(res)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)











           
        
            

