from itertools import groupby
import re

PHONE_LOG_FILE = "data.txt"

def remove_duplicates(_list):
    """Returns a new list with duplicates removed"""
    uniquekeys = []
    _list = sorted(_list)
    [uniquekeys.append(k) for k, _ in groupby(_list)]
    return uniquekeys


def find_phone_numbers(data):
    """Find all phone numbers in data"""
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # This regex matches phone numbers like 123-456-7890
    numbers = phoneNumRegex.findall(data)
    numbers = remove_duplicates(numbers)
    return numbers

with open(PHONE_LOG_FILE) as f:
    data = f.read()


# I recommend you check out the python docs about regexes if you're not familiar with them
# \d+/\d+\s matches '6/15 '
# \d{1,2}:\d{1,2}[AP]\s matches '5:14P '
# (\d\d\d-\d\d\d-\d\d\d\d) matches a phone number and it's in a group so that we can filter phone number later
# \n.+\n.+\n.+\n.+\n--\n--\n--\n 4 lines with any content then 3 '--' lines 
recordRegex = re.compile(r'(\d+/\d+\s\d{1,2}:\d{1,2}[AP]\s(\d\d\d-\d\d\d-\d\d\d\d)\n.+\n.+\n.+\n.+\n--\n--\n--\n)')
records = recordRegex.findall(data)

phoneNumbers = find_phone_numbers(data)
for number in phoneNumbers:
    print(f'Phone number: {number}')
    with open(f'{number}.txt', 'wt') as f:
        for record  in filter(lambda x: x[1] == number, records):
            print(record[0])
            f.write(record[0] + '\n')
