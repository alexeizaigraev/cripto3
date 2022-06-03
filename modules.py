import datetime
import os, sys
import shutil
from colorama import Fore, Style, init
#import gnupg

def alarm(s):
    loger(str(s))
    p_magenta(str(s))


def exec(s):
    loger('satart exec: ' + s)
    try:
        os.system(s)
        loger('success exec')
    except Exception as ex:
        alarm(str(ex))


def cod_string(fname, user1='', user2=''):
    loger('start cod_string')
    try:
        #s = 'gpg --output ' + OUT_DATA_PATH + nau().replace(" ", "_") + '_' + fname + '.gpg --encrypt --recipient ' + EMAIL_1 + ' --recipient ' + EMAIL_2 + ' ' + IN_DATA_PATH + fname
        s = 'gpg --output ' + OUT_DATA_PATH + fname + '.gpg --encrypt --recipient ' + EMAIL_1 + ' --recipient ' + EMAIL_2 + ' ' + IN_DATA_PATH + fname
        
        
        #s = f'gpg --output {OUT_DATA_PATH}{nau().replace(" ", "_")}_{fname}.gpg --encrypt --recipient {EMAIL_1} --recipient {EMAIL_2} {IN_DATA_PATH + fname}'
        loger(s)
        return s
    except Exception as ex:
        alarm(str(ex))

def say_yes():
    print('y')
    print('\n')


def cod_up(fname, user1='', user2=''):
    loger('start cod_up')
    s = cod_string(fname, user1, user2)
    loger('start cod_up - exec')
    exec(s)
    say_yes()
    p_dblue(fname)


def nau():
    return str(datetime.datetime.now())


def loger(log_data):
    #log_data = f'{log_data};{nau()}\n'
    text_add_file(log_data + '\n', 'logi.log')


def process(fname):
    try:
        user1 = EMAIL_1
        user2 = EMAIL_2
        log_data = 'start process: ' + fname + ' ' + user1 + ' ' + user2
        cod_up(fname, user1, user2)
        os.remove(IN_DATA_PATH + fname)
    except Exception as ex:
        alarm(str(ex) + ' ' + fname)


def put_to_out(fname):
    in_fname = IN_DATA_PATH + fname
    out_fname = OUT_DATA_PATH + fname
    try:
        #shutil.move(in_fname, out_fname)
        p_green('-> ' + out_fname)
        loger(out_fname)
    except Exception as ex:
        p_red(ex)
        p_magenta('err movie: ' + str(ex) + ' ' + in_fname)
        loger('err movie: ' + str(ex) + ' ' + in_fname)


def get_in_fnames():
    return os.listdir(IN_DATA_PATH)


def file_to_arr(path):
    """ Читает файл в массив. имя файла: path """
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            if ";" in line:
                b.append(line.strip().split(";"))
            else:
                b.append(line.strip())
    return b


def file_to_arr_nosharp(path):
    """ Читает файл в массив. имя файла: path """
    #sharp_nobom_file(path)
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            if ";" in line:
                b.append(line.strip().split(";"))
            else:
                b.append(line.strip())
    return b


def file_to_gen(path):
    """ Читает файл в массив. имя файла: path """
    #sharp_nobom_file(path)
    for line in open(path, 'r', encoding="UTF-8"):
        if ";" in line:
            b = line.strip().split(";")
        else:
            b = line.strip()
        yield b


def file_to_vec(path):
    """ Читает файл в массив. имя файла: path """
    #sharp_nobom_file(path)
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            b.append(line.strip())
    return b


def file_to_dict_one(fname, num_col):
    #sharp_nobom_file(fname)
    h = dict()
    with open(fname, 'r', encoding="UTF-8") as file:
        for line in file:
            split_line = line.strip().split(";")
            h[split_line[0]] = split_line[num_col]
    return h


def arr_to_text(arr):
    text = ''
    for v in arr:
        text += ';'.join(v) + "\n"
    return text


def file_to_text(fname):
    text = None
    with open(fname, 'r', encoding="UTF-8") as file:
        text = file.read()
    return text


def text_to_file(b, fname):
    """Записывает текст b в файл с именем fname"""

    with open(fname, 'w', encoding="UTF-8") as out_object:
        out_object.write(b)

    if b == '':
        p_magenta('emptty ' + fname)
    else:
        print(fname)


def text_add_file(b, fname):
    """Записывает текст b в файл с именем fname"""
    with open(fname, 'a', encoding="UTF-8") as out_object:
        out_object.write(b)

    if b == '':
        print('empty ' + fname)


def p_red(text):
    print(Fore.RED + str(text))

def p_green(text):
    print(Fore.GREEN + str(text))

def p_yellow(text):
    print(Fore.YELLOW + text)

def p_cyan(text):
    print(Fore.CYAN + str(text))

def p_magenta(text):
    print(Fore.MAGENTA + str(text))

def p_blue(text):
    print(Fore.LIGHTBLUE_EX + str(text))

def p_dblue(text):
    print(Fore.BLUE + str(text))

def has_prefix(s):
    for prefix in prefixes:
        if s.startswith(prefix):
            return True
    return False

def check_prefix(fname):
    if has_prefix(fname):
        return True
    os.rename(IN_DATA_PATH + fname, 'arhiv/' + nau().split(".")[-1] + '_' + fname)
    loger('move to arhiv ' + fname)
    return False

def check_indata():
    fnames = os.listdir(IN_DATA_PATH)
    if fnames:
        msg = 'not empty: ' + IN_DATA_PATH + ' :\n' + str(fnames)
        alarm(msg)


#color print__________________________________________
def say(t):
    p_blue(t)
def ssay(t):
    p_green(t)


#body_____________________

init()

prefixes = file_to_vec('config/prefix.txt')

config_data = file_to_dict_one('config/config.sys', 1)



IN_DATA_PATH = 'in_data/'
OUT_DATA_PATH = 'out_data/'
USER = config_data['user']

EMAIL_1 = config_data['email_1']
EMAIL_2 = config_data['email_2']

GNU_PG_HOME = '/home/' + USER + '/.gnupg'
