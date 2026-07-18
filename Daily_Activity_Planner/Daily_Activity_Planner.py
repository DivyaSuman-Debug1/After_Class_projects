
temp = int(input("Enter today's temperature in Celsius: "))
 
if temp < 20:
    act = "Indoor games"
    print("It is cool today.")
    print("Do", act)
else:
    act = "Outdoor walk"
    print("It is warm today.")
    print("Do", act)
 
rain = input("Is it raining today? (yes/no): ")
if rain == "yes":
    print("Choose an indoor activity or carry an umbrella")
 
print("Daily activity planner")
print("Temperature:", temp)
print("Activity Chosen:", act)
print("Raining:", rain)