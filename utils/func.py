import json
import requests
from datetime import datetime

def unpacking(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json(), "INFO: данные получены успешно"
    return None, f"WARNING: ошибка {response.status_code}"


def get_filter(data, filtered_empy_from=False):
#    data = [x for x in data if ['state'] in x and x["state"] == "EXECUTED"]
    data = [x for x in data if 'state' in x and x["state"] == "EXECUTED"]
    if filtered_empy_from:
        data = [x for x in data if 'from' in x]
    return data


def get_last(data, count_last):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last]


def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        sender = row['from'].split()
        sender_bill = sender.pop(-1)
        sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}'
        sender_info = ' '.join(sender)
        recipient = f'**{row["to"][-4:]}'
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f'{date} {description}\n{sender_info} {sender_bill} -> Счет {recipient}\n{amount}\n')
    return formatted_data
