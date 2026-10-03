print("Welcoome to PayUp!")

event = input("What was the event/occasion? ")
cost = float(input("What was the cost? "))
service_charge = int(input("What was the service charge? ").strip("%"))
group_size = int(input("What was the size of your group? "))

service_charge_total = ((service_charge / 100) * cost)
grand_total= service_charge_total + cost
total_per_person = grand_total / group_size

print()
print(f"Here's the breakdown for {event}")
print()
print(f"Cost: ${cost:.2f}")
print(f"Service Charges:${service_charge_total:.2f}")
print("Group Size:",group_size)
print(f"Grand Total:${grand_total:.2f}")
print()
print(f"Each person must PayUp: ${total_per_person:.2f}")