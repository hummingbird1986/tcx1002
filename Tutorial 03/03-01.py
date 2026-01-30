import re
import string
def find_valid_plates(text):
    result, prefix_number=[],[]
    match = r'\b([A-Z]{1,3})\s*([0-9]{1,4})\s*([A-Z]{1})\b'
    result = re.findall(match, text, re.IGNORECASE)
    # print('result: ',result)
    prefix_number=get_alphabet_mapping(result)
    postfix_number=get_number_mapping(result)
    whole_number=[]
    for i in range(len(result)):
        whole_number.append(prefix_number[i][1]+postfix_number[i])

    # print('prefix_number: ',prefix_number)
    # print('postfix_number: ',postfix_number)
    # print(whole_number)
    # test_number_=0
    # checksum_=''
    valid_car_num=[]
    for j in range(len(result)) :
        test_number_=check_sum_weights(whole_number[j])
        checksum_=checksum_letter(test_number_)
        # print(checksum_)
        if checksum_==result[j][2]:
            # print(prefix_number[j][0])
            # print(result[j][1])
            valid_car_num.append(result[j][0].upper()+result[j][1]+result[j][2])
    return valid_car_num
            # print("true car number: ',postfix_number[0]+result[j][1])




def get_alphabet_mapping(car_number_alpha):
    alpha_to_number= {letter: i+1 for i, letter in enumerate(string.ascii_uppercase)} #dictrionary
    prefix_num_lst=[]
    for i in range(len(car_number_alpha)):
        alpha = car_number_alpha[i][0]
        if alpha.isalpha():
             if len(alpha) == 1:
                 alpha='00'+alpha.upper()
             elif len(alpha) == 2:
                 alpha='0'+alpha.upper()
             else:
                 alpha=alpha.upper()
             alpha_to_number_list = []
             for j in range(1,len(alpha)):
                alpha_to_number_list.append(alpha_to_number[alpha[j]])
                prefix_number_=(alpha,alpha_to_number_list)
             prefix_num_lst.append(prefix_number_)
    return prefix_num_lst


def get_number_mapping(car_number_number):
    postfix_num_lst=[]
    for i in range(len(car_number_number)):
        number_=car_number_number[i][1]
        number_list_=[]
        if number_.isdigit():
             for j in number_:
                 number_list_.append(int(j))
             if len(number_list_) == 1:
                 number_list_ = [0, 0, 0] + number_list_
             elif len(number_list_) == 2:
                 number_list_ = [0, 0] + number_list_
             elif len(number_list_) == 3:
                 number_list_ = [0] + number_list_
             else:
                 pass
             postfix_num_lst.append(number_list_)

    return postfix_num_lst
# mapping=get_alphabet_mapping()
# print(mapping['Z'])

def check_sum_weights(car_whole_number):
    weights = (9, 4, 5, 4, 3, 2)
    number_=0
    for i in range(len(car_whole_number)):
        number_+=car_whole_number[i]*weights[i]
    return number_


def checksum_letter(check_sum_num):
    i=check_sum_num%19
    checksum='AZYXUTSRPMLKJHGEDCB'
    return checksum[i]

print(find_valid_plates('Meet at carpark with plates: SGP1234A, sL 0123 Z, Gbf307K and S-12 A SG 5443K'))
