import requests
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.request import urlretrieve
from urllib.request import *
import os


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

counter = 1
no = 0
com = 1

#url = "https://comic.naver.com/webtoon/detail.nhn?titleId=" + str(titleId) + "&no=" + str(no) + "&weekday=" + weekday

def get_html(url):
    #r = requests.get(url)
    #return r.text
    r = Request(url)
    html = urlopen(r).read()
    return html

#def get_html1(url):
    #r = requests.get(url)
    #return r.text 

def get_html_links(html):
    soup = BeautifulSoup(html, 'lxml')    
    tds = soup.find('ul', id='_listUl').find_all('li')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        print (a)
        links.append(a) 
        
    return links



def get_chapter_links(url):
    page = urlopen(url)
    soup = BeautifulSoup(page.read(), 'html.parser')       
    tds = soup.find('ul', id='_listUl').find_all('li')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        #print (a)
        links.append(a) 
        
    return links

def save_data(name, file_data):
    file = open(name, 'bw') #Binary mode, the image is transmitted by bytes
    for chunk in file_data.iter_content(4096): #We write data to the file block by block
        file.write(chunk)
    file.close()    
        
def download(name, file_object):  
    with open("pic/" + url + ".jpg", 'wb') as out:
    #with open(name, 'wb') as out:
        for chunk in file_object.iter_content(8192):
            out.write(chunk)
    out.close()     


def get_in_links(url):
    page = urlopen(url)
    soup = BeautifulSoup(page.read(), 'html.parser')   
    tds = soup.find('div', id='_viewerBox').find_all('div')
    print (tds) #Takes what you need. Remains to cut out the excess
    links = []
    for td in tds:
        a = td.get('src')
        print (a)
        links.append(a) 
        
    return links    

def get_img_links(url):
    counter = 1
    print (url)
    page = urlopen(url)
    soup = BeautifulSoup(page.read(), 'html.parser')  
    
    print(soup)
    #imgUrls = soup.find('div', id='_imageList').find_all('img', class_='_images')
    imgUrls = soup.findAll('img')#, class_='_images')#('div', id='_imageList')
    
    
    for a in imgUrls:
        
         img = a['src']  
         if not (img.find('pstatic' or 'PNG')):
                 print(img)
                 
         if (img.find('webtoon' and '_JPEG') != -1) and (img.find('thumb' and 'mobile' and 'transparency') == -1):
            name = "pic/" + str(no) + "_" + str(counter) + ".jpg" 
             
            #save_data(name, img)
            try:
                urllib.request.urlretrieve(img, name)
                counter = 1     
                print (img) 
            #request=urllib.request.Request(img,None,headers) #The assembled request
            #response = urllib.request.urlopen(request)
            #data = response.read()    
            
            #out = open(name,'wb')
            #out.write(data)
            #counter += 1
            #out.close()
            except:
                print ('Page not found')    
        
    #imgs = imgUrls.find(class_='_images')['src']
    #print (imgs)
    #print('\n')
    #links = []
    #for image in imgUrls:
        #try:            
            #imgUrl = image['src']
            #if(imgUrl.find('webtoon') != -1):
                #f = open('images_links.txt', 'w')
                #f.write(imgUrl+"\n")
                ##a = td.get('src')
                #print (imgUrl)
                #links.append(imgUrl)  
                
                #request=urllib.request.Request(imgUrl,None,headers) #The assembled request
                #response = urllib.request.urlopen(request)
                #data = response.read() # The data u need 
            
                #out = open("pic/" + image + ".jpg", 'wb')
                #out.write(data)
                #out.close()   
                    
                #f.close()                
        #except:
            #pass
             
    return img#links    
    
def get_file(url):
    r = requests.get(url, stream=True)
    return r

def get_name(url):
    name = url.split('/')[-1]
    return name


    
def img_download(imgUrl):
    request=urllib.request.Request(imgUrl,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need 

    out = open("pic/" + url + ".jpg", 'wb')
    out.write(data)
    out.close()    
    
def main():
    no = 0
    com = 1
    counter = 1
    with open('comic-link-list.txt', 'r') as stf: #as start file
        comics = stf.read().splitlines()
    print(comics) 
    
    for i in comics:
        all_chapters = get_chapter_links(i)       
        for j in all_chapters:  
            
            all_img = get_in_links(j)#get_img_links(j)
            no += 1
            #for k in all_img:
                ##download(get_name(k), get_file(k))
                #print(k + '\n')
                ##download(k, get_file(k))
                #img_download(k)
        com += 1
        no = 1
        counter = 1
        
if __name__ == '__main__':       
    main()
    
