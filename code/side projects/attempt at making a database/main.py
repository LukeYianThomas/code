valuelist = []
bname = []
bvalue = []
bdemand = []
name = []
value = []
demand = []
vdeviance = []
ddeviance = []
nextmessage = "awaiting input"
# first convert the stupid text file into 3 lists
with open("valuelist.txt") as f:
    for x in f:
        valuelist.append(x)
for x in valuelist:
    tn,tv,td,disintergration = x.split(",") # obliterate /n
    name.append(tn)
    bvalue.append(tv) # b = broken
    bdemand.append(td)
# then fix the broken shit
for x in bvalue:
    if "t" in x:
        tv2,tv3 = x.split("t") #tv = temp value
        tvd = int(tv3)-int(tv2) # tvd = temp value deviance
        value.append(tv3)
        vdeviance.append(tvd) # deviance is how much the value varies going backwards e.g v2 d1 = 1-2
    else:
        value.append(x)
        vdeviance.append(0)
for x in bdemand:
    if "t" in x:
        td2,td3 = x.split("t") #td = temp demand
        tdd = int(td3)-int(td2) # tdd = temp demand deviance
        demand.append(td3)
        ddeviance.append(tdd)
    else:
        demand.append(x)
        ddeviance.append(0)
# person types in random stuff split with , and it returns 
def lookup(querie):
    global nextmessage
    results = []
    temp = []
    if "," in querie:temp = querie.split(",")
    else:temp.append(querie)
    for i in range(0,len(temp)):# super awesome invalid results filter
        if temp[i] not in name:nextmessage = (f"{temp[i]} is an invalid querie and will not be added to the results")
        else:results.append(fetch(temp[i]))
    calc(results,False)
            
# the thing that goes and finds the stuff from the lists for other functions
def fetch(target):
    index = 0
    for x in name:
        if x == target:break
        else:index += 1      # creates a number to find the stuff
    return name[index],int(value[index]),int(vdeviance[index]),int(demand[index]),int(ddeviance[index])

# the maths
def calc(results,GoCompare):
    global nextmessage
    vdtotal = 0
    ddtotal = 0
    demandtotal = 0
    valuetotal = 0
    for x in results:
        name,value,vdeviance,demand,ddeviance = x
        vdtotal+=vdeviance
        ddtotal+=ddeviance
        valuetotal+=value
        demandtotal+=demand
        remainder = value%3
        value= 3*round((value-remainder)/3)
#        if GoCompare == False:nextmessage = (f"{name} is {value} myths , {remainder} rares deviating by {ddeviance} rares, {demand} demand deviating by {ddeviance}")
    if len(results)>1:demandaverage = demandtotal/len(results)
    else:demandaverage = demandtotal
    if GoCompare == False:nextmessage = (f"total value = {valuetotal} with a deviance of {vdtotal} and a average demand of {demandaverage} with a deviance of {ddtotal}")
    if GoCompare == True:return valuetotal,vdtotal,demandaverage,ddtotal

def compare(UserInv,EnemyInv):
    global nextmessage
    UVT,UVDT,UDA,UDDT = calc(UserInv,True)
    EVT,EVDT,EDA,EDDT = calc(EnemyInv,True)# I FORGOT WHAT THIS IS
    nextmessage = (f"Your total value = {UVT} with a deviance of {UVDT} and a average demand of {UDA} with a deviance of {UDDT}")
    nextmessage = (f"Their total value = {EVT} with a deviance of {EVDT} and a average demand of {EDA} with a deviance of {EDDT}")
    profit = EVT-UVT
    remainder = profit%3
    profit= 3*round((profit-remainder)/3)
    COMBINEDDEVIANCE = UDDT+EDDT
    DAPROFIT = EDA-UDA
    nextmessage = (f"Your estimated profit is {profit} myths , {remainder} rares with a deviance of {COMBINEDDEVIANCE} and an average demand profit of {DAPROFIT}")
def inputs(fish):
    global nextmessage
    if fish == "help":nextmessage = ("GRAHHHHHHHHHHHHHHHHHHHHHHHHHH")
    if "querie-" in fish: # the tech support bit ^
        obliteration,actuallyuseful = fish.split("-")
        lookup(actuallyuseful)
    if "compare-" in fish:
        worldendingcalamity,almostuseful = fish.split("-")
        UserInv,EnemyInv = almostuseful.split("<>")
        compare(UserInv,EnemyInv)
 # credit to nearoo for the textinput import
import pygame_textinput
import pygame
pygame.init()
textinput = pygame_textinput.TextInputVisualizer()
screen = pygame.display.set_mode((1050, 100))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 18)
while True:
    screen.fill((225, 225, 225))
    events = pygame.event.get()
    textinput.update(events)
    outputs = font.render(nextmessage,False, (0,0,0))
    screen.blit(textinput.surface, (10, 10))
    screen.blit(outputs, (10, 60))
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            inputs(textinput.value)
            textinput = pygame_textinput.TextInputVisualizer()
    pygame.display.update()
    clock.tick(30)