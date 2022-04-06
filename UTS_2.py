#!/usr/bin/python3
# UTS April 6 2022
# Muhammad Shofuwan Anwar (21/483339/SV/20142)

# calulator interpreter
from tkinter import N


def parse_op_from_str(str_data):
    operator_ch = ('+', '-', '*', '/', '%')
    data_op = []

    for i in range(len(str_data)):
        if str_data[i] in operator_ch:
            data_op.append(str_data[i])
    
    return data_op

def parse_num_from_str(str_data):
    data_num = []
    add_digit_as_str = ''
    is_float = False

    # check if it's a number, then add all digits to the list
    str_data += ' '
    for i in range(len(str_data)):
        if str_data[i].isdigit() or str_data[i] == '.':
            if str_data[i] == '.':
                is_float = True
            add_digit_as_str += str_data[i]
        else:
            if is_float:
                data_num.append(float(add_digit_as_str))
            else:
                data_num.append(int(add_digit_as_str))
            add_digit_as_str = ''
    
    return data_num

def process_op_and_num(operator_list, number_list):
    result = []

    try:
        # Calculate the number list depending on the operator list
        for x in range((len(operator_list)*2)-1):
            if operator_list[x] == '+':
                result.append(number_list[x] + number_list[x+1])
            elif operator_list[x] == '-':
                result.append(number_list[x] - number_list[x+1])
            elif operator_list[x] == '*':
                result.append(number_list[x] * number_list[x+1])
            elif operator_list[x] == '/':
                result.append(number_list[x] / number_list[x+1])
            elif operator_list[x] == '%':
                result.append(number_list[x] % number_list[x+1])

    except ZeroDivisionError:
        print('Error: Zero Division')
    except IndexError:
        print('Error: Index Out of Range')
    except:
        print('Error: Unknown Error')
    
    return result

if __name__ == '__main__':
    str_param = input('> ') # input string

    operator_list = parse_op_from_str(str_param)
    number_list = parse_num_from_str(str_param)
    print(number_list)
    result = process_op_and_num(operator_list, number_list)

    print(str_param, '=', result)
