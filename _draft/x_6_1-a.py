# 6の段「エラーと例外処理 ~ 1」
#
# エラーが起こった場合に「リストの範囲外です」と表示させてください

try:
    'あ' + 1
except:
    print('型の違いによるエラーが発生しました')

members = ['桃太郎', 'いぬ', 'さる', 'きじ']
members[5]

print('リストの範囲外です')
