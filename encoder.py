import os

META_SYMBOL = "#"
input = 'input.txt'
output = 'code.txt'
offset = 0
count = 0


def write_to_file(count, symbol, filename):
    if count <= 3 and ord(symbol) != ord(META_SYMBOL):
        encode_string = symbol * count
    else:
        encode_string = META_SYMBOL + chr(count) + symbol

    with open(filename, 'a') as output_file:
        output_file.write(encode_string)


with open(output, 'w') as output_file:
    output_file.write('')

with open(input, 'r') as input_file:
    for i in range(0, os.path.getsize(input)):
        input_file.seek(offset)
        offset += 1
        symbol = input_file.read(1)
        if count == 0:
            prev_symbol = symbol
            code = ord(symbol)
            count += 1
        elif ord(symbol) == code and count < 255:
            count += 1
        else:
            write_to_file(count, prev_symbol, output)

            count = 1
            prev_symbol = symbol
            code = ord(symbol)

    if count != 0:
        write_to_file(count, prev_symbol, output)

    print('ENCODE DONE!')


