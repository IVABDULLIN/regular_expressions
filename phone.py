from pprint import pprint
import csv
import re

source_file = 'phonebook_raw.csv'
phone_pattern = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
sub_numbers = r'+7(\3)\6-\8-\10 \12\13'


def challenge_data():
  with open(source_file, encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  return contacts_list


def normal_view(contacts_list):
  new_contacts_list = []
  for list in contacts_list:
    data_of_contact = []
    full_string = ",".join(list[:3])
    result = re.findall(r'(\w+)', full_string)
    while len(result) < 3:
      result.append('')
    data_of_contact += result
    data_of_contact.append(list[3])
    data_of_contact.append(list[4])
    pattern = re.compile(phone_pattern)
    changed_phone = pattern.sub(sub_numbers, list[5])
    data_of_contact.append(changed_phone)
    data_of_contact.append(list[6])
    new_contacts_list.append(data_of_contact)
  return new_contacts_list


def delete_duplicates_contact(new_contacts_list):
  phone_book = {}
  for contact in new_contacts_list:
    if contact[0] in phone_book:
      contact_value = phone_book[contact[0]]
      for sign in range(len(contact_value)):
        if contact[sign]:
          contact_value[sign] = contact[sign]
    else:
      phone_book[contact[0]] = contact
  return list(phone_book.values())


def write_data(new_contacts_list):
  with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(new_contacts_list)


new_contacts_list = challenge_data()

new_parsed_list = normal_view(new_contacts_list)

contact_book_with_values = delete_duplicates_contact(new_parsed_list)

write_data(contact_book_with_values)