coin_count = 0
want_more_coins = True
while want_more_coins:
    print "You have {} coins.".format(coin_count),
    coin_ask = raw_input("Do you want another? ")
    if coin_ask == "yes":
        coin_count += 1
    elif coin_ask == "no":
        print "Bye!"
        break
    else:
       print "Please type 'yes' or 'no'"