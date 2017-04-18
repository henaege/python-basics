sub_total = float(raw_input("How much is the bill? "))
service = raw_input("How was the service (good, fair, or bad)? ")
if service == "good":
    tip = sub_total * 0.2
    total = sub_total + tip
    print "Tip amount: ${:.2f} Total amount: ${:.2f}".format(tip, total)
elif service == "fair":
    tip = sub_total * 0.15
    total = sub_total + tip
    print "Tip amount: ${:.2f} Total amount: ${:.2f}".format(tip, total)
elif service == "bad":
    tip = sub_total * 0.10
    total = sub_total + tip
    print "Tip amount: ${:.2f} Total amount: ${:.2f}".format(tip, total)
else:
    print "Please enter a valid service level next time"
    
