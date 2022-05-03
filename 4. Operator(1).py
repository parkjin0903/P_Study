money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = int(input("exchange"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n 500won => %d" % c500)
print("100won => %d " %c100)
print("50won => %d" %c50)
print("10won => %d" %c10)
print("exchange => %d" %money)
