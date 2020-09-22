import os

META_SYMBOL = "#"
input = 'input.txt'
output = 'decode.txt'
offset = 0


with open(output, 'w') as output_file:
    output_file.write('')

with open(input, 'r') as input_file:
    for i in range(0, os.path.getsize(input)):
        input_file.seek(offset)
        symbol = input_file.read(1)
        decode_string = symbol

        if symbol == META_SYMBOL:
            input_file.seek(offset + 1)
            count = ord(input_file.read(1))
            input_file.seek(offset + 2)
            print_symbol = input_file.read(1)
            decode_string = print_symbol * count

            with open(output, 'a') as output_file:
                output_file.write(decode_string)
            offset += 3
            i += 2
        else:
            with open(output, 'a') as output_file:
                output_file.write(decode_string)
                offset += 1
print('DECODE DONE!')