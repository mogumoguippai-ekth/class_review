from inspect import AGEN_CLOSED


class Customer:  # クラス名Customer
    # 各問のコードが期待通り動作するように実装
    # pass …将来実装する予定の空の処理
    def __init__(self, first_name, family_name, age):  # 顧客情報を初期化
        self.first_name = first_name     # インスタンス変数first_nameの初期化
        self.family_name = family_name   # インスタンス変数family_nameの初期化
        self.age = age                   # インスタンス変数ageの初期化


    def full_name(self):  # フルネームを取得する
        return f"{self.first_name} {self.family_name}"  # f記法で「first_name family_name」を取得する


    def entry_fee(self):  # 入場料を設定する
        if self.age <= 3:           # C-5 幼児無料(3歳以下)
            return 0
        elif 4 < self.age < 20:     # こども料金(4歳以上20歳未満)
            return 1000
        elif 20 <= self.age < 65:   # おとな料金(20歳以上65歳未満)
            return 1500
        else:                       # シニア料金(65歳以上)
            return 1200


    def info_csv(self):  # 顧客情報をCSV形式で取得する
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

# インスタンス
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)  # 応用編追加

# 以降で各問のコードを追加していく
# C-1. フルネームを取得できる
print(ken.full_name())
print(tom.full_name())
print(ieyasu.full_name())


# C-2. 年齢という概念の追加
print(ken.age)
print(tom.age)
print(ieyasu.age)


# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee())



# C-4. 単一の顧客情報をCSV形式で取得できる
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())


# C-5.3歳以下の入場料金の無料化
print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee())
print(michelle.entry_fee())
