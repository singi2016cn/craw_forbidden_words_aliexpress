from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from lxml import etree
from tqdm import trange
import json
import tools
import write_sql
import platform
import config


words_path = config.words_path # 文本保存路径

# chromedriver驱动
executable_path = config.chromedriver_win
if(platform.system() == "Linux"):
    executable_path = config.chromedriver_linux

res = [] # 最终结果]
table_row = 51

options = Options()
options.add_argument('--headless')
dr = webdriver.Chrome(executable_path=executable_path, options=options)

dr.get(config.data_page)
sleep(1)


htmlSource = dr.page_source
html = etree.HTML(htmlSource)

print('爬取服饰鞋包手表配饰')
for i in trange(21):
    table_number1 = i + 1
    xpathReg = '/html/body/div[2]/div/div/div[1]/div[2]/span/span/table[%d]' % (table_number1)
    xpathReg += '/tbody/tr[%d]//text()'
    res += tools.pageData(html, xpathReg, table_row, table_number1)

jsonData = json.dumps(res)
with open(words_path, "w") as f:
    f.write(jsonData)

print('爬取数据完成')

print('开始写入数据库')
write_sql.write_into_db(words_path, 1)
print('写入数据库完成')


res = []
print('运动娱乐休闲')
for i in trange(1):
    xpath_table_pre = '/html/body/div[2]/div/div/div[3]/span/span/table/tbody'
    total = tools.get_table_row_count(dr, xpath_table_pre)
    xpathReg = xpath_table_pre + '/tr[%d]//text()'
    res += tools.pageData(html, xpathReg, total + 1, 1)

jsonData = json.dumps(res)
with open(words_path, "w") as f:
    f.write(jsonData)

print('爬取数据完成')

print('开始写入数据库')
write_sql.write_into_db(words_path, 3)
print('写入数据库完成')


res = []
print('家电')
for i in trange(1):
    xpath_table_pre = '/html/body/div[2]/div/div/div[7]/span/span/table/tbody'
    total = tools.get_table_row_count(dr, xpath_table_pre)
    xpathReg = xpath_table_pre + '/tr[%d]//text()'
    res += tools.pageData(html, xpathReg, total + 1, 1)

jsonData = json.dumps(res)
with open(words_path, "w") as f:
    f.write(jsonData)

print('爬取数据完成')

print('开始写入数据库')
write_sql.write_into_db(words_path, 5)
print('写入数据库完成')


res = []
print('美容健康')
for i in trange(1):
    xpath_table_pre = '/html/body/div[2]/div/div/div[9]/span/span/table/tbody'
    total = tools.get_table_row_count(dr, xpath_table_pre)
    xpathReg = xpath_table_pre + '/tr[%d]//text()'
    res += tools.pageData(html, xpathReg, total + 1, 1)

jsonData = json.dumps(res)
with open(words_path, "w") as f:
    f.write(jsonData)

print('爬取数据完成')

print('开始写入数据库')
write_sql.write_into_db(words_path, 6)
print('写入数据库完成')


res = []
print('礼品玩具')
for i in trange(1):
    xpath_table_pre = '/html/body/div[2]/div/div/div[11]/span/span/table/tbody'
    total = tools.get_table_row_count(dr, xpath_table_pre)
    xpathReg = xpath_table_pre + '/tr[%d]//text()'
    res += tools.pageData(html, xpathReg, total + 1, 1)

jsonData = json.dumps(res)
with open(words_path, "w") as f:
    f.write(jsonData)

print('爬取数据完成')

print('开始写入数据库')
write_sql.write_into_db(words_path, 7)
print('写入数据库完成')


res = []
print('交通工具配件等')
for i in trange(1):
    xpath_table_pre = '/html/body/div[2]/div/div/div[13]/span/span/table/tbody'
    total = tools.get_table_row_count(dr, xpath_table_pre)
    xpathReg = xpath_table_pre + '/tr[%d]//text()'
    res += tools.pageData(html, xpathReg, total + 1, 1)

jsonData = json.dumps(res)
with open(words_path, "w") as f:
    f.write(jsonData)

print('爬取数据完成')

print('开始写入数据库')
write_sql.write_into_db(words_path, 8)
print('写入数据库完成')


dr.quit()
