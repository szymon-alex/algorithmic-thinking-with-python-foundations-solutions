def make_change(target_amount):
    coins = {200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
    # As of Python version 3.7, dictionaries are ordered.
    remained_amount = target_amount

    for coin, value in coins.items():
        coins_found=int(remained_amount / coin)
        if coins_found > 0:
            coins[coin]=coins_found
            remained_amount -= coin * coins_found 
            #print(f"remained_amount={remained_amount}")

    total_coins=0
    for coin, value in coins.items():
        total_coins += value

    return total_coins  # Write your solution here. 


print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p
print(make_change(666))
