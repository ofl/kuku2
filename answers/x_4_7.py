# x_4_7
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

hello = 'Hello World'

print(hello.upper())
print(hello.lower())
print(hello.title())
print(hello.swapcase())


class MyStr(str):
    def upper(self):
        return '<大文字にします>' + super().upper()

    def lower(self):
        return '<小文字にします>' + super().lower()

    def title(self):
        return '<題名っぽくします>' + super().title()

    def swapcase(self):
        return '<大文字と小文字を反転させます>' + super().swapcase()


sneaker_brands = MyStr('adidas Nike PUMA')

a = sneaker_brands.upper()
b = sneaker_brands.lower()
c = sneaker_brands.title()
d = sneaker_brands.swapcase()

print(a)  # => <大文字にします>ADIDAS NIKE PUMA (super().upper()で上書き前の結果を追加した)
print(b)  # => <小文字にします>adidas nike puma (super().lower()で上書き前の結果を追加した)
print(c)  # => <題名っぽくします>Adidas Nike Puma (super().title()で上書き前の結果を追加した)
print(d)  # => <大文字と小文字を反転させます>ADIDAS nIKE puma (super().swapcase()で上書き前の結果を追加した)
