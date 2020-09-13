# -*- coding: utf-8 -*-
'''
Created on 13.08.2020

@author: Sergey
'''
from bs4 import BeautifulSoup;
import requests;

url = 'http://svetonik.ru/site';
dict = {};

#func to take SOUP (html of page for bs4) to parse data
def take_soup(url):
    page = requests.get(url);
    soup = BeautifulSoup(page.text, "html.parser");
    return soup;

#func to take all names and links of categories on page
def take_links_from_page(soup, url):
    lis = soup.find('ul', class_='bx_catalog_tile_ul');
    list_of_categories = [];
    try:
        names_cat = lis.find_all('span');
    except AttributeError:
        return ['products',url];
    #link_cat = lis.find_all('a')
    
    for x in names_cat:
        name_category = x.a.text;
        link_category = 'http://svetonik.ru'+x.a['href'];
        list_of_categories.append([name_category,link_category]);


    return list_of_categories

#we add all categories and links in dict:
def add_to_list(list_of_categories, level,parentsCategory,lastCategory):
    levelInDict = 'lev' + str(level);
    dict = {};
    
    for i in range(1, len(list_of_categories)):
        numberInDict = 'number'+ str(i);
        #print('Уровень', levelInDict);
        #print('Порядковый номер', numberInDict);
        #Write name category and link in dict with name consist level-number
        dict[levelInDict + '-' + numberInDict + '-' + parentsCategory] = [list_of_categories[i][0], list_of_categories[i][1], lastCategory];
        #print(dict);
        

    return dict;


if __name__ == '__main__':
    
    #we take all categories and link
    soup = take_soup(url);
    list_of_categories = take_links_from_page(soup);
    level = 1;
    parentsCategory = "zeroCategory";
    lastCategory = 'Not last';
    dict = add_to_list(list_of_categories, level,parentsCategory, lastCategory);
    print(len(dict));
    print(dict);
    for data in dict:
        print(dict[data][0]);
        print(dict[data][1]);
        
'''
    #take second level
    try:
        for level1 in dict:
            if parentsCategory in level1:
                #take link from list of data
                url = dict[level1][1];
                soup = take_soup(url);
                list_of_categories = take_links_from_page(soup);
                level = 2;
                parentsCategory = "main";
                lastCategory = 'Not last';
                dict2 = add_to_list(list_of_categories, level,parentsCategory, lastCategory);
                print(dict2);
    except RuntimeError:
        print('Mistake in ', level1, url);
    dict.update(dict2);
    print(len(dict));
    print(dict);
    
    
    #for i in range(1,len(dict[level1]) + 1):
        #print(i);'''