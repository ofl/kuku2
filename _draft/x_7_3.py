# 7の段「正規表現 ~ 3」
#
# クレジットカードの番号を判定するコードを追加してください

import re

zipcode = input('郵便番号を入力してください(xxx-xxxx):')
zipcode_pattern = r'[0-9]{3}-[0-9]{4}'

if re.match(zipcode_pattern, zipcode):
    print('正しい郵便番号です')
else:
    print('不正な郵便番号です')

credit_card_number = input('クレジットカード番号を入力してください(xxxx-xxxx-xxxx-xxxx):')
