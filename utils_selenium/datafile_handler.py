def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for row in lines:
            if '\n' in row:
                row = row[:-1]
            
            list_row = row.split(',')
            data.append(list_row)
    return data