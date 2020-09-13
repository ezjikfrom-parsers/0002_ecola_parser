# -*- coding: utf-8 -*-
'''
Created on 26.08.2020

@author: Sergey
'''

import csv
#for write pic:
import requests


def readCsv(csvName):
    with open(csvName, 'r', newline="", encoding='utf-8') as file:
        list = [];
        reader = csv.reader(file, delimiter=';');
        for row in reader:
            list.append(row);
        #print('ÐŸÐ¾Ð»ÑƒÑ‡Ð¸Ð»Ð¸ Ð»Ð¸Ñ�Ñ‚:',list);
    return(list);

if __name__ == '__main__':
    ans = readCsv('D:\Programming\Python\Eclipse\Parser_ecola\src\\result\\all-2020-8-20.csv');
    for one in ans:
        #print(one)
        #print(one[6])
        try:
            p = requests.get(one[6]);
            print(one[6]);
            break
        except:
            continue;
        out = open("{}".format(one[6]), "wb")
        out.write(p.content)
        out.close()
        
