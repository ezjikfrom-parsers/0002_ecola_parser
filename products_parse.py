# -*- coding: utf-8 -*-
'''
Created on 13.08.2020

@author: Sergey
'''

from bs4 import BeautifulSoup;
import requests;

url = 'http://svetonik.ru/site/50270/';


#func to take SOUP (html of page for bs4) to parse data
def take_soup(url):
    page = requests.get(url);
    soup = BeautifulSoup(page.text, "html.parser");
    return soup;

#func to take all links of products on page
def take_links_from_page(soup):
    lis = soup.find_all('a', class_='nameofgood');
    list_of_orders = [];
    if lis == []:
        lis = soup.find_all('div', class_='bx_catalog_item_title');
        for x in lis:
            a = x.find('a');
            link = a['href'];
            #link_category = 'http://svetonik.ru'#+names_cat.a['href'];
            list_of_orders.append('http://svetonik.ru'+link);
    
    else:
        for a in lis:
            #a = x.find('a');
            link = a['href'];
            #link_category = 'http://svetonik.ru'#+names_cat.a['href'];
            list_of_orders.append('http://svetonik.ru'+link);
    #print(list_of_categories);


    return list_of_orders

#we take all pages
def pagination(url_first):
    pass
    
    
def take_data_of_product(soup):
    #1. take title of product:
    title = soup.find('div', class_='bx_item_title');
    try:
        title = title.span.text;
    except AttributeError:
        #print("Mistake in one. Don't worry we just find empty product. We will go to next");
        return '';
    
    #2. take prise:
    price = soup.find('div', class_='item_price');
    oldPrice = price.find('div',class_ = 'item_old_price').text;
    realPrice = price.find('div' , class_ = 'item_current_price').text;
    discauntPrice = price.find('div' , class_ = 'item_economy_price').text;
    
    #del ' руб.':
    oldPrice = oldPrice[:-5];
    realPrice = realPrice[:-5];
    discauntPrice = discauntPrice[:-5];
    
    realPrice = realPrice.replace(' ', '');
    #print(realPrice);
    try:
        prise_minus_5 = str(int(realPrice)*0.95);
    except ValueError:
        prise_minus_5 = '';
    
    #3. take photo:
    photo = soup.find('div', class_='bx_bigimages_imgcontainer');
    photo = 'http://svetonik.ru' + photo.img['src'];
    
    #4. take params:
    params = soup.find('div', class_='item_info_section');
    
    names = params.find_all('dt');
    info = params.find_all('dd');
    
        #take only data from tags
    listParamsNames = [];
    listParamsInfo = [];
    
    for i in names:
        listParamsNames.append(i.text);
    for i in info:
        listParamsInfo.append(i.text);
    #print(listParamsNames);
    
    dict_params = dict(zip(listParamsNames, listParamsInfo));
    
    
    
    params = ['Артикул', 'Цвет', 'Мощность (Ватт)', 'Напряжение (Вольт)', 'Цветовая температура (К)', 
     'Срок службы (Час)', 'Размеры мм (длина * толщина)', 'Модель','Цоколь'];
    listParamsInfo = []
    #write list of params:
    for param in params:
        if param in dict_params:
            #print(dict_params);
            listParamsInfo.append(dict_params[param]);
        else:
            listParamsInfo.append('');
    #find new params:
    for param in dict_params:
        if param not in params:
            print('\nwe have not param',param);
            print(param)
    
    #5. take description:
    descr = soup.find('section', id='content1');
    descrAll = descr.find_all('span');
    
    #6. take category (from breadcrumbs):
    category = soup.find('div', class_='cm_breadcrumbs');
    main_category = category.find('span').text;
    #print('Главная категория товара:', main_category);
    #print(title);
    
    '''#Каталог/С[ветильники/Светодиодные светильники
    one = ['Встраиваемые точечные светильники','Накладные светильники','Светодиодные панели и комплектующие к ним','Гирлянды',
           'Светодиодные даунлайты','Светодиодные линейные светильники'];
    #Каталог/Источники света/Лампы светодиодные
    two = ['Лампы для встраиваемых и накладных светильников','Накладные светильники','Лампы для встраиваемых и накладных светильников',
           'Лампы-свечи','Лампы-шарики, шары и груши','Рефлекторы "на винте"','Лампы 300-360° и кукурузы','Маленькие лампы для холодильника и шв. машинки',
           'Линейные лампы Т8','Лампы для хрустальных люстр','Золотистые лампы'
           'Лампы серии Ecola Premium','Цветные лампы','Мощные LED лампы','Лампы для диммера'];
    #Каталог/Источники света/Лампы накаливания
    three = ['Нитевидные лампы (Filament)'];
    #Каталог/Источники света/Лампы энергосберегающие
    four = ['Традиционные энергосберегающие (КЛЛ) лампы']
    #Каталог/Светильники/Прожекторы
    fife = ['Светодиодные даунлайты'];
    #Каталог/Источники света/Лента светодиодная
    six = ['Светодиодная лента и всё для светодиодной ленты'];

    if main_category in one:
        main_category = 'Каталог/Светильники/Светодиодные светильники';
    elif main_category in two:
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category in three:
        main_category = 'Каталог/Источники света/Лампы накаливания';
    elif main_category in four:
        main_category = 'Каталог/Источники света/Лампы энергосберегающие';
    elif main_category in four:
        main_category = 'Каталог/Светильники/Прожекторы';
    elif main_category in four:
        main_category = 'Каталог/Источники света/Лента светодиодная';'''
    if main_category == 'Светильники GX53 с LED подсветкой':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Встраиваемые/Круглые/С подсветкой';
    elif main_category == 'Светильники MR16 с LED подсветкой':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Встраиваемые/Круглые/С подсветкой';
    elif main_category == 'Квадратные и овальные светильники GX53':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Встраиваемые/Квадратные';
    elif main_category == 'Встраиваемые точечные светильники':
        main_category = 'остальные из этой категории Каталог/Светильники/Светодиодные светильники/Встраиваемые/Круглые';
    elif main_category == 'Накладные светильники':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Накладные';
    elif main_category == 'Лампы-свечи':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Лампы-шарики, шары и груши':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Лампы для встраиваемых и накладных светильников':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Рефлекторы "на винте"':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Лампы 300-360° и кукурузы':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Маленькие лампы для холодильника и шв. машинки':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Линейные лампы Т8':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Золотистые лампы':
        main_category = 'Каталог/Источники света/Лампы декоративные, лофт';
    elif main_category == 'Лампы серии Ecola Premium':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Мощные LED лампы':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Цветные лампы':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Традиционные энергосберегающие (КЛЛ) лампы':
        main_category = 'Каталог/Источники света/Лампы энергосберегающие';
    elif main_category == 'Лампы для диммера':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Светодиодные панели и комплектующие к ним':
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category == 'Прожекторы и лампы для прожекторов':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Прожекторы';
    elif main_category == 'Встраиваемые квадратные':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Встраиваемые/Квадратные';
    elif main_category == 'Встраиваемые круглые':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Встраиваемые/Круглые';
    elif main_category == 'Накладные квадратные':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Встраиваемые/Квадратные';      
    elif main_category == 'Накладные круглые':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Встраиваемые/Круглые';      
    elif main_category == 'Светодиодные линейные светильники':
        main_category = 'Каталог/Светильники/Светодиодные светильники/Накладные';
    elif main_category == 'Светодиодная лента и всё для светодиодной ленты':
        main_category = 'Каталог/Источники света/Светодиодная лента';
    elif main_category == 'Патроны':
        main_category = 'Каталог/Электроустановочные изделия и аксессуары/Патроны';       
    elif main_category == 'Переходники, разветвители и патроны':
        main_category = 'Каталог/Электроустановочные изделия и аксессуары/Переходники';         
        
    
    #print('Главная категория товара:', main_category);
    all = '';
    for i in descrAll:
        all = all + i.text;
    
    #print('Параметры:',listParamsInfo);
    return {'main_category':main_category,'title':title,'prise_minus_5':prise_minus_5, 'oldPrice':oldPrice,'realPrice':realPrice,'discauntPrice':discauntPrice, 'photo':photo,'listParamsNames':listParamsNames,'listParamsInfo':listParamsInfo,'alltext':all};

if __name__ == '__main__':
    url = 'http://svetonik.ru/site/50270/9495476.php';
    soup = take_soup(url);
    #take_links_from_page(soup);
    
    ans = take_data_of_product(soup)
    #print(ans);