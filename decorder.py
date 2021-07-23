
dict_morse_4 = {'1010': 'c', '0010': 'f', '0000': 'h', '0111': 'j', '0100': 'l', '0110': 'p', '1101': 'q', '0001': 'v',
                '1001': 'x', '1011': 'y', '1100': 'z'} #11

dict_morse_3 = {'100': 'd', '110': 'g', '101': 'k', '111': 'o', '010': 'r', '000': 's', '001': 'u', '011': 'w'} #9

dict_morse_2 = {'01': 'a', '00': 'i', '11': 'm', '10': 'n'} #4

dict_morse_1 = {'0': 'e', '1': 't'}

arr_dict_morse = [dict_morse_1, dict_morse_2, dict_morse_3, dict_morse_4]

arrAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', ]
arrMorse = ['01', '100', '1010', '100', '0', '0010', '110', '0000', '00', '0111', '101', '0100', '11', '10', '111',
            '0110', '1101', '010', '000', '1', '001', '0001', '011', '1001', '1011', '1100']




strText = "Ryusei takagi"

def encodeMor(strText):
    strLower = strText.lower()
    arrCapital = []

    for i in range(len(strText)):
        if strText[i] == strLower[i]:
            arrCapital.append('0')
        else:
            arrCapital.append('1')

    strMorse = []
    for i in strLower:
        index = 0
        for j in arrAlphabet:

            if i == j:
                strMorse.append(arrMorse[index])
                index += 1

            elif i == ' ':
                strMorse.append("/")  # Whatever symbol you want for space at arrMose[26]
                index += 1
                break
            else:
                index += 1
    return strMorse, arrCapital



def decodeMor(s, k):
    m = " "
    for i in range(len(s)):
        if s[i] == "/":
            m += " "
            continue
        for j in range(len(arrMorse)):
            if s[i] == arrMorse[j]:
                if k[i] == "0":
                    m += arrAlphabet[j].lower()
                else:
                    m += arrAlphabet[j].upper()
                break

    return m


def get_swap_dict(d):
    return {v: k for k, v in d.items()}


def cut_morse(morse_str):
    index = 0
    result = ""
    while index <= len(morse_str):
        for i in range(3, -1, -1):
            if morse_str[index] not in ["0", "1"]:
                index+=1
                break
            if morse_str[index: index+i+1] in arr_dict_morse[i]:
                result += arr_dict_morse[i][morse_str[index: index+i+1]]
                print(result)
                index += i + 1
                break

    return result

if __name__ == "__main__":
    a, b = encodeMor(strText)
    print(a)
    print(decodeMor(a, b))
