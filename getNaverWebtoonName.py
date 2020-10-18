from selenium import webdriver
import codecs
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get("https://comic.naver.com/webtoon/weekday.nhn")
driver.implicitly_wait(3)

text = driver.page_source

driver.quit()

p = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')

text_sp = text.split("\n")

file_p = codecs.open("Webtoon_list.txt", "w", 'UTF-8')

for i in text_sp:
    #print("[i] : " + str(i))
    match = p.search(i)
    if str(match) != "None":
        #print("[" + str(count) + "]Webtoon Name : " + match.string)
        if match.string.find('class=\"title\" title=') != -1:
            final_text = match.string.split(">")[1].split("<")[0]
            file_p.writelines(final_text + "\r\n")

file_p.close()

