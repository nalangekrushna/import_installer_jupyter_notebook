import re, sys, json, warnings, pkgutil
warnings.filterwarnings("ignore")

data = ''
with open('test.ipynb') as f :
    data = f.read()
dic = json.loads(data)
print(dic.keys())
cells = dic['cells']
import_set = set()
for cell in cells :
    if cell['cell_type'] == "code" :
        txt_list = cell['source']
        for txt in txt_list :
            if txt.startswith('from') :
                import_set.add(re.search('from \w+',txt).group(0).split()[1])
            elif txt.startswith('import') :
                import_set.add(re.search('import \w+',txt).group(0).split()[1])
print('package list to import '+str(import_set))

# alternative to below solution is this python library. stdlib-list
lib_set = set([ key.split('.')[0] for key in sys.modules if not key.startswith('_') ])
pkg_util_set = set([ i[1] for i in pkgutil.iter_modules(None) ])
lib_set = lib_set | pkg_util_set
install_set = import_set-lib_set
print('package list to install '+str(install_set))
