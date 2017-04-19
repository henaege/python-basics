sub_total = float(raw_input("How much is the bill? "))
service = raw_input("How was the service (good, fair, or bad)? ")
split = int(raw_input("Split how many ways? "))
if service == "good":
    tip = sub_total * 0.2
    total = sub_total + tip
    total_per_person = total / split
    print "Tip amount: ${:.2f} Total amount: ${:.2f} Total per person: ${:.2f}".format(tip, total, total_per_person)
elif service == "fair":
    tip = sub_total * 0.15
    total = sub_total + tip
    total_per_person = total / split
    print "Tip amount: ${:.2f} Total amount: ${:.2f} Total per person: ${:.2f}".format(tip, total, total_per_person)
elif service == "bad":
    tip = sub_total * 0.10
    total = sub_total + tip
    total_per_person = total / split
    print "Tip amount: ${:.2f} Total amount: ${:.2f} Total per person: ${:.2f}".format(tip, total, total_per_person)
else:
    print "Please enter a valid service level next time"
    
