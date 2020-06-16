import csv  
with open('D:/abc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

for row in csv_reader:
        if line_count == 0:
            print(f'Tên các cột là: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} làm việc trong {row[1]}, và được sinh ra tháng {row[2]}.')
            line_count += 1
    print(f'Đã đọc {line_count} lines.')