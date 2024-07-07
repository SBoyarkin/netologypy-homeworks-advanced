from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
def update_phone(phone):
  pattern = r'(\+7|8)\s*\(*(\d{3})\(*\s*\)*\-*\s*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})\s*\(*(\w*\.*)\s*(\d+)*\)*'
  subs = r'+7(\2)\3-\4-\5 \6\7'
  result = re.sub(pattern, subs, phone)
  return result

def struct_person(list):
  person_list = []
  for info in list:
    person = []
    for i in info[:3]:
      information = i.split(' ')
      if len(information[0]) == 0:
        continue
      else:
        person += information
    if len(person) != 3:
      person.append('')
    for i in info[3:]:
      i = update_phone(i).strip(' ')
      person.append(i)
    person_list.append(person)
  return person_list

def remove_dublicates(person_list):
  result = []
  while True:
    popped = person_list.pop()
    result.append(popped)
    for i in person_list:
      if popped[0] and popped[1] in i:
        print('это поппед',popped)
        print("это и",i)
        for indx, data in enumerate(popped):
          if data:
            continue
          else:
            popped[indx] = i[indx]
        result[-1] = popped
    if len(person_list) == 0:
      return result




if __name__ == '__main__':
  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    table_name = contacts_list[:1]
    intermediate_data = struct_person(contacts_list[1:])
    person_list = remove_dublicates(intermediate_data)




# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(person_list)