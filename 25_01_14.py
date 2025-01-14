# Input
cash = int(input())
stock_price = list(map(int, input().split()))
# Jun
jun_cash = cash
jun_stock = 0
# Sung
sung_cash = cash
sung_stock = 0
rise_cnt = 0
fall_cnt = 0
# Calculate
for i in range(len(stock_price)):
    #
    jun_stock += jun_cash // stock_price[i]
    jun_cash -= stock_price[i] * (jun_cash // stock_price[i])
    #
    if i == 0: pre_price=stock_price[0]
    if pre_price < stock_price[i]:
        rise_cnt +=1
    else:
        rise_cnt = 0
    if pre_price > stock_price[i]:
        fall_cnt +=1
    else:
        fall_cnt = 0
    #
    pre_price = stock_price[i]
    if fall_cnt >= 3:
        sung_stock += sung_cash // stock_price[i]
        sung_cash -= stock_price[i] * (sung_cash // stock_price[i])
    if rise_cnt >= 3:
        sung_cash += stock_price[i] * sung_stock
        sung_stock = 0
    if i == 13:
        jun = jun_cash + (jun_stock*stock_price[i])
        sung = sung_cash + (sung_stock*stock_price[i])
if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")



