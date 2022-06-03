import datetime
from modules import *
import os, sys, shutil


def main():
    print('emaills: ', EMAIL_1, EMAIL_2)
    fnames = os.listdir('in_data')
    if fnames:
        for fname in fnames:
            log_data = 'start main ' + str(fnames)
            loger(log_data)
            flag_prefix = check_prefix(fname)
            if not flag_prefix:
                p_yellow('-> arhiv: ' + fname)
                continue
            process(fname)
            loger('\n')
        loger('finish main\n')


main()
