# x_1_2
#
# 「input()」で入力している箇所を「teinei_input()」で入力するように修正してください

def teinei_input(string):
    return input('お忙しいところ誠に申し訳ございませんが、' + string)


name = teinei_input('あなたの名前を入力してください:')
print('私の名前は' + name + 'です')

food = teinei_input('好きな食べ物を入力してください:')
print('好きな食べ物は' + food + 'です')
