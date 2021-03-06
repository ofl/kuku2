# x_2_9
#
# 「2-8」のように関数の中で自分自身を呼び出すものを「再帰関数」といいます
# 再帰関数を使って全てのメンバーを１行づつ表示してください
# ヒント: リスト内の要素がリストでなければ「print()」で値を表示してリストであれば自身の関数を呼び出します

members = [
    ['桃太郎', 'いぬ', 'さる', 'きじ', ['赤鬼', '青鬼', '黄鬼']],
    ['くり', 'うす', 'はち', '牛糞', ['子がに1', '子がに2']],
    ['浦島太郎', 'かめ', '乙姫', 'たい', 'ひらめ', ['つる']],
]


def dig(members):  # 関数名は自由につけて良いのですがここでは掘り下げる(dig)という関数名にしました
    if type(members) == list:
        for member in members:
            dig(member)
    else:
        print(members)


dig(members)
