import csv  
with open('D:/abc.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Tên các cột là: {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} làm việc trong {row["department"]}, và được sinh ra tháng {row["birthday month"]}.')
        line_count += 1
print(f'Đã đọc {line_count} lines.')