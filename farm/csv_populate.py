import csv

table_head = ['name', 'kind', 'owner', 'price']
tablde_data = [
    ['Apple', 'Eva', 'Tung', 4],
    ['Pear', 'South Africa', 'Tom', 8]
]

with open('for-population.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(table_head)
    writer.writerows(tablde_data)

