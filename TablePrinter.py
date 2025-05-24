def print_table(table_data):
    col_widths = [0] * len(table_data)
    for i, column in enumerate(table_data):
        col_widths[i] = max(len(word) for word in column)

    for row in range(len(table_data[0])):
        for col, column in enumerate(table_data):
            print(column[row].rjust(col_widths[col]), end=' ')
        print()

def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)

if _name_ == "_main_":
    main()
