import sys
import urllib
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
#import wget
from urllib.request import urlretrieve

#create/open a file
start_file = open('comic-link-list.txt', 'w')
titleId = 702672
weekday = "sat"
f = open("images_links.txt", 'w')
counter = 1

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

for no in range (191, 194): 

  #open comic.naver.com url
    url = "https://comic.naver.com/webtoon/detail.nhn?titleId=" + str(titleId) + "&no=" + str(no) + "&weekday=" + weekday
    page = urlopen(url)

#get comic page from page
    soup = BeautifulSoup(page.read(), "html.parser")
  
#Find all images in the file, put them in imgUrls 
    imgUrls = soup.findAll('img')
    imagesDict = {}

# download all images
    for image in imgUrls:
        try:
        #get src tag and download file, save link and local link in dict
            imgUrl = image['src']
            if (imgUrl.find('/webtoon/' and '_IMAG') != -1) and (imgUrl.find('thumb') == -1):
                
                print(imgUrl)
                f.write(imgUrl+"\n")

                #wget.download(url)

                request=urllib.request.Request(imgUrl,None,headers) #The assembled request
                response = urllib.request.urlopen(request)
                data = response.read() # The data u need 
                
                out = open("pic/" + str(no) + "_" + str(counter) + ".jpg", 'wb')
                out.write(data)
                out.close()
                 
                counter += 1
        except:
            pass

    counter = 1 
    
f.close()
start_file.close()