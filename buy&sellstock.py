prices = [7,1,5,3,6,4]
n=len(prices)
def func(prices,n):
    buy_price=prices[0]
    profit=0
    for i in range(1,n):
        sell_price=prices[i]
        if sell_price>buy_price:
            profit=max(profit,(sell_price-buy_price))
        if buy_price>sell_price:
            buy_price=prices[i]
    return profit
print(func(prices,n))