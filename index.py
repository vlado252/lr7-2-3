import json
with open ("flower.json","r",encoding="UTF-8") as file:
     flowers = json.load(file)
count = 0

def menu():
     print("""
     1.Вывести все записи
     2.Вывести запись по полю
     3.Добавить запись
     4.Удалить запись по полю
     5.Выйти из программы
     """)
def all():
     global count
     print("Вы выбрали пункт: Вывести все записи")
     for flower in flowers:
          print(f"""
          Номер:{flower["id"]},
          Назавание:{flower["name"]},
          Латинское название:{flower["latin_name"]},
          Занесена в красную книгу РБ:{flower["is_red_book_flower"]};
          Цена:{flower["price"]}
          """)
def definite():
     global count
     print("Вы выбрали пункт: Вывести запись по полю")
     num_id = input("Введи номер id цветка который хотите получить: ")
     index = 1
     find = False
     try:
          num_id = int(num_id)
     except:
          print("Неккоректно введен id")
     for flower in flowers:
          if num_id == flower["id"]:
               print("Номер:",flower["id"])
               print("Назавание:",flower["name"])
               print("Латинское название:",flower["latin_name"])
               print("Занесена в красную книгу РБ:",flower["is_red_book_flower"])
               print("Цена:",flower["price"])
               print("Позиция в словаре = ",index)
               find = True
               break
     count +=1
     if not find:
          print("Запись с таким id не найдена")
def add():
     global count
     exists = False
     flag = True
     id = input("Введите id цветка которго хотите добавить: ")
     try:
          id = int(id)
     except:
          flag = False
     if(not flag):
          print("Значение введено неверно.")
     name = input("Введите название: ")  
     latin_name = input("Введите латинское название: ")  
     is_red_book_flower = input("Введите, занесен ли цветок в красную книгу (да/нет): ")  
     price = input("Введите сумму цветка: ")
     try:
          price = int(price)
     except:
          flag = False
           
     for flower in flowers:
          if flower['id'] == id:
               exists = True  
     if exists:
          print("Ошибка: цветок с таким номером уже существует.")
     if(not flag):
          print("Значение введено неверно.")
     else:
          new_flower = {
               'id': id,
               'name': name,
               'latin_name': latin_name,
               'is_red_book_flower': True if is_red_book_flower.lower() == 'да' else False, 
               'price': price
          }
          flowers.append(new_flower) 
          with open("flower.json", 'w', encoding='utf-8') as out_file: 
               json.dump(flowers, out_file)
          print("Цветок успешно добавлен.")
     count += 1
def delete():
     global count
     del_find = False
     print("Вы выбрали пункт: Удалить запись по полю")
     iddel = input("Введите id цветка который хотите удалить: ")
     try:
          iddel = int(iddel)
     except:
          print("Неверно введне id")
     for flower in flowers:
          if  flower["id"] == iddel:
               del_find = True
               flowers.remove(flower)
               with open("flower.json", 'w', encoding='utf-8') as out_file: 
                    json.dump(flowers, out_file)
               print("Цветок успешно удален.")
     if not del_find:
          print("Запись не найдена.")

     count+=1
          

def end():
     print("Вы выбрали пункт: Выйти из программы")
     print("Вы точно хотите выйти из программы:")
     yes_or_not = int(input("Введите 1 для подтверждения выхода или 2 для отмены выхода: "))
     if yes_or_not == 1:
          print("Программа завершена. Количество выполненых операци = ",count)
          quit()
     else:
          print("Не вышли из прогрмаммы")
def main():
     while True:
          menu()

          num = int(input("Введите номер действия: "))

          if num == 1:
               all()
          elif num == 2:
               definite()
          elif num == 3:
               add()
          elif num == 4:
               delete()
          elif num == 5:
               end()
          else:
               print("Такого номера нет.")

main()
