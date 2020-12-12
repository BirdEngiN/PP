#Test
import random
Pokemon =   {
            "Bulbasaur":
                {'Hp':45,'Atk':49,'Def':49,'Sp.Atk':65,'Sp.Def':65,'Speed':45,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                    'Tackle':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                    'Growl':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':40},
                    'Vine Whip':{'Type':'Grass','cat':'physical','pwr':45,'acc':100,'pp':25},
                    'Growth':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':20},
                    'Leech Seed':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':10},
                    'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                    'Poison Powder':{'Type':'Poison','cat':'status','pwr':0,'acc':75,'pp':35},
                    'Sleep Powder':{'Type':'Grass','cat':'status','pwr':0,'acc':75,'pp':15},
                    'Seed Bomb':{'Type':'Grass','cat':'physical','pwr':80,'acc':100,'pp':15},
                    'Take Down':{'Type':'Normal','cat':'physical','pwr':90,'acc':85,'pp':20},
                    'Sweet Scent':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':20},
                    'Synthesis':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':5},
                    'Worry Seed':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':10},
                    'Double-Edge':{'Type':'Normal','cat':'physical','pwr':120,'acc':100,'pp':15},
                    'Solar Beam':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10}
                }},
                "Ivysaur":
                {'Hp':60,'Atk':62,'Def':63,'Sp.Atk':80,'Sp.Def':80,'Speed':60,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                    'Tackle':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                    'Growl':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':40},
                    'Vine Whip':{'Type':'Grass','cat':'physical','pwr':45,'acc':100,'pp':25},
                    'Growth':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':20},
                    'Leech Seed':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':10},
                    'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                    'Poison Powder':{'Type':'Poison','cat':'status','pwr':0,'acc':75,'pp':35},
                    'Sleep Powder':{'Type':'Grass','cat':'status','pwr':0,'acc':75,'pp':15},
                    'Seed Bomb':{'Type':'Grass','cat':'physical','pwr':80,'acc':100,'pp':15},
                    'Take Down':{'Type':'Normal','cat':'physical','pwr':90,'acc':85,'pp':20},
                    'Sweet Scent':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':20},
                    'Synthesis':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':5},
                    'Worry Seed':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':10},
                    'Double-Edge':{'Type':'Normal','cat':'physical','pwr':120,'acc':100,'pp':15},
                    'Solar Beam':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10}
                }},
                "Venusaur":
                {'Hp':80,'Atk':82,'Def':83,'Sp.Atk':100,'Sp.Def':100,'Speed':80,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                    'Petal Blizzard':{'Type':'Grass','cat':'physical','pwr':90,'acc':100,'pp':15},
                    'Petal Dance':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10},
                    'Tackle':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                    'Growl':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':40},
                    'Vine Whip':{'Type':'Grass','cat':'physical','pwr':45,'acc':100,'pp':25},
                    'Growth':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':20},
                    'Leech Seed':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':10},
                    'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                    'Poison Powder':{'Type':'Poison','cat':'status','pwr':0,'acc':75,'pp':35},
                    'Sleep Powder':{'Type':'Grass','cat':'status','pwr':0,'acc':75,'pp':15},
                    'Seed Bomb':{'Type':'Grass','cat':'physical','pwr':80,'acc':100,'pp':15},
                    'Take Down':{'Type':'Normal','cat':'physical','pwr':90,'acc':85,'pp':20},
                    'Sweet Scent':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':20},
                    'Synthesis':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':5},
                    'Worry Seed':{'Type':'Grass','cat':'status','pwr':0,'acc':100,'pp':10},
                    'Double-Edge':{'Type':'Normal','cat':'physical','pwr':120,'acc':100,'pp':15},
                    'Solar Beam':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10}
                }},
            "Charmander":
                {'Hp':39,'Atk':52,'Def':43,'Sp.Atk':60,'Sp.Def':50,'Speed':65,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                'Growl':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':40},
                'Ember':{'Type':'Fire','cat':'special','pwr':40,'acc':100,'pp':25},
                'Smokescreen':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':30},
                'Slash':{'Type':'Normal','cat':'physical','pwr':70,'acc':100,'pp':20},
                'Dragon Breath':{'Type':'Dragon','cat':'special','pwr':60,'acc':100,'pp':20},
                'Fire Fang':{'Type':'Fire','cat':'physical','pwr':65,'acc':95,'pp':15},
                'Flamethrower':{'Type':'Fire','cat':'special','pwr':90,'acc':100,'pp':15},
                'Scary Face':{'Type':'Normal','cat':'status','pwr':0,'acc':100,'pp':10},
                'Fire Spin':{'Type':'Fire','cat':"special",'pwr':35,'acc':85,'pp':15},
                'Inferno':{'Type':'Fire','cat':'special','pwr':100,'acc':50,'pp':5},
                'Flare Blitz':{'Type':'Fire','cat':'physical','pwr':120,'acc':100,'pp':15}
                }},
            "Charmeleon":
                {'Hp':58,'Atk':64,'Def':58,'Sp.Atk':80,'Sp.Def':65,'Speed':80,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Growl':{'Type':"Normal",'cat':"status",'pwr':0,'acc':100,'pp':40},
                'Ember':{'Type':"Fire",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Smokescreen':{'Type':"Normal",'cat':"status",'pwr':0,'acc':100,'pp':30},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Dragon Breath':{'Type':"Dragon",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Fire Fang':{'Type':"Fire",'cat':"physical",'pwr':65,'acc':95,'pp':15},
                'Flamethrower':{'Type':"Fire",'cat':"special",'pwr':90,'acc':100,'pp':15},
                'Scary Face':{'Type':"Normal",'cat':"status",'pwr':0,'acc':100,'pp':10},
                'Fire Spin':{'Type':"Fire",'cat':"special",'pwr':35,'acc':85,'pp':15},
                'Inferno':{'Type':"Fire",'cat':"special",'pwr':100,'acc':50,'pp':5},
                'Flare Blitz':{'Type':"Fire",'cat':"physical",'pwr':120,'acc':100,'pp':15}
                }},
            "Charizard":
                {'Hp':78,'Atk':84,'Def':78,'Sp.Atk':109,'Sp.Def':85,'Speed':100,
                'Type':['Fire','Flying'],'Weakness':{'Water':2,'Electric':2,'Rock':4},
                'Immune':{'Ground':0},'Resistant':{'Fighting':1/2,'Steel':1/2,'Bug':1/4,'Fire':1/2,'Grass':1/4},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Growl':{'Type':"Normal",'cat':"status",'pwr':0,'acc':100,'pp':40},
                'Ember':{'Type':"Fire",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Smokescreen':{'Type':"Normal",'cat':"status",'pwr':0,'acc':100,'pp':30},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Dragon Breath':{'Type':"Dragon",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Fire Fang':{'Type':"Fire",'cat':"physical",'pwr':65,'acc':95,'pp':15},
                'Flamethrower':{'Type':"Fire",'cat':"special",'pwr':90,'acc':100,'pp':15},
                'Scary Face':{'Type':"Normal",'cat':"status",'pwr':0,'acc':100,'pp':10},
                'Fire Spin':{'Type':"Fire",'cat':"special",'pwr':35,'acc':85,'pp':15},
                'Inferno':{'Type':"Fire",'cat':"special",'pwr':100,'acc':50,'pp':5},
                'Flare Blitz':{'Type':"Fire",'cat':"physical",'pwr':120,'acc':100,'pp':15},
                'Air Slash':{'Type':"Flying",'cat':"special",'pwr':75,'acc':95,'pp':15},
                'Dragon Claw':{'Type':"Dragon",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Heat Wave':{'Type':"Fire",'cat':"special",'pwr':95,'acc':90,'pp':10}
                }}
}
#==========================================================================================================
def Hp(p1): #Real Hp
    RHP = int(((((2*Pokemon[p1]['Hp'])+31)/100)*50)+50+10)
    ##RHP = int(((((2*Pokemon[p1]['Hp'])+31+Pokemon[p1]['EVs'])/100)*50)+50+10)
    return RHP
def Atk(p1):
    RATK = int((((((2*Pokemon[p1]['Atk'])+31)/100)*50)+5))
    ##RHP = int(((((2*Pokemon[p1]['Atk'])+31+Pokemon[p1]['EVs']))/100)+5)*Pokemon[p1]['Nature'])
    return RATK
def Def(p1):
    RDEF = int((((((2*Pokemon[p1]['Def'])+31)/100)*50)+5))
    ##RHP = int(((((2*Pokemon[p1]['Def'])+31+Pokemon[p1]['EVs']))/100)+5)*Pokemon[p1]['Nature'])
    return RDEF
def SpAtk(p1):
    RSATK = int((((((2*Pokemon[p1]['Sp.Atk'])+31)/100)*50)+5))
    ##RHP = int(((((2*Pokemon[p1]['Sp.Atk'])+31+Pokemon[p1]['EVs']))/100)+5)*Pokemon[p1]['Nature'])
    return RSATK
def SpDef(p1):
    RSDEF = int((((((2*Pokemon[p1]['Sp.Def'])+31)/100)*50)+5))
    ##RHP = int(((((2*Pokemon[p1]['Sp.Def'])+31+Pokemon[p1]['EVs']))/100)+5)*Pokemon[p1]['Nature'])
    return RSDEF
def Speed(p1):
    RSPEED = int((((((2*Pokemon[p1]['Speed'])+31)/100)*50)+5))
    ##RHP = int(((((2*Pokemon[p1]['Speed'])+31+Pokemon[p1]['EVs']))/100)+5)*Pokemon[p1]['Nature'])
    return RSPEED
def Realstats(p1): ## stats จริงของมอน
    RS = []
    RS.append(Hp(p1))
    RS.append(Atk(p1))
    RS.append(Def(p1))
    RS.append(SpAtk(p1))
    RS.append(SpDef(p1))
    RS.append(Speed(p1))
    return RS
#==========================================================================================================
##ทำที่ใส่นิสัยแบบใส่โปเกมอน
##PokemonP1 =[p1,movech1]
##print(PokemonP1)
def Priority(p1,p2):
    use1 = p1[2]
    use2 = p2[2]
    p = []
    p5p = ['Helping Hand']
    p4p = ['Baneful Bunker','Detect','Endure',"King's Shield",'Magic Coat','Protect','Spiky Shield','Snatch']
    p3p = ['Crafty Shield','Fake Out','Quick Guard','Wide Guard']
    p2p = ['Ally Switch','Extreme Speed','Feint','First Impression','Follow Me','Rage Powder','Zippy Zap']
    p1p = ['Accelerock','Aqua Jet','Baby-Doll Eyes','Bide','Bullet Punch','Ice Shard','Ion Deluge','Mach Punch','Powder','Quick Attack','Shadow Sneak','Sucker Punch','Vacuum Wave','Water Shuriken']
    p1m = ['Vital Throw']
    p3m = ['Focus Punch']
    p4m = ['Avalanche','Revenge']
    p5m = ['Counter','Mirror Coat']
    p6m = ['Circle Throw','Dragon Tail','Roar','Whirlwind']
    p7m = ['Trick Room']
    prip = [p5p,p4p,p3p,p2p,p1p] #Priority Plus
    prim = [p1m,p3m,p4m,p5m,p6m,p7m] #Priority Minus
    pri = [p5p,p4p,p3p,p2p,p1p,p1m,p3m,p4m,p5m,p6m,p7m]
    using1 = use1
    using2 = use2
    for i in pri:
        if i == p5p:
            j = +5
        elif i == p4p:
            j = +4
        elif i == p3p:
            j = +3
        elif i == p2p:
            j = +2
        elif i == p1p:
            j = +1
        elif i == p1m:
            j = -1
        elif i == p3m:
            j = -3
        elif i == p4m:
            j = -4
        elif i == p5m:
            j = -5
        elif i == p6m:
            j = -6
        elif i == p7m:
            j = -7
        else:
            j=0
        if use1 in i:
            use1 = [use1,j]
            break
        else:
            use1 = [use1,0]
            break
    for i in pri:
        if i == p5p:
            j = +5
        elif i == p4p:
            j = +4
        elif i == p3p:
            j = +3
        elif i == p2p:
            j = +2
        elif i == p1p:
            j = +1
        elif i == p1m:
            j = -1
        elif i == p3m:
            j = -3
        elif i == p4m:
            j = -4
        elif i == p5m:
            j = -5
        elif i == p6m:
            j = -6
        elif i == p7m:
            j = -7
        else:
            j=0
        if use2 in i:
            use2 = [use2,j]
            break
        else:
            use2 = [use2,0]
            break
    if use1[1] == use2[1]:
        if Pokemon[p1[0]]['Speed'] > Pokemon[p2[0]]['Speed']:
            p.append(using1)
            p.append(using2)
            return p
        elif Pokemon[p1[0]]['Speed'] < Pokemon[p2[0]]['Speed']:
            p.append(using2)
            p.append(using1)
            return p
    elif use1[1] > use2[1]:
        p.append(using1)
        p.append(using2)
        return p
    else: #use 2 > use 1
        p.append(using2)
        p.append(using1)
        return p
#====================================================================================================================================       
""" def Status(p1,p2):
    if  """
#=====================================================================================================================================
def Battle(p1,p2): ## Phrase ต่อสู้
    for i in p1[1]:
        print(i)
    use1 = input("Choose your move!! :")
    for i in p2[1]:
        print(i)
    use2 = input("Choose your opponent move!! :")
    p1.append(use1)
    p2.append(use2)
    return [p1,p2]
PokemonP1 = ['Charizard',['Flare Blitz','Inferno','Fire Spin','Air Slash']]
PokemonP2 = ['Venusaur',['Solar Beam','Poison Powder','Razor Leaf','Take Down']]
""" p = Battle(PokemonP1,PokemonP2)
move1,move2 = p[0],p[1]
Priority = Priority(move1,move2) """
def movec(move):#Critical calculator 
    if move != 'Razor Leaf' and move != 'Crabhammer' and move != 'Razor Wind' and move!='Shadow Claw' and move!='Slash' and move!='Stone Edge' and move!='Night Slash':
        p =random.randint(0,23)
        if p==1 :
            return 1.5
        else:
            return 1
    else:
        p = random.randint(0,7)
        if p ==1:
            return 1.5
        else:
            return 1
def Damaging(Move,PokemonP1,PokemonP2): #PokemonP1 = ['Charizard',[Moves],[usage_move]]
    randomfactor = random.uniform(0.85,1.00)
    critical = movec(Move)
    if Move in PokemonP1:
        if Pokemon[PokemonP1[0]]['Moves'][Move]['Type'] in Pokemon[PokemonP1[0]]['Type']:
            STAB = 1.5
        else:
            STAB = 1.0
        if 'Burn' in PokemonP1:
            Burn = 0.5
        else:
            Burn = 1
        Modifier = critical*randomfactor*STAB*Burn
        if (Pokemon[PokemonP1[0]]['Moves'][Move]['cat']) == 'physical':
            damage = (((((((((2*50)/5)+2)*Type(PokemonP1[0],Move,PokemonP2[0]))*Atk(PokemonP1[0]))/Def(PokemonP2[0]))+((100*Type(PokemonP1[0],Move,PokemonP2[0]))/Pokemon[PokemonP1[0]]['Moves'][Move]['pwr']))/50))*Modifier
        else:
            damage = (((((((((2*50)/5)+2)*Type(PokemonP1[0],Move,PokemonP2[0]))*SpAtk(PokemonP1[0]))/SpDef(PokemonP2[0]))+((100*Type(PokemonP1[0],Move,PokemonP2[0]))/Pokemon[PokemonP1[0]]['Moves'][Move]['pwr']))/50))*Modifier
        return (int(damage))
    else :
        if Pokemon[PokemonP2[0]]['Moves'][Move]['Type'] in Pokemon[PokemonP2[0]]['Type']:
            STAB = 1.5
        else:
            STAB = 1.0
        if 'Burn' in PokemonP2:
            Burn = 0.5
        else:
            Burn = 1
        Modifier = critical*randomfactor*STAB*Burn
        if (Pokemon[PokemonP2[0]]['Moves'][Move]['cat']) == 'physical':
            damage = (((((((((2*50)/5)+2)*Type(PokemonP2[0],Move,PokemonP1[0]))*Atk(PokemonP2[0]))/Def(PokemonP1[0]))+((100*Type(PokemonP2[0],Move,PokemonP1[0]))/Pokemon[PokemonP2[0]]['Moves'][Move]['pwr']))/50))*Modifier
        else :
            damage = (((((((((2*50)/5)+2)*Type(PokemonP2[0],Move,PokemonP1[0]))*SpAtk(PokemonP2[0]))/SpDef(PokemonP1[0]))+((100*Type(PokemonP2[0],Move,PokemonP1[0]))/Pokemon[PokemonP2[0]]['Moves'][Move]['pwr']))/50))*Modifier
        return int(damage)
        ##damage = ((((((((2*50)/5)+2)*power)*Atk(p1))/Def(p2))/50)+2)*Modifier
#=====================================================================================================================================
""" 
def Mod(p1,usage_move):
    if Pokemon[p1]['Moves'][usage_move] == ''
"""
#=====================================================================================================================================
def Type(p1,usage_move,p2): ##Type Calculator
    p1movetype = Pokemon[p1]['Moves'][usage_move]['Type'] ##ธาตุของท่าที่ตีมา
    if p1movetype in Pokemon[p2]['Weakness']:#usage move == ชื่อท่า
        dmg = (Pokemon[p2]['Weakness'][p1movetype])*int(Pokemon[p1]['Moves'][usage_move]['pwr'])
    elif p1movetype in Pokemon[p2]['Resistant']:
        dmg = (Pokemon[p2]['Resistant'][p1movetype])*int(Pokemon[p1]['Moves'][usage_move]['pwr'])
    elif p1movetype in Pokemon[p2]['Immune']:
        dmg = (Pokemon[p2]['Immune'][p1movetype])*int(Pokemon[p1]['Moves'][usage_move]['pwr'])
    else:
        dmg = int(Pokemon[p1]['Moves'][usage_move]['pwr'])
    return dmg
#==========================================================================================================
def MainBattle(p1,p2): 
    p1chp = Hp(p1[0]) #Player 1 Current Hp
    p2chp = Hp(p2[0]) #Player 2 Current Hp
    if p1chp !=0 and p2chp !=0:
        p = Battle(PokemonP1,PokemonP2)
        move1,move2 = p[0],p[1]
        Respect = Priority(move1,move2)
        damage_each_turn = []
        for i in Respect:
            damage_each_turn.append(Damaging(i,p1,p2))
    else:
        if p1chp !=0:
            print(p1,'Won the battle!!')
        else:
            print(p2,'Won the battle!!')
MainBattle(PokemonP1,PokemonP2)
#======================================================================================================================
""" q1 = True
while q1 == True:
    p1 = input("Choose your Pokemon!! : ")
    print('You have choose',p1,'!!!')
    print('Base Stats:')
    print('HP :',Pokemon[p1]['Hp'])
    print('Atk :',Pokemon[p1]['Atk'])
    print('Def :',Pokemon[p1]['Def'])
    print('Sp.Atk :',Pokemon[p1]['Sp.Atk'])
    print('Sp.Def :',Pokemon[p1]['Sp.Def'])
    print('Speed :',Pokemon[p1]['Speed'])
    print('Moves :')
    moves1 = Pokemon[p1]['Moves'].keys()
    for i in (moves1):
        print(i)
    print('Please choose 4 moves for your Pokemon.')
    movech1 =[]
    for j in range(4):
        move = input('')
        movech1.append(move)
    print(p1)
    for i in movech1:
        print(i)
    confirmation2 = input("Press 'Confirm' for confirmation.\n:")
    if confirmation2 == 'Confirm':
        q1 = False
        break
    else:
        pass
PokemonP1 =[p1,movech1]
print(PokemonP1)
##========================================================================================================
q2 = True
while q2 == True:
    p2 = input("Choose your opponent Pokemon!! : ")
    print('You have choose',p2,'!!!')
    print('Base Stats:')
    print('HP :',Pokemon[p2]['Hp'])
    print('Atk :',Pokemon[p2]['Atk'])
    print('Def :',Pokemon[p2]['Def'])
    print('Sp.Atk :',Pokemon[p2]['Sp.Atk'])
    print('Sp.Def :',Pokemon[p2]['Sp.Def'])
    print('Speed :',Pokemon[p2]['Speed'])
    print('Moves :')
    moves2 = Pokemon[p2]['Moves'].keys()
    for i in (moves2):
        print(i)
    print("Please choose 4 moves for your opponent Pokemon.")
    movech2 =[]
    for j in range(4):
        move = input('')
        movech2.append(move)
    print(p2)
    for i in movech2:
        print(i)
    confirmation2 = input("Press 'Confirm' for confirmation.\n:")
    if confirmation2 == 'Confirm':
        q2 = False
        break
    else:
        pass
PokemonP2 =[p2,movech2]
print(PokemonP2)
print(p1,p2)
battle_confirm=None
while battle_confirm !='Battle':
    battle_confirm = input("Press 'Battle' to start the battle!!\n :") """
