
sqi = int(0)
sq = []
isl = input("Please enter an initial stock level:")
mtp = int(input("Please enter the number of month to plan:"))

print(type(mtp))
for i in range(mtp):
    sqi = input("Please enter the planned sales quantity:")
    sq.append(sqi)
    
print(sq)    
 
