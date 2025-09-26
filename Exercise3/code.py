#SOLUTION ON STACK
portal=[]
#push operation
portal.append("Login")
portal.append("View Grade")
portal.append("Download")
portal.append("Trancript")
print ("stack before undo twice=",portal)
#undo operation
portal.pop()
portal.pop()
print ("stack after undo twice=",portal)

#momo pay stack
momo_pay=[]
momo_pay.append("Enter Amount")
momo_pay.append("Enter Pin")
momo_pay.append("Confirm")
print("Momo Pay before pop one=",momo_pay)
momo_pay.pop()
print("Momo Pay after pop one=",momo_pay)

#We are going to make clear algorithm on challenge stack
# I am going to declale stack called challenge
challenge=[]
#I am going to enter(push) element in challenge, after adding three element I removed one element and then after add another
challenge.append("X")
challenge.append("Y")
challenge.append("Z")
# I am going to print element in challege before removing one
print("challange before removing one element=",challenge)
# Iam going to remove element in challange and it use last in last out then print challenge after removing one element
challenge.pop()
print("challange after removing one element=",challenge)
# I am going to add one element in challenge and print element on the top
challenge.append("w")
print("challenge after adding W",challenge)
print("Top element in challenge is:",challenge[-1])

reflection=" Explaining how stack fit on undoing financial transaction; it fit it becouse it unable to undo last recent finacial transaction which means after decting mistake it collected first after being done"
print("reflection is this:",reflection)
#QUEUE answer
print("PRINT ANSWER ON QUEUE")
bk_atm=["jean","alain","jack","jule"]
print("queue before two withdraw=",bk_atm)
for _ in range(2):
  removed=bk_atm.pop(0)
print("queue after two withdraw=",bk_atm)
#answer on buses
print("bus answer")
bus=["retco","horizon","volcano","jali","4g","alpha"]
print("buses in park before three depart are:",bus)
#departing three buses
for _ in range(3):
 removed =bus.pop(0)
print("buses in park after three depart are:",bus)
#CHALLENGE
#Example of voting line especially based on arriving time
#let say there many voters we use sample of first five
vote_list=["ngenzi","manzi","nganji","niwe","niyo"]
print("vote list before vote start=",vote_list)
#by using this queue below after ngenzi vote the next will manzi and it works next by next until it end
vote_list.pop(0)
print("vote list after ngenzi voted=",vote_list)
vote_list.pop(0)
print("vote list after manzi voted=",vote_list)
vote_list.pop(0)
print("vote list after nganji voted=",vote_list)
vote_list.pop(0)
print("vote list after niwe voted=",vote_list)

print("REFLECTION:")
print("To use queue in election is fair because the voters vote in older as they arrived which means first come first vote in order which ensure efficient ellection")






























