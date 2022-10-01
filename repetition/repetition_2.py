# color = str(input("what is the collor?,yellow,red or green"))
# if color=="red":
#     print("STOP!")
# elif color=="yellow":
#     print("READY!")
# elif color=="green":
#     print("GO!")
good_apples = 0
bad_apples = 0
apple = 20
while apple!=0:
 apple3 = int(input("what apple do you want to choose? "))
 if apple3 == 1:
     apple -= 1
     good_apples +=1
     print(f"good - {good_apples}\napple whole - {apple}")
 elif apple3 == 2:
    apple -= 1
    print(f"bad - {bad_apples}\napple whole - {apple}")
 print(f"whole num - {apple}\n"
       f"good_apple - {good_apples}\n"
       f"bad_apple - {bad_apples}")





