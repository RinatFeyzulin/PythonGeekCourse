# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# os.path.exists(path)

from genericpath import exists


def rle_encode(data:str):
    if data=='': return 'error none char'
    char_data = ''.join(data)
    current_char=char_data[0]
    result=''
    count=0
    for x in char_data:
        if current_char==x:
            count+=1
        else:
            result+=f'{count}{current_char}'
            current_char=x
            count=1
    result+=f'{count}{current_char}'
    # print(result)
    return result

def rle_decode(code):
    if code=='': return 'error none code'
    data =''.join(code)
    result=''
    count=''
    for i in data:
        if i.isdigit():
            count = i
        else:
            result+=i*int(count)
    return(result)

def save_encode(file_txt,file_code):
    if exists(file_txt) and exists(file_code): 
        with open(file_txt, 'r') as data, \
                open(file_code, 'w') as encode:
            codetxt=rle_encode(data.readlines())
            encode.write(codetxt)
    else: print('path does not exist')

def decode_file(file):
    if exists(file):
        with open(file,'r') as data:
            result=rle_decode(data.readlines())
        print(result)
        return result
    else: print(f'file <{file}> path does not exist ')

f_text=input('Enter the name of the file with the text:')
f_record=input('Enter the file name to record:')
f_decode=input('Enter the name of the file to decode:')

decode_file(f_decode)
save_encode(f_text,f_decode)


