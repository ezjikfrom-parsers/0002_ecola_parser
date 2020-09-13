# -*- coding: utf-8 -*-
'''
Created on 19.08.2020

@author: Sergey
'''

import products_parse;
import parseSvetonikLists;
import write_csv;
#play alert
import winsound
#храним инфо
import pickle;

def make_danse(soup,count):
    pass;

        
        

def find_all_products(list_of_product,list_of_categories):
    glob_list_of_categories = [];
    for link in list_of_categories: 
        #try:
        #print(link);
        soup = products_parse.take_soup(link[1]);
        list_of_categories2 = parseSvetonikLists.take_links_from_page(soup, link[1]);
        if list_of_categories2[0] == 'products':
            list_of_product.append(list_of_categories2[1])
        else:
            glob_list_of_categories = glob_list_of_categories + list_of_categories2;
        #except:
            #print('Mistake!!',list_of_categories);
            #continue;
    print('Количество разделов с товарами:',len(list_of_product));
    #print(list_of_product);
    return list_of_product,glob_list_of_categories;
    


if __name__ == '__main__':
    url = 'http://svetonik.ru/site/';
    #we take all categories and link
    soup = products_parse.take_soup(url);
    #in this var we place all link on products
    list_of_product = [];
    '''
    #level1
    print('level1');
    list_of_categories = parseSvetonikLists.take_links_from_page(soup, url);
    if list_of_categories[0] == 'products':
        list_of_product.append(list_of_categories[1]);
    #print('Количество разделов с товарами:\n',len(list_of_product));
    #print(list_of_product);
    #print('\n');
    #level2
    print('level2');
    #print('Категорий для парсинга:\n',len(list_of_categories));
    #print('Категории для парсинга:\n',list_of_categories);
    #print('\n');
    list_of_product,list_of_categories2 = find_all_products(list_of_product,list_of_categories);
    print('\n');
    #level3
    print('level3');
    #print('Категорий для парсинга:\n',len(list_of_categories2));
    print('Категории для парсинга:\n',list_of_categories2);
    #print('\n');
    list_of_product,list_of_categories3 = find_all_products(list_of_product,list_of_categories2);
    #print('\n');
    #level4
    print('level4');
    #print('Категорий для парсинга:\n',len(list_of_categories3));
    print('Категории для парсинга:\n',list_of_categories3);
    #print('\n');
    list_of_product,list_of_categories4 = find_all_products(list_of_product,list_of_categories3);
    #print('\n');
    #level5
    print('level5');
    #print('Категорий для парсинга:\n',len(list_of_categories4));
    print('Категории для парсинга:\n',list_of_categories4);
    #print('\n');
    list_of_product,list_of_categories5 = find_all_products(list_of_product,list_of_categories4);
    #print('\n');
    #level6
    #print('level6');
    #print('Категорий для парсинга:\n',len(list_of_categories5));
    #print('Категории для парсинга:\n',list_of_categories5);
    #print('\n');
    #list_of_product,list_of_categories6 = find_all_products(list_of_product,list_of_categories5);
    #print('\n');
        
        
    winsound.Beep(500, 200);
    
    #write Titles:
    
    #write products:
    
    #for title one time write
    
    print(len(list_of_product));
    
    with open('data.pickle', 'wb') as f:
        pickle.dump(list_of_product, f);
    
    print('We write pickle!!');
    
    '''
    
    count = 1;
    with open('data.pickle', 'rb') as f:
        list_of_product = pickle.load(f)
    
    list_of_all_products = [];
    for url in list_of_product:
        #print(url)
        soup = products_parse.take_soup(url);
        #take all products from list
        list_of_product_on_page = products_parse.take_links_from_page(soup);
        #print('Продуктов на странице', url, ',:', len(list_of_product_on_page))
        #print(list_of_product_on_page);
        for prod in list_of_product_on_page:
            try:
                #print(prod);
                soup = products_parse.take_soup(prod);
                ans = products_parse.take_data_of_product(soup); 
                #print('Пишем товар ' + ans);
                #write in csv
                #print(prod);
                #print('ans',ans);
                
                #if we hav't product we get '':
                if ans != '':
                    #write title only first time
                    if count < 2:
                        print('Пишем заголовок');
                        count += 1;
                        write_csv.write_title_csv(ans);
                        
                    else:
                        list_of_all_products.append(ans);
                        count += 1;
                        print(count);
            
            except:
                #print('Нет продукта на странице',prod);
                continue;
            '''if count > 5:
                break;            
        if count > 5:
            break;   '''         
    #clean dubles
    clean_ans = [];
    list_for_comparison = [];
    for v in list_of_all_products:
        if v['listParamsInfo'] not in list_for_comparison:
            list_for_comparison.append(v['listParamsInfo'])
            clean_ans.append(v);  
    #print(list_of_all_products)
    #write csv
    print('begin write')
    for z in clean_ans:
        #print(z);
        write_csv.write_dict_in_csv(z);
    print('---------------------All!----------------------');
    #play alert:
    winsound.Beep(500, 500);
    winsound.Beep(500, 500);
    