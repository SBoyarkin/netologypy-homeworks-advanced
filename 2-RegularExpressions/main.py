from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  person_list = []
  for info in contacts_list[1:]:
    person = []
    for i in info[:3]:

      information = i.split(' ')
      if len(information[0]) == 0:
        continue
      else:
        person += information
    for i in info[3:]:
      person.append(i)
    print(person)


def update_phone(phone):
  pattern = r'(\+7|8)\s*\(*(\d{3})\(*\s*\)*\-*\s*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})\s*\(*(\w*\.*)\s*(\d+)*'
  subs = r'+7(\2)\3-\4-\5 \6\7'
  result = re.sub(pattern, subs, phone)
  return result


print(update_phone(p))

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)