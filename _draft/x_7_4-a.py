# x_7_4
#
#

import re

pattern = r'\d\d\d-\d\d\d\d'
str = input('郵便番号を入力してください(xxx-xxxx):')

if re.search(pattern, str):
    print('正しい郵便番号です')
else:
    print('不正な郵便番号です')
