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
    print(len(person))
    person_list.append(person)
  return person_list






if __name__ == '__main__':
  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    person_list = contacts_list[:1]
    person_list += struct_person(contacts_list[3:])




# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(person_list)