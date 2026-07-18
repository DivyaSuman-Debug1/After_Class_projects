# Holiday Activity Planner
# Lesson: Nested Conditional Statements
 
print("Time to Plan your Holiday")
print("Step 1: Pick your holiday type")
print("1 - Beach Holiday")
 
choice = int(input("Enter 1: "))
 
if choice == 1:
    print("Step 2: Pick your beach activity")
    print("1 - Swimming")
    print("2 - Sandcastle Building")
 
    beach_activity = int(input("Enter 1 or 2: "))
    print()
 
    if beach_activity == 1:
        print("You picked: Swimming")
        print("Best time: Morning")
        print("Remember: Carry sunscreen and water")
    else:
        print("You picked: Sandcastle Building")
        print("Best time: Evening")
        print("Remember: Carry a bucket and spade")
 
else:
    print("That was not a valid choice.")
    print("Please enter 1 for Beach Holiday as it is the only avilable option")
 
print("Your holiday plan is ready!, Enjoy your trip!")