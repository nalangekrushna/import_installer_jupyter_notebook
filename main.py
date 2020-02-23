import re
import ast
import json

data = ''
with open('test.ipynb') as f :
    data = f.read()
dic = json.loads(data)
print(dic.keys())
cells = dic['cells']
import_list = []
for cell in cells :
    if cell['cell_type'] == "code" :
        txt_list = cell['source']
        for txt in txt_list :
            if txt.startswith('from') :
                import_list.append(re.search('from \w+',txt).group(0).split()[1])
            elif txt.startswith('import') :
                import_list.append(re.search('import \w+',txt).group(0).split()[1])
print('package list to install '+str(import_list))
