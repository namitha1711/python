
def print_zigzag(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s

    result = [''] * num_rows
    index, step = 0, 1

    for char in s:
        result[index] += char
        if index == 0:
            step = 1
        elif index == num_rows - 1:
            step = -1
        index += step

    return ''.join(result)

s = "PAYPALISHIRING"
num_rows = 3
print(print_zigzag(s, num_rows))
