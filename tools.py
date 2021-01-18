def pageData(html, xpathReg, table_row, table_number):
    res = []
    index = 1
    if table_number == 1:
        index = 2
    for i in range(index, table_row):
        xpathStr = xpathReg % i
        word = html.xpath(xpathStr)
        if len(word) == 0:
            break
        res.append(word[1].strip())
        res.append(word[3].strip())
    return res

def words_format(words):
    res = ''
    if words.find('&') != -1:
        res = words.replace(' ', '')
    else:
        res = ' '.join(words.split())
        res = res.replace(' ', '&')
    return res