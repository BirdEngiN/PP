#Pokemon
import random
Pokemon =   {
            "Bulbasaur":
                {'Hp':45,'Atk':49,'Def':49,'Sp.Atk':65,'Sp.Def':65,'Speed':45,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                    'Tackle':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                    'Vine Whip':{'Type':'Grass','cat':'physical','pwr':45,'acc':100,'pp':25},
                    'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                    'Seed Bomb':{'Type':'Grass','cat':'physical','pwr':80,'acc':100,'pp':15},
                    'Take Down':{'Type':'Normal','cat':'physical','pwr':90,'acc':85,'pp':20},
                    'Double-Edge':{'Type':'Normal','cat':'physical','pwr':120,'acc':100,'pp':15},
                    'Solar Beam':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10}
                }},
                "Ivysaur":
                {'Hp':60,'Atk':62,'Def':63,'Sp.Atk':80,'Sp.Def':80,'Speed':60,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                    'Tackle':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                    'Vine Whip':{'Type':'Grass','cat':'physical','pwr':45,'acc':100,'pp':25},
                    'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                    'Seed Bomb':{'Type':'Grass','cat':'physical','pwr':80,'acc':100,'pp':15},
                    'Take Down':{'Type':'Normal','cat':'physical','pwr':90,'acc':85,'pp':20},
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
                    'Vine Whip':{'Type':'Grass','cat':'physical','pwr':45,'acc':100,'pp':25},
                    'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                    'Seed Bomb':{'Type':'Grass','cat':'physical','pwr':80,'acc':100,'pp':15},
                    'Take Down':{'Type':'Normal','cat':'physical','pwr':90,'acc':85,'pp':20},
                    'Double-Edge':{'Type':'Normal','cat':'physical','pwr':120,'acc':100,'pp':15},
                    'Solar Beam':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10}
                }},
            "Charmander":
                {'Hp':39,'Atk':52,'Def':43,'Sp.Atk':60,'Sp.Def':50,'Speed':65,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                'Ember':{'Type':'Fire','cat':'special','pwr':40,'acc':100,'pp':25},
                'Slash':{'Type':'Normal','cat':'physical','pwr':70,'acc':100,'pp':20},
                'Dragon Breath':{'Type':'Dragon','cat':'special','pwr':60,'acc':100,'pp':20},
                'Fire Fang':{'Type':'Fire','cat':'physical','pwr':65,'acc':95,'pp':15},
                'Flamethrower':{'Type':'Fire','cat':'special','pwr':90,'acc':100,'pp':15},
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
                'Ember':{'Type':"Fire",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Dragon Breath':{'Type':"Dragon",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Fire Fang':{'Type':"Fire",'cat':"physical",'pwr':65,'acc':95,'pp':15},
                'Flamethrower':{'Type':"Fire",'cat':"special",'pwr':90,'acc':100,'pp':15},
                'Fire Spin':{'Type':"Fire",'cat':"special",'pwr':35,'acc':85,'pp':15},
                'Inferno':{'Type':"Fire",'cat':"special",'pwr':100,'acc':50,'pp':5},
                'Flare Blitz':{'Type':"Fire",'cat':"physical",'pwr':120,'acc':100,'pp':15}
                }},
            "Charizard":
                {'Hp':78,'Atk':84,'Def':78,'Sp.Atk':109,'Sp.Def':85,'Speed':100,
                'Type':['Fire','Flying'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Ember':{'Type':"Fire",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Dragon Breath':{'Type':"Dragon",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Fire Fang':{'Type':"Fire",'cat':"physical",'pwr':65,'acc':95,'pp':15},
                'Flamethrower':{'Type':"Fire",'cat':"special",'pwr':90,'acc':100,'pp':15},
                'Fire Spin':{'Type':"Fire",'cat':"special",'pwr':35,'acc':85,'pp':15},
                'Inferno':{'Type':"Fire",'cat':"special",'pwr':100,'acc':50,'pp':5},
                'Flare Blitz':{'Type':"Fire",'cat':"physical",'pwr':120,'acc':100,'pp':15},
                'Air Slash':{'Type':"Flying",'cat':"special",'pwr':75,'acc':95,'pp':15},
                'Dragon Claw':{'Type':"Dragon",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Heat Wave':{'Type':"Fire",'cat':"special",'pwr':950,'acc':90,'pp':10}
                }},
            "Squirtle":
                {'Hp':44,'Atk':48,'Def':65,'Sp.Atk':50,'Sp.Def':64,'Speed':43,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Water Gun':{'Type':"Water",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Rapid Spin':{'Type':"Normal",'cat':"physical",'pwr':50,'acc':100,'pp':40},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Water Pulse':{'Type':"Water",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Aqua Tail':{'Type':"Water",'cat':"physical",'pwr':90,'acc':90,'pp':10},
                'Hydro Pump':{'Type':"Water",'cat':"special",'pwr':110,'acc':80,'pp':5},
                'Skull Bash':{'Type':"Normal",'cat':"physical",'pwr':130,'acc':100,'pp':10}
                }},
            "Wartortle":
                {'Hp':59,'Atk':63,'Def':80,'Sp.Atk':65,'Sp.Def':80,'Speed':58,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Water Gun':{'Type':"Water",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Rapid Spin':{'Type':"Normal",'cat':"physical",'pwr':50,'acc':100,'pp':40},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Water Pulse':{'Type':"Water",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Aqua Tail':{'Type':"Water",'cat':"physical",'pwr':90,'acc':90,'pp':10},
                'Hydro Pump':{'Type':"Water",'cat':"special",'pwr':110,'acc':80,'pp':5},
                'Skull Bash':{'Type':"Normal",'cat':"physical",'pwr':130,'acc':100,'pp':10}
                }},
            "Blastoise":
                {'Hp':79,'Atk':83,'Def':100,'Sp.Atk':85,'Sp.Def':105,'Speed':78,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Water Gun':{'Type':"Water",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Rapid Spin':{'Type':"Normal",'cat':"physical",'pwr':50,'acc':100,'pp':40},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Water Pulse':{'Type':"Water",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Aqua Tail':{'Type':"Water",'cat':"physical",'pwr':90,'acc':90,'pp':10},
                'Hydro Pump':{'Type':"Water",'cat':"special",'pwr':110,'acc':80,'pp':5},
                'Skull Bash':{'Type':"Normal",'cat':"physical",'pwr':130,'acc':100,'pp':10},
                'Flash Cannon':{'Type':"Steel",'cat':"special",'pwr':80,'acc':100,'pp':10},
                }},
            "Caterpie":
                {'Hp':45,'Atk':30,'Def':35,'Sp.Atk':20,'Sp.Def':20,'Speed':45,
                'Type':['Bug'],'Weakness':{'Flying':2,'Rock':2,'Fire':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Ground':1/2,'Grass':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Bug Bite':{'Type':"Bug",'cat':"physical",'pwr':60,'acc':100,'pp':20}
                }},
            "Metapod":
                {'Hp':50,'Atk':20,'Def':55,'Sp.Atk':25,'Sp.Def':25,'Speed':30,
                'Type':['Bug'],'Weakness':{'Flying':2,'Rock':2,'Fire':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Ground':1/2,'Grass':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Bug Bite':{'Type':"Bug",'cat':"physical",'pwr':60,'acc':100,'pp':20}
                }},
            "Butterfree":
                {'Hp':60,'Atk':45,'Def':50,'Sp.Atk':80,'Sp.Def':80,'Speed':70,
                'Type':['Bug','Flying'],'Weakness':{'Flying':2,'Rock':4,'Fire':2,'Electric':2,'Ice':2},
                'Immune':{'Ground':0},'Resistant':{'Fighting':1/4,'Bug':1/2,'Grass':1/4},
                'Moves':{
                'Gust':{'Type':"Flying",'cat':"special",'pwr':40,'acc':100,'pp':35},
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Bug Bite':{'Type':"Bug",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Confusion':{'Type':"Normal",'cat':"special",'pwr':50,'acc':100,'pp':25},
                'Psybeam':{'Type':"Normal",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Air Slash':{'Type':"Flying",'cat':"special",'pwr':75,'acc':95,'pp':15},
                'Bug Buzz':{'Type':"Bug",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Weedle":
                {'Hp':40,'Atk':35,'Def':30,'Sp.Atk':20,'Sp.Def':20,'Speed':50,
                'Type':['Bug','Poison'],'Weakness':{'Flying':2,'Rock':2,'Fire':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/4,'Poison':1/2,'Grass':1/4,'Bug':1/2},
                'Moves':{
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Bug Bite':{'Type':"Bug",'cat':"physical",'pwr':60,'acc':100,'pp':20}
                }},
            "Kakuna":
                {'Hp':45,'Atk':25,'Def':50,'Sp.Atk':25,'Sp.Def':25,'Speed':35,
                'Type':['Bug','Poison'],'Weakness':{'Flying':2,'Rock':2,'Fire':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/4,'Poison':1/2,'Grass':1/4,'Bug':1/2},
                'Moves':{
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Bug Bite':{'Type':"Bug",'cat':"physical",'pwr':60,'acc':100,'pp':20}
                }},
            "Beedrill":
                {'Hp':65,'Atk':80,'Def':40,'Sp.Atk':45,'Sp.Def':80,'Speed':75,
                'Type':['Bug','Poison'],'Weakness':{'Flying':2,'Rock':2,'Fire':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/4,'Poison':1/2,'Grass':1/4,'Bug':1/2},
                'Moves':{
                'Twineedle':{'Type':"Bug",'cat':"physical",'pwr':25,'acc':100,'pp':20},
                'Fury Attack':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':20},
                'Rage':{'Type':"Normal",'cat':"physical",'pwr':20,'acc':100,'pp':20},
                'Pursuit':{'Type':"Dark",'cat':"physical",'pwr':40,'acc':100,'pp':20},
                'Venoshock':{'Type':"Poison",'cat':"special",'pwr':65,'acc':100,'pp':10},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Pin Missile':{'Type':"Bug",'cat':"physical",'pwr':25,'acc':95,'pp':20},
                'Poison Jab':{'Type':"Poison",'cat':"physical",'pwr':80,'acc':100,'pp':20},
                'Endeavor':{'Type':"Normal",'cat':"physical",'pwr':0,'acc':100,'pp':5},
                'Fell Stinger':{'Type':"Bug",'cat':"physical",'pwr':50,'acc':100,'pp':25}
                }},
            "Pidgey":
                {'Hp':40,'Atk':45,'Def':40,'Sp.Atk':35,'Sp.Def':35,'Speed':56,
                'Type':['Normal','Flying'],'Weakness':{'Electric':2,'Rock':2,'Ice':2},
                'Immune':{'Ground':0,'Ghost':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Gust':{'Type':"Flying",'cat':"special",'pwr':40,'acc':100,'pp':35},
                'Quick Attack':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Twister':{'Type':"Dragon",'cat':"special",'pwr':40,'acc':100,'pp':35},
                'Wing Attack':{'Type':"Flying",'cat':"physical",'pwr':60,'acc':100,'pp':35},
                'Air Slash':{'Type':"Flying",'cat':"special",'pwr':75,'acc':95,'pp':35},
                'Hurricane':{'Type':"Flying",'cat':"special",'pwr':110,'acc':70,'pp':35}
                }},                
            "Pidgeotto":
                {'Hp':63,'Atk':60,'Def':55,'Sp.Atk':50,'Sp.Def':50,'Speed':71,
                'Type':['Normal','Flying'],'Weakness':{'Electric':2,'Rock':2,'Ice':2},
                'Immune':{'Ground':0,'Ghost':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Gust':{'Type':"Flying",'cat':"special",'pwr':40,'acc':100,'pp':35},
                'Quick Attack':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Twister':{'Type':"Dragon",'cat':"special",'pwr':40,'acc':100,'pp':35},
                'Wing Attack':{'Type':"Flying",'cat':"physical",'pwr':60,'acc':100,'pp':35},
                'Air Slash':{'Type':"Flying",'cat':"special",'pwr':75,'acc':95,'pp':35},
                'Hurricane':{'Type':"Flying",'cat':"special",'pwr':110,'acc':70,'pp':35}
                }},
            "Pidgeot":
                {'Hp':83,'Atk':80,'Def':80,'Sp.Atk':135,'Sp.Def':80,'Speed':121,
                'Type':['Normal','Flying'],'Weakness':{'Electric':2,'Rock':2,'Ice':2},
                'Immune':{'Ground':0,'Ghost':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Gust':{'Type':"Flying",'cat':"special",'pwr':40,'acc':100,'pp':35},
                'Quick Attack':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Twister':{'Type':"Dragon",'cat':"special",'pwr':40,'acc':100,'pp':35},
                'Wing Attack':{'Type':"Flying",'cat':"physical",'pwr':60,'acc':100,'pp':35},
                'Air Slash':{'Type':"Flying",'cat':"special",'pwr':75,'acc':95,'pp':35},
                'Hurricane':{'Type':"Flying",'cat':"special",'pwr':110,'acc':70,'pp':35}
                }},
            "Rattata":
                {'Hp':30,'Atk':56,'Def':35,'Sp.Atk':25,'Sp.Def':35,'Speed':72,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Quick Attack':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Pursuit':{'Type':"Dark",'cat':"physical",'pwr':40,'acc':100,'pp':20},
                'Hyper Fang':{'Type':"Normal",'cat':"physical",'pwr':80,'acc':90,'pp':15},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Crunch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Sucker Punch':{'Type':"Dark",'cat':"physical",'pwr':70,'acc':100,'pp':5},
                'Super Fang':{'Type':"Normal",'cat':"physical",'pwr':0,'acc':90,'pp':10},
                'Double-Edge':{'Type':"Normal",'cat':"physical",'pwr':120,'acc':100,'pp':15},
                'Endeavor':{'Type':"Normal",'cat':"physical",'pwr':0,'acc':100,'pp':5}
                }},
            "Raticate":
                {'Hp':55,'Atk':81,'Def':60,'Sp.Atk':50,'Sp.Def':70,'Speed':97,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Quick Attack':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Pursuit':{'Type':"Dark",'cat':"physical",'pwr':40,'acc':100,'pp':20},
                'Hyper Fang':{'Type':"Normal",'cat':"physical",'pwr':80,'acc':90,'pp':15},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Crunch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Sucker Punch':{'Type':"Dark",'cat':"physical",'pwr':70,'acc':100,'pp':5},
                'Super Fang':{'Type':"Normal",'cat':"physical",'pwr':0,'acc':90,'pp':10},
                'Double-Edge':{'Type':"Normal",'cat':"physical",'pwr':120,'acc':100,'pp':15},
                'Endeavor':{'Type':"Normal",'cat':"physical",'pwr':0,'acc':100,'pp':5},
                }},
            "Spearow":
                {'Hp':40,'Atk':60,'Def':30,'Sp.Atk':31,'Sp.Def':31,'Speed':70,
                'Type':['Normal','Flying'],'Weakness':{'Electric':2,'Rock':2,'Ice':2},
                'Immune':{'Ground':0,'Ghost':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Peck':{'Type':"Flying",'cat':"physical",'pwr':35,'acc':100,'pp':35},
                'Pursuit':{'Type':"Dark",'cat':"physical",'pwr':40,'acc':100,'pp':20},
                'Fury Attack':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':20},
                'Aerial Ace':{'Type':"Flying",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Drill Peck':{'Type':"Flying",'cat':"physical",'pwr':80,'acc':100,'pp':20}
                }},
            "Fearow":
                {'Hp':65,'Atk':90,'Def':65,'Sp.Atk':61,'Sp.Def':61,'Speed':100,
                'Type':['Normal','Flying'],'Weakness':{'Electric':2,'Rock':2,'Ice':2},
                'Immune':{'Ground':0,'Ghost':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Peck':{'Type':"Flying",'cat':"physical",'pwr':35,'acc':100,'pp':35},
                'Pursuit':{'Type':"Dark",'cat':"physical",'pwr':40,'acc':100,'pp':20},
                'Fury Attack':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':20},
                'Aerial Ace':{'Type':"Flying",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Drill Peck':{'Type':"Flying",'cat':"physical",'pwr':80,'acc':100,'pp':20},
                'Drill Run':{'Type':"Ground",'cat':"physical",'pwr':80,'acc':95,'pp':10},
                'Pluck':{'Type':"Flying",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                }},
            "Ekans":
                {'Hp':35,'Atk':60,'Def':44,'Sp.Atk':40,'Sp.Def':54,'Speed':55,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Grass':1/2,'Bug':1/2,'Poison':1/2,'Fighting':1/2},
                'Moves':{
                'Wrap':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':90,'pp':20},
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Acid':{'Type':"Poison",'cat':"special",'pwr':40,'acc':100,'pp':30},
                'Acid Spray':{'Type':"Poison",'cat':"special",'pwr':40,'acc':90,'pp':20},
                'Mud Bomb':{'Type':"Normal",'cat':"special",'pwr':65,'acc':90,'pp':10},
                'Gunk Shot':{'Type':"Poison",'cat':"physical",'pwr':120,'acc':80,'pp':5}
                }},
            "Arbok":
                {'Hp':60,'Atk':95,'Def':69,'Sp.Atk':65,'Sp.Def':79,'Speed':80,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Grass':1/2,'Bug':1/2,'Poison':1/2,'Fighting':1/2},
                'Moves':{
                'Wrap':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':90,'pp':20},
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Acid':{'Type':"Poison",'cat':"special",'pwr':40,'acc':100,'pp':30},
                'Acid Spray':{'Type':"Poison",'cat':"special",'pwr':40,'acc':90,'pp':20},
                'Mud Bomb':{'Type':"Normal",'cat':"special",'pwr':65,'acc':90,'pp':10},
                'Gunk Shot':{'Type':"Poison",'cat':"physical",'pwr':120,'acc':80,'pp':5},
                'Crunch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Ice Fang':{'Type':"Ice",'cat':"physical",'pwr':65,'acc':95,'pp':15},
                'Thunder Fang':{'Type':"Thunder",'cat':"physical",'pwr':65,'acc':95,'pp':15},
                'Fire Fang':{'Type':"Fire",'cat':"physical",'pwr':65,'acc':95,'pp':15}
                }},
            "Pikachu":
                {'Hp':35,'Atk':55,'Def':40,'Sp.Atk':50,'Sp.Def':50,'Speed':90,
                'Type':['Electric'],'Weakness':{'Ground':2},
                'Immune':{},'Resistant':{'Flying':1/2,'Steel':1/2,'Electric':1/2},
                'Moves':{
                'Thunder Shock':{'Type':"Electric",'cat':"special",'pwr':40,'acc':100,'pp':30},
                'Quick Attack':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':30},
                'Electro Ball':{'Type':"Electric",'cat':"special",'pwr':60,'acc':100,'pp':10},
                'Feint':{'Type':"Normal",'cat':"physical",'pwr':30,'acc':100,'pp':10},
                'Spark':{'Type':"Electric",'cat':"physical",'pwr':65,'acc':100,'pp':20},
                'Nuzzle':{'Type':"Electric",'cat':"physical",'pwr':20,'acc':100,'pp':20},
                'Discharge':{'Type':"Electric",'cat':"special",'pwr':80,'acc':100,'pp':15},
                'Slam':{'Type':"Normal",'cat':"physical",'pwr':80,'acc':75,'pp':20},
                'Thunderbolt':{'Type':"Electric",'cat':"special",'pwr':90,'acc':100,'pp':15},
                'Wild Charge':{'Type':"Electric",'cat':"physical",'pwr':90,'acc':100,'pp':15},
                'Thunder':{'Type':"Electric",'cat':"special",'pwr':110,'acc':70,'pp':10}
                }},
            "Raichu":
                {'Hp':60,'Atk':90,'Def':55,'Sp.Atk':90,'Sp.Def':80,'Speed':110,
                'Type':['Electric'],'Weakness':{'Ground':2},
                'Immune':{},'Resistant':{'Flying':1/2,'Steel':1/2,'Electric':1/2},
                'Moves':{
                'Thunder Shock':{'Type':"Electric",'cat':"special",'pwr':40,'acc':100,'pp':30},
                'Quick Attack':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':30},
                'Electro Ball':{'Type':"Electric",'cat':"special",'pwr':60,'acc':100,'pp':10},
                'Feint':{'Type':"Normal",'cat':"physical",'pwr':30,'acc':100,'pp':10},
                'Spark':{'Type':"Electric",'cat':"physical",'pwr':65,'acc':100,'pp':20},
                'Nuzzle':{'Type':"Electric",'cat':"physical",'pwr':20,'acc':100,'pp':20},
                'Discharge':{'Type':"Electric",'cat':"special",'pwr':80,'acc':100,'pp':15},
                'Slam':{'Type':"Normal",'cat':"physical",'pwr':80,'acc':75,'pp':20},
                'Thunderbolt':{'Type':"Electric",'cat':"special",'pwr':90,'acc':100,'pp':15},
                'Wild Charge':{'Type':"Electric",'cat':"physical",'pwr':90,'acc':100,'pp':15},
                'Thunder':{'Type':"Electric",'cat':"special",'pwr':110,'acc':70,'pp':10}
                }},
            "Sandshrew":
                {'Hp':50,'Atk':75,'Def':85,'Sp.Atk':20,'Sp.Def':30,'Speed':40,
                'Type':['Ground'],'Weakness':{'Water':2,'Grass':2,'Ice':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/2,'Rock':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Rollout':{'Type':"Rock",'cat':"physical",'pwr':30,'acc':90,'pp':20},
                'Fury Cutter':{'Type':"Bug",'cat':"physical",'pwr':40,'acc':95,'pp':20},
                'Rapid Spin':{'Type':"Normal",'cat':"physical",'pwr':50,'acc':100,'pp':40},
                'Bulldoze':{'Type':"Ground",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Swift':{'Type':"Normal",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Fury Swipes':{'Type':"Normal",'cat':"special",'pwr':18,'acc':80,'pp':15},
                'Agility':{'Type':"Psychic",'cat':"physical",'pwr':0,'acc':100,'pp':30},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Dig':{'Type':"Ground",'cat':"physical",'pwr':80,'acc':100,'pp':10},
                'Gyro Ball':{'Type':"Steel",'cat':"physical",'pwr':40,'acc':100,'pp':5},
                'Earthquake':{'Type':"Ground",'cat':"physical",'pwr':100,'acc':100,'pp':10},
                }},
            "Sandslash":
                {'Hp':75,'Atk':100,'Def':110,'Sp.Atk':45,'Sp.Def':55,'Speed':65,
                'Type':['Ground'],'Weakness':{'Water':2,'Grass':2,'Ice':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/2,'Rock':1/2},
                'Moves':{
                'Crush Claw':{'Type':'Normal','cat':"physical",'pwr':75,'acc':95,'pp':10}
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Rollout':{'Type':"Rock",'cat':"physical",'pwr':30,'acc':90,'pp':20},
                'Fury Cutter':{'Type':"Bug",'cat':"physical",'pwr':40,'acc':95,'pp':20},
                'Rapid Spin':{'Type':"Normal",'cat':"physical",'pwr':50,'acc':100,'pp':40},
                'Bulldoze':{'Type':"Ground",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Swift':{'Type':"Normal",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Fury Swipes':{'Type':"Normal",'cat':"special",'pwr':18,'acc':80,'pp':15},
                'Sand Tomb':{'Type':"Ground",'cat':"physical",'pwr':35,'acc':85,'pp':15},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Dig':{'Type':"Ground",'cat':"physical",'pwr':80,'acc':100,'pp':10},
                'Gyro Ball':{'Type':"Steel",'cat':"physical",'pwr':40,'acc':100,'pp':5},
                'Earthquake':{'Type':"Ground",'cat':"physical",'pwr':100,'acc':100,'pp':10},
                }},
            "NidoranF":
                {'Hp':55,'Atk':47,'Def':52,'Sp.Atk':40,'Sp.Def':40,'Speed':41,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Poison':1/2,'Bug':1/2,'Grass':1/2},
                'Moves':{
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Double Kick':{'Type':"Fighting",'cat':"physical",'pwr':30,'acc':100,'pp':30},
                'Crunch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Earth Power':{'Type':"Ground",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Nidorina":
                {'Hp':70,'Atk':62,'Def':67,'Sp.Atk':55,'Sp.Def':55,'Speed':56,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Poison':1/2,'Bug':1/2,'Grass':1/2},
                'Moves':{
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Double Kick':{'Type':"Fighting",'cat':"physical",'pwr':30,'acc':100,'pp':30},
                'Crunch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Earth Power':{'Type':"Ground",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Nidoqueen":
                {'Hp':90,'Atk':92,'Def':87,'Sp.Atk':75,'Sp.Def':85,'Speed':76,
                'Type':['Poison','Ground'],'Weakness':{'Ground':2,'Psychic':2,'Water':2,'Ice':2},
                'Immune':{'Electric':0},'Resistant':{'Fighting':1/2,'Poison':1/4,'Bug':1/2,'Rock':1/2},
                'Moves':{
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Double Kick':{'Type':"Fighting",'cat':"physical",'pwr':30,'acc':100,'pp':30},
                'Crunch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Earth Power':{'Type':"Ground",'cat':"special",'pwr':90,'acc':100,'pp':10},
                'Superpower':{'Type':"Fighting",'cat':"physical",'pwr':120,'acc':100,'pp':5}
                }},
            "NidoranM":
                {'Hp':46,'Atk':57,'Def':40,'Sp.Atk':40,'Sp.Def':40,'Speed':50,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Poison':1/2,'Bug':1/2,'Grass':1/2},
                'Moves':{
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Peck':{'Type':"Flying",'cat':"physical",'pwr':35,'acc':100,'pp':35},
                'Horn Attack':{'Type':"Normal",'cat':"physical",'pwr':65,'acc':100,'pp':25},
                'Fury Attack':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':20},
                'Double Kick':{'Type':"Fighting",'cat':"physical",'pwr':30,'acc':100,'pp':30},
                'Poison Jab':{'Type':"Poison",'cat':"physical",'pwr':80,'acc':100,'pp':20},
                'Earth Power':{'Type':"Ground",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Nidorino":
                {'Hp':61,'Atk':72,'Def':57,'Sp.Atk':55,'Sp.Def':55,'Speed':65,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Poison':1/2,'Bug':1/2,'Grass':1/2},
                'Moves':{
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Peck':{'Type':"Flying",'cat':"physical",'pwr':35,'acc':100,'pp':35},
                'Horn Attack':{'Type':"Normal",'cat':"physical",'pwr':65,'acc':100,'pp':25},
                'Fury Attack':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':20},
                'Double Kick':{'Type':"Fighting",'cat':"physical",'pwr':30,'acc':100,'pp':30},
                'Poison Jab':{'Type':"Poison",'cat':"physical",'pwr':80,'acc':100,'pp':20},
                'Earth Power':{'Type':"Ground",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Nidoking":
                {'Hp':81,'Atk':102,'Def':77,'Sp.Atk':85,'Sp.Def':75,'Speed':85,
                'Type':['Poison','Ground'],'Weakness':{'Ground':2,'Psychic':2,'Water':2,'Ice':2},
                'Immune':{'Electric':0},'Resistant':{'Fighting':1/2,'Poison':1/4,'Bug':1/2,'Rock':1/2},
                'Moves':{
                'Poison Sting':{'Type':"Poison",'cat':"physical",'pwr':15,'acc':100,'pp':35},
                'Peck':{'Type':"Flying",'cat':"physical",'pwr':35,'acc':100,'pp':35},
                'Horn Attack':{'Type':"Normal",'cat':"physical",'pwr':65,'acc':100,'pp':25},
                'Fury Attack':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':20},
                'Double Kick':{'Type':"Fighting",'cat':"physical",'pwr':30,'acc':100,'pp':30},
                'Poison Jab':{'Type':"Poison",'cat':"physical",'pwr':80,'acc':100,'pp':20},
                'Earth Power':{'Type':"Ground",'cat':"special",'pwr':90,'acc':100,'pp':10},
                'Megahorn':{'Type':'Bug','cat':'physical','pwr':120,'acc':80,'pp':10}
                }},
            "Clefairy":
                {'Hp':70,'Atk':45,'Def':48,'Sp.Atk':60,'Sp.Def':65,'Speed':35,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Pound':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'DoubleSlap':{'Type':"Normal",'cat':"physical",'pwr':30,'acc':100,'pp':10},
                }},
            "Clefable":
                {'Hp':95,'Atk':70,'Def':73,'Sp.Atk':95,'Sp.Def':90,'Speed':60,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Pound':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'DoubleSlap':{'Type':"Normal",'cat':"physical",'pwr':30,'acc':100,'pp':10},
                }},
            "Vulpix":
                {'Hp':38,'Atk':41,'Def':40,'Sp.Atk':50,'Sp.Def':65,'Speed':65,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Ember':{'Type':'Fire','cat':'special','pwr':40,'acc':100,'pp':25},
                'Quick Attack':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':30},
                'Flamethrower':{'Type':'Fire','cat':'special','pwr':95,'acc':100,'pp':15},
                'Faint Attack':{'Type':'Dark','cat':'physical','pwr':60,'acc':100,'pp':20},
                'Hex':{'Type':'Ghost','cat':'special','pwr':50,'acc':100,'pp':10},
                'Payback':{'Type':'Dark','cat':'physical','pwr':50,'acc':100,'pp':10},
                'Extrasensory':{'Type':'Psychic','cat':'special','pwr':80,'acc':100,'pp':30},
                'Fire Blast':{'Type':'Fire','cat':'special','pwr':120,'acc':85,'pp':5},
                'Inferno':{'Type':'Fire','cat':'special','pwr':100,'acc':100,'pp':25},
                'Fire Spin':{'Type':'Fire','cat':'special','pwr':35,'acc':85,'pp':15},
                'Flame Burst':{'Type':'Fire','cat':'special','pwr':70,'acc':100,'pp':15}
                }},
            "Ninetales":
                {'Hp':73,'Atk':76,'Def':75,'Sp.Atk':81,'Sp.Def':100,'Speed':100,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Ember':{'Type':'Fire','cat':'special','pwr':40,'acc':100,'pp':25},
                'Quick Attack':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':30},
                'Flamethrower':{'Type':'Fire','cat':'special','pwr':95,'acc':100,'pp':15},
                'Faint Attack':{'Type':'Dark','cat':'physical','pwr':60,'acc':100,'pp':20},
                'Hex':{'Type':'Ghost','cat':'special','pwr':50,'acc':100,'pp':10},
                'Payback':{'Type':'Dark','cat':'physical','pwr':50,'acc':100,'pp':10},
                'Extrasensory':{'Type':'Psychic','cat':'special','pwr':80,'acc':100,'pp':30},
                'Fire Blast':{'Type':'Fire','cat':'special','pwr':120,'acc':85,'pp':5},
                'Inferno':{'Type':'Fire','cat':'special','pwr':100,'acc':100,'pp':25},
                'Fire Spin':{'Type':'Fire','cat':'special','pwr':35,'acc':85,'pp':15},
                'Flame Burst':{'Type':'Fire','cat':'special','pwr':70,'acc':100,'pp':15}
                }},
            "Jigglypuff":
                {'Hp':115,'Atk':45,'Def':20,'Sp.Atk':45,'Sp.Def':25,'Speed':20,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Pound':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                'Round':{'Type':'Normal','cat':'special','pwr':60,'acc':100,'pp':15},
                'Rollout':{'Type':'Rock','cat':'physical','pwr':30,'acc':90,'pp':20},
                'DoubleSlap':{'Type':'Normal','cat':'physical','pwr':15,'acc':85,'pp':10},
                'Body Slam':{'Type':'Normal','cat':'physical','pwr':85,'acc':100,'pp':15},
                'Gyro Ball':{'Type':'Steel','cat':'physical','pwr':60,'acc':100,'pp':5},
                'Wake-Up Slap':{'Type':'Fighting','cat':'physical','pwr':60,'acc':100,'pp':10},
                'Hyper Voice':{'Type':'Normal','cat':'special','pwr':90,'acc':100,'pp':10},
                'Double-Edge':{'Type':'Normal','cat':'physical','pwr':120,'acc':100,'pp':15}
                }},
            "Wigglytuff":
                {'Hp':140,'Atk':70,'Def':45,'Sp.Atk':85,'Sp.Def':50,'Speed':45,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Pound':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                'Round':{'Type':'Normal','cat':'special','pwr':60,'acc':100,'pp':15},
                'Rollout':{'Type':'Rock','cat':'physical','pwr':30,'acc':90,'pp':20},
                'DoubleSlap':{'Type':'Normal','cat':'physical','pwr':15,'acc':85,'pp':10},
                'Body Slam':{'Type':'Normal','cat':'physical','pwr':85,'acc':100,'pp':15},
                'Gyro Ball':{'Type':'Steel','cat':'physical','pwr':60,'acc':100,'pp':5},
                'Wake-Up Slap':{'Type':'Fighting','cat':'physical','pwr':60,'acc':100,'pp':10},
                'Hyper Voice':{'Type':'Normal','cat':'special','pwr':90,'acc':100,'pp':10},
                'Double-Edge':{'Type':'Normal','cat':'physical','pwr':120,'acc':100,'pp':15}
                }},
            "Zubat":
                {'Hp':40,'Atk':45,'Def':35,'Sp.Atk':30,'Sp.Def':40,'Speed':55,
                'Type':['Poison','Flying'],'Weakness':{'Psychic':2,'Rock':2,'Electric':2,'Ice':2},
                'Immune':{'Ground':0},'Resistant':{'Fighting':1/4,'Bug':1/4,'Grass':1/4,'Poison':1/2},
                'Moves':{
                'Leech Life':{'Type':"Bug",'cat':"physical",'pwr':20,'acc':100,'pp':15},
                'Astonish':{'Type':"Ghost",'cat':"physical",'pwr':30,'acc':100,'pp':15},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Wing Attack':{'Type':"Flying",'cat':"physical",'pwr':60,'acc':100,'pp':35},
                'Swift':{'Type':"Normal",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Air Cutter':{'Type':"Flying",'cat':"special",'pwr':55,'acc':95,'pp':25},
                'Acrobatics':{'Type':"Flying",'cat':"physical",'pwr':55,'acc':100,'pp':15},
                'Poison Fang':{'Type':"Poison",'cat':"physical",'pwr':50,'acc':100,'pp':15},
                'Air Slash':{'Type':"Flying",'cat':"special",'pwr':75,'acc':95,'pp':20}
                }},
            "Golbat":
                {'Hp':75,'Atk':80,'Def':70,'Sp.Atk':65,'Sp.Def':75,'Speed':90,
                'Type':['Poison','Flying'],'Weakness':{'Psychic':2,'Rock':2,'Electric':2,'Ice':2},
                'Immune':{'Ground':0},'Resistant':{'Fighting':1/4,'Bug':1/4,'Grass':1/4,'Poison':1/2},
                'Moves':{
                'Leech Life':{'Type':"Bug",'cat':"physical",'pwr':20,'acc':100,'pp':15},
                'Astonish':{'Type':"Ghost",'cat':"physical",'pwr':30,'acc':100,'pp':15},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Wing Attack':{'Type':"Flying",'cat':"physical",'pwr':60,'acc':100,'pp':35},
                'Swift':{'Type':"Normal",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Air Cutter':{'Type':"Flying",'cat':"special",'pwr':55,'acc':95,'pp':25},
                'Acrobatics':{'Type':"Flying",'cat':"physical",'pwr':55,'acc':100,'pp':15},
                'Poison Fang':{'Type':"Poison",'cat':"physical",'pwr':50,'acc':100,'pp':15},
                'Air Slash':{'Type':"Flying",'cat':"special",'pwr':75,'acc':95,'pp':20}
                }},
            "Oddish":
                {'Hp':45,'Atk':50,'Def':55,'Sp.Atk':75,'Sp.Def':65,'Speed':30,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                'Absorb':{'Type':'Grass','cat':'special','pwr':20,'acc':100,'pp':25},
                'Acid':{'Type':'Poison','cat':'special','pwr':40,'acc':100,'pp'30},
                'Mega Drain':{'Type':'Grass','cat':'special','pwr':40,'acc':100,'pp':15},
                'Giga Drain':{'Type':'Grass','cat':'special','pwr':75,'acc':100,'pp':10},
                'Petal Dance':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10}
                }},
            "Gloom":
                {'Hp':60,'Atk':65,'Def':70,'Sp.Atk':85,'Sp.Def':75,'Speed':40,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                'Absorb':{'Type':'Grass','cat':'special','pwr':20,'acc':100,'pp':25},
                'Acid':{'Type':'Poison','cat':'special','pwr':40,'acc':100,'pp'30},
                'Mega Drain':{'Type':'Grass','cat':'special','pwr':40,'acc':100,'pp':15},
                'Giga Drain':{'Type':'Grass','cat':'special','pwr':75,'acc':100,'pp':10},
                'Petal Dance':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10}
                }},
            "Vileplume":
                {'Hp':75,'Atk':80,'Def':85,'Sp.Atk':110,'Sp.Def':90,'Speed':50,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                'Absorb':{'Type':'Grass','cat':'special','pwr':20,'acc':100,'pp':25},
                'Acid':{'Type':'Poison','cat':'special','pwr':40,'acc':100,'pp'30},
                'Mega Drain':{'Type':'Grass','cat':'special','pwr':40,'acc':100,'pp':15},
                'Giga Drain':{'Type':'Grass','cat':'special','pwr':75,'acc':100,'pp':10},
                'Petal Dance':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10},
                'Solar Beam':{'Type':'Grass','cat':'special','pwr':120,'acc':100,'pp':10}
                }},
            "Paras":
                {'Hp':35,'Atk':70,'Def':55,'Sp.Atk':45,'Sp.Def':55,'Speed':25,
                'Type':['Bug','Grass'],'Weakness':{'Flying':4,'Fire':4,'Rock':2,'Ice':2,'Bug':2,'Poison':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2,'Ground':1/4},
                'Moves':{
                'Scratch':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                'Leech Life':{'Type':'Bug','cat':'physical','pwr':20,'acc':100,'pp':15},
                'Fury Cutter':{'Type':'Bug','cat':'physical','pwr':20,'acc':95,'pp':20},
                'Slash':{'Type':'Normal','cat':'physical','pwr':70,'acc':100,'pp':20},
                'Giga Drain':{'Type':'Grass','cat':'special','pwr':75,'acc':100,'pp':10},
                'X-Scissor':{'Type':'Bug','cat':'physical','pwr':80,'acc':100,'pp':15}
                }},
            "Parasect":
                {'Hp':60,'Atk':95,'Def':80,'Sp.Atk':60,'Sp.Def':80,'Speed':30,
                'Type':['Bug','Grass'],'Weakness':{'Flying':4,'Fire':4,'Rock':2,'Ice':2,'Bug':2,'Poison':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2,'Ground':1/4},
                'Moves':{
                'Cross Poison':{'Type':'Poison','cat':'physical','pwr':70,'acc':100,'pp':20},
                'Scratch':{'Type':'Normal','cat':'physical','pwr':40,'acc':100,'pp':35},
                'Leech Life':{'Type':'Bug','cat':'physical','pwr':20,'acc':100,'pp':15},
                'Fury Cutter':{'Type':'Bug','cat':'physical','pwr':20,'acc':95,'pp':20},
                'Slash':{'Type':'Normal','cat':'physical','pwr':70,'acc':100,'pp':20},
                'Giga Drain':{'Type':'Grass','cat':'special','pwr':75,'acc':100,'pp':10},
                'X-Scissor':{'Type':'Bug','cat':'physical','pwr':80,'acc':100,'pp':15}
                }},
            "Venonat":
                {'Hp':60,'Atk':55,'Def':50,'Sp.Atk':40,'Sp.Def':55,'Speed':45,
                'Type':['Bug','Poison'],'Weakness':{'Flying':2,'Rock':2,'Fire':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/4,'Poison':1/2,'Grass':1/4,'Bug':1/2},
                'Moves':{
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':50,'acc':100,'pp':35},
                'Confusion':{'Type':"Psychic",'cat':"special",'pwr':50,'acc':100,'pp':25},
                'Leech Life':{'Type':"Bug",'cat':"physical",'pwr':20,'acc':100,'pp':15},
                'Psybeam':{'Type':"Psychic",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Signal Beam':{'Type':"Bug",'cat':"special",'pwr':75,'acc':100,'pp':15},
                'Zen Headbutt':{'Type':"Psychic",'cat':"physical",'pwr':80,'acc':90,'pp':15},
                'Poison Fang':{'Type':"Poison",'cat':"physical",'pwr':50,'acc':100,'pp':15},
                'Psychic':{'Type':"Psychic",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Venomoth":
                {'Hp':70,'Atk':65,'Def':60,'Sp.Atk':90,'Sp.Def':75,'Speed':90,
                'Type':['Bug','Poison'],'Weakness':{'Flying':2,'Rock':2,'Fire':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/4,'Poison':1/2,'Grass':1/4,'Bug':1/2},
                'Moves':{
                'Silver Wind':{'Type':"Bug",'cat':"special",'pwr':60,'acc':100,'pp':5},
                'Tackle':{'Type':"Normal",'cat':"physical",'pwr':50,'acc':100,'pp':35},
                'Confusion':{'Type':"Psychic",'cat':"special",'pwr':50,'acc':100,'pp':25},
                'Leech Life':{'Type':"Bug",'cat':"physical",'pwr':20,'acc':100,'pp':15},
                'Psybeam':{'Type':"Psychic",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Gust':{'Type':"Flying",'cat':"special",'pwr':40,'acc':100,'pp':35},
                'Signal Beam':{'Type':"Bug",'cat':"special",'pwr':75,'acc':100,'pp':15},
                'Zen Headbutt':{'Type':"Psychic",'cat':"physical",'pwr':80,'acc':90,'pp':15},
                'Poison Fang':{'Type':"Poison",'cat':"physical",'pwr':50,'acc':100,'pp':15},
                'Psychic':{'Type':"Psychic",'cat':"special",'pwr':90,'acc':100,'pp':10}
                'Bug Buzz':{'Type':"Bug",'cat':"special",'pwr':90,'acc':100,'pp':10},
                }},
            "Diglett":
                {'Hp':10,'Atk':55,'Def':25,'Sp.Atk':35,'Sp.Def':45,'Speed':95,
                'Type':['Ground'],'Weakness':{'Water':2,'Grass':2,'Ice':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/2,'Rock':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Astonish':{'Type':"Ghost",'cat':"physical",'pwr':30,'acc':100,'pp':45},
                'Mud-Slap':{'Type':"Ground",'cat':"special",'pwr':20,'acc':90,'pp':10},
                'Magnitude':{'Type':"Ground",'cat':"physical",'pwr':70,'acc':95,'pp':30},
                'Bulldoze':{'Type':"Ground",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Sucker Punch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':5},
                'Mud Bomb':{'Type':"Ground",'cat':"special",'pwr':65,'acc':100,'pp':10},
                'Earth Power':{'Type':"Ground",'cat':"special",'pwr':90,'acc':80,'pp':10},
                'Dig':{'Type':"Ground",'cat':"physical",'pwr':80,'acc':100,'pp':10},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Fissure':{'Type':"Ground",'cat':"physical",'pwr':0,'acc':100,'pp':5},
                'Earthquake':{'Type':"Ground",'cat':"physical",'pwr':100,'acc':100,'pp':10}
                }},
            "Dugtrio":
                {'Hp':35,'Atk':100,'Def':50,'Sp.Atk':50,'Sp.Def':70,'Speed':120,
                'Type':['Ground'],'Weakness':{'Water':2,'Grass':2,'Ice':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/2,'Rock':1/2},
                'Moves':{
                'Night Slash':{'Type':"Dark",'cat':"physical",'pwr':70,'acc':100,'pp':15},
                'Tri Attack':{'Type':"Normal",'cat':"special",'pwr':80,'acc':100,'pp':10},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Astonish':{'Type':"Ghost",'cat':"physical",'pwr':30,'acc':100,'pp':45},
                'Mud-Slap':{'Type':"Ground",'cat':"special",'pwr':20,'acc':90,'pp':10},
                'Magnitude':{'Type':"Ground",'cat':"physical",'pwr':70,'acc':95,'pp':30},
                'Bulldoze':{'Type':"Ground",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Sucker Punch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':5},
                'Sand Tomb':{'Type':"Ground",'cat':"physical",'pwr':35,'acc':85,'pp':15},
                'Mud Bomb':{'Type':"Ground",'cat':"special",'pwr':65,'acc':100,'pp':10},
                'Earth Power':{'Type':"Ground",'cat':"special",'pwr':90,'acc':80,'pp':10},
                'Dig':{'Type':"Ground",'cat':"physical",'pwr':80,'acc':100,'pp':10},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Fissure':{'Type':"Ground",'cat':"physical",'pwr':0,'acc':100,'pp':5},
                'Earthquake':{'Type':"Ground",'cat':"physical",'pwr':100,'acc':100,'pp':10}
                }},
            "Meowth":
                {'Hp':40,'Atk':45,'Def':35,'Sp.Atk':40,'Sp.Def':40,'Speed':90,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Fake Out':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':10},
                'Feint':{'Type':"Normal",'cat':"physical",'pwr':30,'acc':100,'pp':10},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Pay Day':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':20},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':50,'acc':100,'pp':10},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Faint Attack':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Night Slash':{'Type':'Dark','cat':"physical",'pwr':70,'acc':100,'pp':15}
                }},
            "Persian":
                {'Hp':65,'Atk':70,'Def':60,'Sp.Atk':65,'Sp.Def':65,'Speed':115,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Fake Out':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':10},
                'Feint':{'Type':"Normal",'cat':"physical",'pwr':30,'acc':100,'pp':10},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Power Gem':{'Type':"Rock",'cat':"special",'pwr':70,'acc':100,'pp':20},
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':50,'acc':100,'pp':10},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Slash':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Faint Attack':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Night Slash':{'Type':'Dark','cat':"physical",'pwr':70,'acc':100,'pp':15}
                }},
            "Psyduck":
                {'Hp':50,'Atk':52,'Def':48,'Sp.Atk':65,'Sp.Def':50,'Speed':55,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Water Gun':{'Type':"Water",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Confusion':{'Type':"Psychic",'cat':"special",'pwr':50,'acc':100,'pp':25},
                'Water Pulse':{'Type':"Water",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Zen Headbutt':{'Type':"Psychic",'cat':"physical",'pwr':80,'acc':90,'pp':15},
                'Aqua Tail':{'Type':"Water",'cat':"physical",'pwr':90,'acc':90,'pp':10},
                'Hydro Pump':{'Type':"Water",'cat':"special",'pwr':120,'acc':80,'pp':5}
                }},
            "Golduck":
                {'Hp':80,'Atk':82,'Def':78,'Sp.Atk':95,'Sp.Def':80,'Speed':85,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Aqua Jet':{'Type':"Water",'cat':"physical",'pwr':40,'acc':90,'pp':20},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Water Gun':{'Type':"Water",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Confusion':{'Type':"Psychic",'cat':"special",'pwr':50,'acc':100,'pp':25},
                'Water Pulse':{'Type':"Water",'cat':"special",'pwr':60,'acc':100,'pp':20},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Zen Headbutt':{'Type':"Psychic",'cat':"physical",'pwr':80,'acc':90,'pp':15},
                'Aqua Tail':{'Type':"Water",'cat':"physical",'pwr':90,'acc':90,'pp':10},
                'Hydro Pump':{'Type':"Water",'cat':"special",'pwr':120,'acc':80,'pp':5}
                }},
            "Mankey":
                {'Hp':40,'Atk':80,'Def':35,'Sp.Atk':35,'Sp.Def':45,'Speed':70,
                'Type':['Fighting'],'Weakness':{'Flying':2,'Psychic':2},
                'Immune':{},'Resistant':{'Rock':1/2,'Bug':1/2,'Dark':1/2},
                'Moves':{
                'Covet':{'Type':"Normal",'cat':"physical",'pwr':60,'acc':100,'pp':40},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Low Kick':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Karate Chop':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':25},
                'Seismic Toss':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':20},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':50,'acc':100,'pp':10},
                'Cross Chop':{'Type':"Fighing",'cat':"physical",'pwr':100,'acc':80,'pp':5},
                'Thrash':{'Type':"Normal",'cat':"physical",'pwr':120,'acc':100,'pp':10},
                'Close Combat':{'Type':"Fighing",'cat':"physical",'pwr':120,'acc':100,'pp':5}
                }},
            "Primeape":
                {'Hp':65,'Atk':105,'Def':60,'Sp.Atk':60,'Sp.Def':70,'Speed':95,
                'Type':['Fighting'],'Weakness':{'Flying':2,'Psychic':2},
                'Immune':{},'Resistant':{'Rock':1/2,'Bug':1/2,'Dark':1/2},
                'Moves':{
                'Covet':{'Type':"Normal",'cat':"physical",'pwr':60,'acc':100,'pp':40},
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                'Low Kick':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Fury Swipes':{'Type':"Normal",'cat':"physical",'pwr':18,'acc':80,'pp':15},
                'Karate Chop':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':25},
                'Seismic Toss':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':20},
                'Assurance':{'Type':"Dark",'cat':"physical",'pwr':50,'acc':100,'pp':10},
                'Rage':{'Type':'Normal','cat':'physical','pwr':20,'acc':100,'pp':20},
                'Cross Chop':{'Type':"Fighing",'cat':"physical",'pwr':100,'acc':80,'pp':5},
                'Thrash':{'Type':"Normal",'cat':"physical",'pwr':120,'acc':100,'pp':10},
                'Close Combat':{'Type':"Fighing",'cat':"physical",'pwr':120,'acc':100,'pp':5}
                }},
            "Growlithe":
                {'Hp':55,'Atk':70,'Def':45,'Sp.Atk':70,'Sp.Def':50,'Speed':60,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Ember':{'Type':"Fire",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Flame Wheel':{'Type':"Fire",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Fire Fang':{'Type':"Fire",'cat':"physical",'pwr':65,'acc':95,'pp':15},
                'Take Down':{'Type':"Normal",'cat':"physical",'pwr':90,'acc':85,'pp':20},
                'Flame Burst':{'Type':"Fire",'cat':"special",'pwr':70,'acc':100,'pp':15},
                'Retaliate':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':5},
                'Flamethrower':{'Type':"Fire",'cat':"special",'pwr':95,'acc':100,'pp':15},
                'Crunch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Heat Wave':{'Type':"Fire",'cat':"special",'pwr':100,'acc':90,'pp':10},
                'Outrage':{'Type':"Dragon",'cat':"physical",'pwr':120,'acc':100,'pp':10},
                'Flare Blitz':{'Type':"Fire",'cat':"physical",'pwr':120,'acc':100,'pp':15}
                }},
            "Arcanine":
                {'Hp':90,'Atk':110,'Def':80,'Sp.Atk':100,'Sp.Def':80,'Speed':95,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Bite':{'Type':"Dark",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Ember':{'Type':"Fire",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Flame Wheel':{'Type':"Fire",'cat':"physical",'pwr':60,'acc':100,'pp':25},
                'Fire Fang':{'Type':"Fire",'cat':"physical",'pwr':65,'acc':95,'pp':15},
                'Take Down':{'Type':"Normal",'cat':"physical",'pwr':90,'acc':85,'pp':20},
                'Flame Burst':{'Type':"Fire",'cat':"special",'pwr':70,'acc':100,'pp':15},
                'Retaliate':{'Type':"Normal",'cat':"physical",'pwr':70,'acc':100,'pp':5},
                'Flamethrower':{'Type':"Fire",'cat':"special",'pwr':95,'acc':100,'pp':15},
                'Crunch':{'Type':"Dark",'cat':"physical",'pwr':80,'acc':100,'pp':15},
                'Heat Wave':{'Type':"Fire",'cat':"special",'pwr':100,'acc':90,'pp':10},
                'Outrage':{'Type':"Dragon",'cat':"physical",'pwr':120,'acc':100,'pp':10},
                'Flare Blitz':{'Type':"Fire",'cat':"physical",'pwr':120,'acc':100,'pp':15},
                'Thunder Fang':{'Type':"Electric",'cat':"physical",'pwr':65,'acc':95,'pp':25},
                'Extreme Speed':{'Type':"Normal",'cat':"physical",'pwr':80,'acc':100,'pp':5},
                }},
            "Poliwag":
                {'Hp':40,'Atk':50,'Def':40,'Sp.Atk':40,'Sp.Def':40,'Speed':90,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Bubble':{'Type':"Water",'cat':"special",'pwr':20,'acc':100,'pp':30},
                'Water Gun':{'Type':"Water",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Double Slap':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':10},
                'Body Slam':{'Type':"Normal",'cat':"physical",'pwr':85,'acc':100,'pp':15},
                'Bubble Beam':{'Type':"Water",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Mud Shot':{'Type':"Ground",'cat':"special",'pwr':95,'acc':95,'pp':15},
                'Wake-Up Slap':{'Type':"Fighting",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Hydro Pump':{'Type':"Water",'cat':"special",'pwr':120,'acc':80,'pp':5}
                'Mud Bomb':{'Type':"Ground",'cat':"special",'pwr':65,'acc':85,'pp':10}
                }},
            "Poliwhirl":
                {'Hp':65,'Atk':65,'Def':65,'Sp.Atk':50,'Sp.Def':50,'Speed':90,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Bubble':{'Type':"Water",'cat':"special",'pwr':20,'acc':100,'pp':30},
                'Water Gun':{'Type':"Water",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Double Slap':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':10},
                'Body Slam':{'Type':"Normal",'cat':"physical",'pwr':85,'acc':100,'pp':15},
                'Bubble Beam':{'Type':"Water",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Mud Shot':{'Type':"Ground",'cat':"special",'pwr':95,'acc':95,'pp':15},
                'Wake-Up Slap':{'Type':"Fighting",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Hydro Pump':{'Type':"Water",'cat':"special",'pwr':120,'acc':80,'pp':5}
                'Mud Bomb':{'Type':"Ground",'cat':"special",'pwr':65,'acc':85,'pp':10}
                }},
            "Poliwrath":
                {'Hp':80,'Atk':82,'Def':78,'Sp.Atk':95,'Sp.Def':80,'Speed':85,
                'Type':['Water','Fighting'],'Weakness':{'Grass':2,'Electric':2,'Psychic':2,'Flying':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2,'Rock':1/2,'Bug':1/2,'Dark':1/2},
                'Moves':{
                'Bubble':{'Type':"Water",'cat':"special",'pwr':20,'acc':100,'pp':30},
                'Water Gun':{'Type':"Water",'cat':"special",'pwr':40,'acc':100,'pp':25},
                'Double Slap':{'Type':"Normal",'cat':"physical",'pwr':15,'acc':85,'pp':10},
                'Body Slam':{'Type':"Normal",'cat':"physical",'pwr':85,'acc':100,'pp':15},
                'Bubble Beam':{'Type':"Water",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Mud Shot':{'Type':"Ground",'cat':"special",'pwr':95,'acc':95,'pp':15},
                'Wake-Up Slap':{'Type':"Fighting",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Hydro Pump':{'Type':"Water",'cat':"special",'pwr':120,'acc':80,'pp':5}
                'Mud Bomb':{'Type':"Ground",'cat':"special",'pwr':65,'acc':85,'pp':10}
                'Submission':{'Type':"Fighting",'cat':"physical",'pwr':80,'acc':80,'pp':25},
                'Dynamic Punch':{'Type':"Fighting",'cat':"physical",'pwr':100,'acc':50,'pp':5},
                'Circle Throw':{'Type':"Fighting",'cat':"physical",'pwr':60,'acc':90,'pp':10}
                }},
            "Abra":
                {'Hp':25,'Atk':20,'Def':15,'Sp.Atk':105,'Sp.Def':55,'Speed':90,
                'Type':['Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Confusion':{'Type':"Psychic",'cat':"special",'pwr':50,'acc':100,'pp':25},
                'Psybeam':{'Type':"Psychic",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Psycho Cut':{'Type':"Psychic",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Future Sight':{'Type':"Psychic",'cat':"special",'pwr':100,'acc':100,'pp':10},
                'Psychic':{'Type':"Psychic",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Kadabra":
                {'Hp':40,'Atk':35,'Def':30,'Sp.Atk':120,'Sp.Def':70,'Speed':105,
                'Type':['Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Confusion':{'Type':"Psychic",'cat':"special",'pwr':50,'acc':100,'pp':25},
                'Psybeam':{'Type':"Psychic",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Psycho Cut':{'Type':"Psychic",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Future Sight':{'Type':"Psychic",'cat':"special",'pwr':100,'acc':100,'pp':10},
                'Psychic':{'Type':"Psychic",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Alakazam":
                {'Hp':55,'Atk':50,'Def':45,'Sp.Atk':135,'Sp.Def':95,'Speed':120,
                'Type':['Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Confusion':{'Type':"Psychic",'cat':"special",'pwr':50,'acc':100,'pp':25},
                'Psybeam':{'Type':"Psychic",'cat':"special",'pwr':65,'acc':100,'pp':20},
                'Psycho Cut':{'Type':"Psychic",'cat':"physical",'pwr':70,'acc':100,'pp':20},
                'Future Sight':{'Type':"Psychic",'cat':"special",'pwr':100,'acc':100,'pp':10},
                'Psychic':{'Type':"Psychic",'cat':"special",'pwr':90,'acc':100,'pp':10}
                }},
            "Machop":
                {'Hp':70,'Atk':80,'Def':50,'Sp.Atk':35,'Sp.Def':35,'Speed':35,
                'Type':['Fighting'],'Weakness':{'Flying':2,'Psychic':2},
                'Immune':{},'Resistant':{'Rock':1/2,'Bug':1/2,'Dark':1/2},
                'Moves':{
                'Low Kick':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Karate Chop':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':25},
                'Low Sweep':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Seismic Toss':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':20},
                'Revenge':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Vital Throw':{'Type':"Fighing",'cat':"physical",'pwr':70,'acc':100,'pp':10},
                'Submission':{'Type':"Fighing",'cat':"physical",'pwr':80,'acc':80,'pp':25},
                'Wake-Up Slap':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Cross Chop':{'Type':"Fighing",'cat':"physical",'pwr':100,'acc':80,'pp':5},
                'Dynamic Punch':{'Type':"Fighing",'cat':"physical",'pwr':100,'acc':50,'pp':5}
                }},
            "Machoke":
                {'Hp':80,'Atk':100,'Def':70,'Sp.Atk':50,'Sp.Def':60,'Speed':45,
                'Type':['Fighting'],'Weakness':{'Flying':2,'Psychic':2},
                'Immune':{},'Resistant':{'Rock':1/2,'Bug':1/2,'Dark':1/2},
                'Moves':{
                'Low Kick':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Karate Chop':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':25},
                'Low Sweep':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Seismic Toss':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':20},
                'Revenge':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Vital Throw':{'Type':"Fighing",'cat':"physical",'pwr':70,'acc':100,'pp':10},
                'Submission':{'Type':"Fighing",'cat':"physical",'pwr':80,'acc':80,'pp':25},
                'Wake-Up Slap':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Cross Chop':{'Type':"Fighing",'cat':"physical",'pwr':100,'acc':80,'pp':5},
                'Dynamic Punch':{'Type':"Fighing",'cat':"physical",'pwr':100,'acc':50,'pp':5}
                }},
            "Machamp":
                {'Hp':90,'Atk':130,'Def':80,'Sp.Atk':65,'Sp.Def':85,'Speed':55,
                'Type':['Fighting'],'Weakness':{'Flying':2,'Psychic':2},
                'Immune':{},'Resistant':{'Rock':1/2,'Bug':1/2,'Dark':1/2},
                'Moves':{
                'Low Kick':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Karate Chop':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':25},
                'Low Sweep':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':20},
                'Seismic Toss':{'Type':"Fighing",'cat':"physical",'pwr':50,'acc':100,'pp':20},
                'Revenge':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Vital Throw':{'Type':"Fighing",'cat':"physical",'pwr':70,'acc':100,'pp':10},
                'Submission':{'Type':"Fighing",'cat':"physical",'pwr':80,'acc':80,'pp':25},
                'Wake-Up Slap':{'Type':"Fighing",'cat':"physical",'pwr':60,'acc':100,'pp':10},
                'Cross Chop':{'Type':"Fighing",'cat':"physical",'pwr':100,'acc':80,'pp':5},
                'Dynamic Punch':{'Type':"Fighing",'cat':"physical",'pwr':100,'acc':50,'pp':5}
                }},
            "Bellsprout":
                {'Hp':50,'Atk':75,'Def':35,'Sp.Atk':70,'Sp.Def':30,'Speed':40,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                'Wrap':{'Type':'Normal','cat':'physical','pwr':15,'acc':90,'pp':20},
                'Vine Whip':{'Type':'Grass','cat':'physical','pwr':35,'acc':100,'pp':15},
                'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                'Acid':{'Type':'Poison','cat':'special','pwr':40,'acc':100,'pp':30},
                'Knock Off':{'Type':'Dark','cat':'physical','pwr':20,'acc':100,'pp':20},
                'Slam':{'Type':'Normal','cat':'physical','pwr':80,'acc':75,'pp':20}
                }},
            "Weepinbell":
                {'Hp':65,'Atk':90,'Def':50,'Sp.Atk':85,'Sp.Def':45,'Speed':55,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                'Wrap':{'Type':'Normal','cat':'physical','pwr':15,'acc':90,'pp':20},
                'Vine Whip':{'Type':'Grass','cat':'physical','pwr':35,'acc':100,'pp':15},
                'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                'Acid':{'Type':'Poison','cat':'special','pwr':40,'acc':100,'pp':30},
                'Knock Off':{'Type':'Dark','cat':'physical','pwr':20,'acc':100,'pp':20},
                'Slam':{'Type':'Normal','cat':'physical','pwr':80,'acc':75,'pp':20}
                }},
            "Victreebel":
                {'Hp':80,'Atk':105,'Def':65,'Sp.Atk':100,'Sp.Def':70,'Speed':70,
                'Type':['Grass','Poison'],'Weakness':{'Flying':2,'Fire':2,'Psychic':2,'Ice':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Water':1/2,'Grass':1/4,'Electric':1/2},
                'Moves':{
                'Wrap':{'Type':'Normal','cat':'physical','pwr':15,'acc':90,'pp':20},
                'Vine Whip':{'Type':'Grass','cat':'physical','pwr':35,'acc':100,'pp':15},
                'Razor Leaf':{'Type':'Grass','cat':'physical','pwr':55,'acc':95,'pp':25},
                'Leaf Tornado':{'Type':'Grass','cat':'special','pwr':65,'acc':90,'pp':10},
                'Leaf Storm':{'Type':'Grass','cat':'special','pwr':140,'acc':90,'pp':5},
                'Leaf Blade':{'Type':'Grass','cat':'physical','pwr':90,'acc':100,'pp':15}
                }},
            "Tentacool":
                {'Hp':40,'Atk':40,'Def':35,'Sp.Atk':50,'Sp.Def':100,'Speed':70,
                'Type':['Water','Poison'],'Weakness':{'Ground':2,'Electric':2,'Psychic':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2,'Fighting':1/2,'Poison':1/2,'Bug':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Tentacruel":
                {'Hp':80,'Atk':70,'Def':65,'Sp.Atk':80,'Sp.Def':120,'Speed':100,
                'Type':['Water','Poison'],'Weakness':{'Ground':2,'Electric':2,'Psychic':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2,'Fighting':1/2,'Poison':1/2,'Bug':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Geodude":
                {'Hp':40,'Atk':80,'Def':100,'Sp.Atk':30,'Sp.Def':30,'Speed':20,
                'Type':['Rock','Ground'],'Weakness':{'Water':4,'Grass':4,'Ice':2,'Ground':2,'Fighting':2,'Steel':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/4,'Rock':1/2,'Flying':1/2,'Normal':1/2,'Fire':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Graveler":
                {'Hp':55,'Atk':95,'Def':115,'Sp.Atk':45,'Sp.Def':45,'Speed':35,
                'Type':['Rock','Ground'],'Weakness':{'Water':4,'Grass':4,'Ice':2,'Ground':2,'Fighting':2,'Steel':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/4,'Rock':1/2,'Flying':1/2,'Normal':1/2,'Fire':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Golem":
                {'Hp':80,'Atk':110,'Def':130,'Sp.Atk':55,'Sp.Def':65,'Speed':45,
                'Type':['Rock','Ground'],'Weakness':{'Water':4,'Grass':4,'Ice':2,'Ground':2,'Fighting':2,'Steel':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/4,'Rock':1/2,'Flying':1/2,'Normal':1/2,'Fire':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Ponyta":
                {'Hp':50,'Atk':85,'Def':55,'Sp.Atk':65,'Sp.Def':65,'Speed':90,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                }},
            "Rapidash":
                {'Hp':65,'Atk':100,'Def':70,'Sp.Atk':80,'Sp.Def':80,'Speed':105,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                }},
            "Slowpoke":
                {'Hp':90,'Atk':65,'Def':65,'Sp.Atk':40,'Sp.Def':40,'Speed':15,
                'Type':['Water','Psychic'],'Weakness':{'Grass':2,'Electric':2,'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2,'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Slowbro":
                {'Hp':95,'Atk':75,'Def':110,'Sp.Atk':100,'Sp.Def':80,'Speed':30,
                'Type':['Water','Psychic'],'Weakness':{'Grass':2,'Electric':2,'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2,'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Magnemite":
                {'Hp':25,'Atk':35,'Def':70,'Sp.Atk':95,'Sp.Def':55,'Speed':45,
                'Type':['Electric','Steel'],'Weakness':{'Fighting':2,'Ground':4,'Fire':2},
                'Immune':{'Poison':0},'Resistant':{'Grass':1/2,'Bug':1/2,'Normal':1/2,'Flying':1/4,'Rock':1/2,'Steel':1/4,'Electric':1/2,'Psychic':1/2,'Ice':1/2,'Dragon':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Magneton":
                {'Hp':50,'Atk':60,'Def':95,'Sp.Atk':120,'Sp.Def':70,'Speed':70,
                'Type':['Electric','Steel'],'Weakness':{'Fighting':2,'Ground':4,'Fire':2},
                'Immune':{'Poison':0},'Resistant':{'Grass':1/2,'Bug':1/2,'Normal':1/2,'Flying':1/4,'Rock':1/2,'Steel':1/4,'Electric':1/2,'Psychic':1/2,'Ice':1/2,'Dragon':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Farfetch'd":
                {'Hp':52,'Atk':90,'Def':55,'Sp.Atk':58,'Sp.Def':62,'Speed':60,
                'Type':['Normal','Flying'],'Weakness':{'Electric':2,'Rock':2,'Ice':2},
                'Immune':{'Ground':0,'Ghost':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Doduo":
                {'Hp':35,'Atk':85,'Def':45,'Sp.Atk':35,'Sp.Def':35,'Speed':75,
                'Type':['Normal','Flying'],'Weakness':{'Electric':2,'Rock':2,'Ice':2},
                'Immune':{'Ground':0,'Ghost':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},                
            "Dodrio":
                {'Hp':60,'Atk':110,'Def':70,'Sp.Atk':60,'Sp.Def':60,'Speed':110,
                'Type':['Normal','Flying'],'Weakness':{'Electric':2,'Rock':2,'Ice':2},
                'Immune':{'Ground':0,'Ghost':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Seel":
                {'Hp':65,'Atk':45,'Def':55,'Sp.Atk':45,'Sp.Def':70,'Speed':45,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Dewgong":
                {'Hp':90,'Atk':70,'Def':80,'Sp.Atk':70,'Sp.Def':95,'Speed':70,
                'Type':['Water','Ice'],'Weakness':{'Grass':2,'Electric':2,'Fighting':2,'Rock':2},
                'Immune':{},'Resistant':{'Water':1/2,'Ice':1/4},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Grimer":
                {'Hp':80,'Atk':80,'Def':50,'Sp.Atk':40,'Sp.Def':50,'Speed':25,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Poison':1/2,'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Move'
                }},
            "Muk":
                {'Hp':105,'Atk':105,'Def':75,'Sp.Atk':65,'Sp.Def':100,'Speed':50,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Poison':1/2,'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Move'
                }},
            "Shellder":
                {'Hp':30,'Atk':65,'Def':100,'Sp.Atk':45,'Sp.Def':25,'Speed':40,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Cloyster":
                {'Hp':50,'Atk':95,'Def':180,'Sp.Atk':85,'Sp.Def':45,'Speed':70,
                'Type':['Water','Ice'],'Weakness':{'Grass':2,'Electric':2,'Fighting':2,'Rock':2},
                'Immune':{},'Resistant':{'Water':1/2,'Ice':1/4},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Gastly":
                {'Hp':30,'Atk':35,'Def':30,'Sp.Atk':100,'Sp.Def':35,'Speed':80,
                'Type':['Ghost','Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{'Normal':0,'Fighting':0,'Ground':0},'Resistant':{'Bug':1/4,'Poison':1/4,'Grass':1/2},
                'Moves':{
                'Move'
                }},
            "Haunter":
                {'Hp':45,'Atk':50,'Def':45,'Sp.Atk':115,'Sp.Def':55,'Speed':95,
                'Type':['Ghost','Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{'Normal':0,'Fighting':0,'Ground':0},'Resistant':{'Bug':1/4,'Poison':1/4,'Grass':1/2},
                'Moves':{
                'Move'
                }},
            "Gengar":
                {'Hp':60,'Atk':65,'Def':60,'Sp.Atk':130,'Sp.Def':75,'Speed':110,
                'Type':['Ghost','Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{'Normal':0,'Fighting':0,'Ground':0},'Resistant':{'Bug':1/4,'Poison':1/4,'Grass':1/2},
                'Moves':{
                'Move'
                }},
            "Onix":
                {'Hp':35,'Atk':45,'Def':160,'Sp.Atk':30,'Sp.Def':45,'Speed':70,
                'Type':['Rock','Ground'],'Weakness':{'Water':4,'Grass':4,'Ice':2,'Ground':2,'Fighting':2,'Steel':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/4,'Rock':1/2,'Flying':1/2,'Normal':1/2,'Fire':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Drowzee":
                {'Hp':60,'Atk':48,'Def':45,'Sp.Atk':43,'Sp.Def':90,'Speed':42,
                'Type':['Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Hypno":
                {'Hp':85,'Atk':73,'Def':70,'Sp.Atk':73,'Sp.Def':115,'Speed':67,
                'Type':['Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Krabby":
                {'Hp':30,'Atk':105,'Def':90,'Sp.Atk':25,'Sp.Def':25,'Speed':50,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Kingler":
                {'Hp':55,'Atk':130,'Def':115,'Sp.Atk':50,'Sp.Def':50,'Speed':75,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Voltorb":
                {'Hp':40,'Atk':30,'Def':50,'Sp.Atk':55,'Sp.Def':55,'Speed':100,
                'Type':['Electric'],'Weakness':{'Ground':2},
                'Immune':{},'Resistant':{'Flying':1/2,'Steel':1/2,'Electric':1/2},
                'Moves':{
                'Move':
                }},
            "Electrode":
                {'Hp':60,'Atk':50,'Def':70,'Sp.Atk':80,'Sp.Def':80,'Speed':150,
                'Type':['Electric'],'Weakness':{'Ground':2},
                'Immune':{},'Resistant':{'Flying':1/2,'Steel':1/2,'Electric':1/2},
                'Moves':{
                'Move':
                }},
            "Exeggcute":
                {'Hp':60,'Atk':40,'Def':80,'Sp.Atk':60,'Sp.Def':45,'Speed':40,
                'Type':['Grass','Psychic'],'Weakness':{'Bug':4,'Ghost':2,'Dark':2,'Poison':2,'Ice':2,'Flying':2,'Fire':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2,'Electric':1/2,'Ground':1/2,'Water':1/2,'Grass':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Exeggutor":
                {'Hp':95,'Atk':105,'Def':85,'Sp.Atk':125,'Sp.Def':75,'Speed':45,
                'Type':['Grass','Psychic'],'Weakness':{'Bug':4,'Ghost':2,'Dark':2,'Poison':2,'Ice':2,'Flying':2,'Fire':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2,'Electric':1/2,'Ground':1/2,'Water':1/2,'Grass':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Cubone":
                {'Hp':50,'Atk':50,'Def':95,'Sp.Atk':40,'Sp.Def':50,'Speed':35,
                'Type':['Ground'],'Weakness':{'Water':2,'Grass':2,'Ice':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/2,'Rock':1/2},
                'Moves':{
                'Move':
                }},
            "Marowak":
                {'Hp':60,'Atk':80,'Def':110,'Sp.Atk':50,'Sp.Def':80,'Speed':45,
                'Type':['Ground'],'Weakness':{'Water':2,'Grass':2,'Ice':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/2,'Rock':1/2},
                'Moves':{
                'Move':
                }},
            "Hitmonlee":
                {'Hp':50,'Atk':120,'Def':53,'Sp.Atk':35,'Sp.Def':110,'Speed':87,
                'Type':['Fighting'],'Weakness':{'Flying':2,'Psychic':2},
                'Immune':{},'Resistant':{'Rock':1/2,'Bug':1/2,'Dark':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Hitmonchan":
                {'Hp':50,'Atk':105,'Def':79,'Sp.Atk':35,'Sp.Def':110,'Speed':76,
                'Type':['Fighting'],'Weakness':{'Flying':2,'Psychic':2},
                'Immune':{},'Resistant':{'Rock':1/2,'Bug':1/2,'Dark':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Lickitung":
                {'Hp':90,'Atk':55,'Def':75,'Sp.Atk':60,'Sp.Def':75,'Speed':30,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Move':
                }},
            "Koffing":
                {'Hp':40,'Atk':65,'Def':95,'Sp.Atk':60,'Sp.Def':45,'Speed':35,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Poison':1/2,'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Move'
                }},
            "Weezing":
                {'Hp':65,'Atk':90,'Def':120,'Sp.Atk':85,'Sp.Def':70,'Speed':60,
                'Type':['Poison'],'Weakness':{'Ground':2,'Psychic':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Poison':1/2,'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Move'
                }},
            "Rhyhorn":
                {'Hp':80,'Atk':85,'Def':95,'Sp.Atk':30,'Sp.Def':30,'Speed':25,
                'Type':['Rock','Ground'],'Weakness':{'Water':4,'Grass':4,'Ice':2,'Ground':2,'Fighting':2,'Steel':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/4,'Rock':1/2,'Flying':1/2,'Normal':1/2,'Fire':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Rhydon":
                {'Hp':105,'Atk':130,'Def':120,'Sp.Atk':45,'Sp.Def':45,'Speed':40,
                'Type':['Rock','Ground'],'Weakness':{'Water':4,'Grass':4,'Ice':2,'Ground':2,'Fighting':2,'Steel':2},
                'Immune':{'Electric':0},'Resistant':{'Poison':1/4,'Rock':1/2,'Flying':1/2,'Normal':1/2,'Fire':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Chansey":
                {'Hp':250,'Atk':5,'Def':5,'Sp.Atk':35,'Sp.Def':105,'Speed':50,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Move':
                }},
            "Tangela":
                {'Hp':65,'Atk':55,'Def':115,'Sp.Atk':100,'Sp.Def':40,'Speed':60,
                'Type':['Grass'],'Weakness':{'Flying':2,'Fire':2,'Poison':2,'Ice':2,'Bug':2},
                'Immune':{},'Resistant':{'Ground':1/2,'Water':1/2,'Grass':1/2,'Electric':1/2},
                'Moves':{
                'Move':
                }},
            "Kangaskhan":
                {'Hp':105,'Atk':95,'Def':80,'Sp.Atk':40,'Sp.Def':80,'Speed':90,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Move':
                }},
            "Horsea":
                {'Hp':30,'Atk':40,'Def':70,'Sp.Atk':70,'Sp.Def':25,'Speed':60,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Seadra":
                {'Hp':55,'Atk':65,'Def':95,'Sp.Atk':95,'Sp.Def':45,'Speed':85,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Goldeen":
                {'Hp':45,'Atk':67,'Def':60,'Sp.Atk':35,'Sp.Def':50,'Speed':63,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Seaking":
                {'Hp':80,'Atk':92,'Def':65,'Sp.Atk':65,'Sp.Def':80,'Speed':68,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Staryu":
                {'Hp':30,'Atk':45,'Def':55,'Sp.Atk':70,'Sp.Def':55,'Speed':85,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Starmie":
                {'Hp':60,'Atk':75,'Def':85,'Sp.Atk':100,'Sp.Def':85,'Speed':115,
                'Type':['Water','Psychic'],'Weakness':{'Grass':2,'Electric':2,'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2,'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Mr.Mime":
                {'Hp':40,'Atk':45,'Def':65,'Sp.Atk':100,'Sp.Def':120,'Speed':90,
                'Type':['Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Scyther":
                {'Hp':70,'Atk':110,'Def':80,'Sp.Atk':55,'Sp.Def':80,'Speed':105,
                'Type':['Bug','Flying'],'Weakness':{'Flying':2,'Rock':4,'Fire':2,'Electric':2,'Ice':2},
                'Immune':{'Ground':0},'Resistant':{'Fighting':1/4,'Bug':1/2,'Grass':1/4},
                'Moves':{
                'Move':
                }},
            "Jynx":
                {'Hp':65,'Atk':50,'Def':35,'Sp.Atk':115,'Sp.Def':95,'Speed':95,
                'Type':['Ice','Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2,'Steel':2,'Rock':2,'Fire':2},
                'Immune':{},'Resistant':{'Ice':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Electabuzz":
                {'Hp':65,'Atk':83,'Def':57,'Sp.Atk':95,'Sp.Def':85,'Speed':105,
                'Type':['Electric'],'Weakness':{'Ground':2},
                'Immune':{},'Resistant':{'Flying':1/2,'Steel':1/2,'Electric':1/2},
                'Moves':{
                'Move':
                }},
            "Magmar":
                {'Hp':65,'Atk':95,'Def':57,'Sp.Atk':100,'Sp.Def':85,'Speed':93,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                }},
            "Pinsir":
                {'Hp':65,'Atk':125,'Def':100,'Sp.Atk':55,'Sp.Def':70,'Speed':85,
                'Type':['Bug'],'Weakness':{'Flying':2,'Rock':2,'Fire':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Ground':1/2,'Grass':1/2},
                'Moves':{
                'Move':
                }},
            "Tauros":
                {'Hp':75,'Atk':100,'Def':95,'Sp.Atk':40,'Sp.Def':70,'Speed':110,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Move':
                }},
            "Magikarp":
                {'Hp':20,'Atk':10,'Def':55,'Sp.Atk':15,'Sp.Def':20,'Speed':80,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Gyrados":
                {'Hp':95,'Atk':125,'Def':79,'Sp.Atk':60,'Sp.Def':100,'Speed':81,
                'Type':['Water','Flying'],'Weakness':{'Rock':2,'Electric':4},
                'Immune':{},'Resistant':{'Water':1/2,'Fighting':1/2,'Bug':1/2,'Steel':1/2,'Fire':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Lapras":
                {'Hp':130,'Atk':85,'Def':80,'Sp.Atk':85,'Sp.Def':95,'Speed':60,
                'Type':['Water','Ice'],'Weakness':{'Grass':2,'Electric':2,'Fighting':2,'Rock':2},
                'Immune':{},'Resistant':{'Water':1/2,'Ice':1/4},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Ditto":
                {'Hp':48,'Atk':48,'Def':48,'Sp.Atk':48,'Sp.Def':48,'Speed':48,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Move':
                }},
            "Eevee":
                {'Hp':55,'Atk':55,'Def':50,'Sp.Atk':45,'Sp.Def':65,'Speed':55,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Move':
                }},
            "Vaporeon":
                {'Hp':130,'Atk':65,'Def':60,'Sp.Atk':110,'Sp.Def':95,'Speed':65,
                'Type':['Water'],'Weakness':{'Grass':2,'Electric':2},
                'Immune':{},'Resistant':{'Water':1/2,'Steel':1/2,'Fire':1/2,'Ice':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Jolteon":
                {'Hp':65,'Atk':65,'Def':60,'Sp.Atk':110,'Sp.Def':95,'Speed':130,
                'Type':['Electric'],'Weakness':{'Ground':2},
                'Immune':{},'Resistant':{'Flying':1/2,'Steel':1/2,'Electric':1/2},
                'Moves':{
            "Flareon":
                {'Hp':65,'Atk':130,'Def':60,'Sp.Atk':95,'Sp.Def':110,'Speed':65,
                'Type':['Fire'],'Weakness':{'Ground':2,'Rock':2,'Water':2},
                'Immune':{},'Resistant':{'Bug':1/2,'Steel':1/2,'Fire':1/2,'Grass':1/2,'Ice':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                }},
            "Porygon":
                {'Hp':65,'Atk':60,'Def':70,'Sp.Atk':85,'Sp.Def':75,'Speed':40,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Move':
                }},
            "Omanyte":
                {'Hp':35,'Atk':40,'Def':100,'Sp.Atk':90,'Sp.Def':55,'Speed':35,
                'Type':['Rock','Water'],'Weakness':{'Grass':4,'Electric':2,'Ground':2,'Fighting':2},
                'Immune':{},'Resistant':{'Poison':1/2,'Flying':1/2,'Fire':1/4,'Ice':1/2,'Normal':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Omastar":
                {'Hp':70,'Atk':60,'Def':125,'Sp.Atk':115,'Sp.Def':70,'Speed':55,
                'Type':['Rock','Water'],'Weakness':{'Grass':4,'Electric':2,'Ground':2,'Fighting':2},
                'Immune':{},'Resistant':{'Poison':1/2,'Flying':1/2,'Fire':1/4,'Ice':1/2,'Normal':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Kabuto":
                {'Hp':30,'Atk':80,'Def':90,'Sp.Atk':55,'Sp.Def':45,'Speed':55,
                'Type':['Rock','Water'],'Weakness':{'Grass':4,'Electric':2,'Ground':2,'Fighting':2},
                'Immune':{},'Resistant':{'Poison':1/2,'Flying':1/2,'Fire':1/4,'Ice':1/2,'Normal':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Kabutops":
                {'Hp':60,'Atk':115,'Def':105,'Sp.Atk':65,'Sp.Def':70,'Speed':80,
                'Type':['Rock','Water'],'Weakness':{'Grass':4,'Electric':2,'Ground':2,'Fighting':2},
                'Immune':{},'Resistant':{'Poison':1/2,'Flying':1/2,'Fire':1/4,'Ice':1/2,'Normal':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Aerodactyl":
                {'Hp':80,'Atk':105,'Def':65,'Sp.Atk':60,'Sp.Def':75,'Speed':130,
                'Type':['Rock','Flying'],'Weakness':{'Rock':2,'Steel':2,'Water':2,'Electric':2,'Ice':2},
                'Immune':{'Ground':0},'Resistant':{'Poison':1/2,'Flying':1/2,'Fire':1/2,'Bug':1/2,'Normal':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Snorlax":
                {'Hp':160,'Atk':110,'Def':65,'Sp.Atk':65,'Sp.Def':110,'Speed':30,
                'Type':['Normal'],'Weakness':{'Fighting':2},
                'Immune':{'Ghost':0},'Resistant':{},
                'Moves':{
                'Move':
                }},
            "Articuno":
                {'Hp':90,'Atk':85,'Def':100,'Sp.Atk':95,'Sp.Def':125,'Speed':85,
                'Type':['Ice','Flying'],'Weakness':{'Steel':2,'Rock':4,'Fire':2,'Electric':2},
                'Immune':{'Ground':0},'Resistant':{'Grass':1/2,'Bug':1/2},
                'Moves':{
                'Move':
                }},
            "Zapdos":
                {'Hp':90,'Atk':90,'Def':85,'Sp.Atk':125,'Sp.Def':90,'Speed':100,
                'Type':['Electric','Flying'],'Weakness':{'Ice':2,'Rock':2},
                'Immune':{'Ground':0},'Resistant':{'Grass':1/2,'Bug':1/2,'Fighting':1/2,'Flying':1/2,'Steel':1/2},
                'Moves':{
                'Move':
                }},
            "Moltres":
                {'Hp':90,'Atk':100,'Def':90,'Sp.Atk':125,'Sp.Def':85,'Speed':90,
                'Type':['Fire','Flying'],'Weakness':{'Rock':4,'Water':2,'Electric':2},
                'Immune':{'Ground':0},'Resistant':{'Bug':1/4,'Steel':1/2,'Fire':1/2,'Grass':1/4,'Fighting':1/2},
                'Moves':{
                'Scratch':{'Type':"Normal",'cat':"physical",'pwr':40,'acc':100,'pp':35},
                }},
            "Dratini":
                {'Hp':41,'Atk':64,'Def':45,'Sp.Atk':50,'Sp.Def':50,'Speed':50,
                'Type':['Dragon'],'Weakness':{'Ice':2,'Dragon':2},
                'Immune':{},'Resistant':{'Grass':1/2,'Fire':1/2,'Water':1/2,'Electric':1/2},
                'Moves':{
                'Move':
                }},
            "Dragonair":
                {'Hp':61,'Atk':84,'Def':65,'Sp.Atk':70,'Sp.Def':70,'Speed':70,
                'Type':['Dragon'],'Weakness':{'Ice':2,'Dragon':2},
                'Immune':{},'Resistant':{'Grass':1/2,'Fire':1/2,'Water':1/2,'Electric':1/2},
                'Moves':{
                'Move':
                }},
            "Dragonite":
                {'Hp':91,'Atk':134,'Def':95,'Sp.Atk':100,'Sp.Def':100,'Speed':80,
                'Type':['Dragon','Flying'],'Weakness':{'Rock':2,'Ice':4,'Dragon':2},
                'Immune':{'Ground':0},'Resistant':{'Grass':1/4,'Bug':1/2,'Fighting':1/2,'Fire':1/2,'Water':1/2},
                'Moves':{
                'Move':
                }},
            "Mewtwo":
                {'Hp':106,'Atk':110,'Def':90,'Sp.Atk':154,'Sp.Def':90,'Speed':130,
                'Type':['Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
                }},
            "Mew":
                {'Hp':100,'Atk':100,'Def':100,'Sp.Atk':100,'Sp.Def':100,'Speed':100,
                'Type':['Psychic'],'Weakness':{'Bug':2,'Ghost':2,'Dark':2},
                'Immune':{},'Resistant':{'Fighting':1/2,'Psychic':1/2},
                'Moves':{
                'Water Sport':{'Type':"Water",'cat':"status",'pwr':0,'acc':100,'pp':35},
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
#=====================================================================================================================================
def Battle(p1,p2,p1chp,p2chp): ## Phrase ต่อสู้
    print("Health : ",end='')
    print("="*int(((p1chp)/Hp(p1[0]))*20),end='')
    print("*"*int(20-(((p1chp)/Hp(p1[0]))*20)))
    for i in p1[1]:
        print(i)
    use1 = input("Choose your move!! :")
    print("=================================")
    print("Health : ",end='')
    print("="*int(((p2chp)/Hp(p2[0]))*20),end='')
    print("*"*int(20-(((p2chp)/Hp(p2[0]))*20)))
    for i in p2[1]:
        print(i)
    use2 = input("Choose your opponent move!! :")
    print("=================================")
    p1.append(use1)
    p2.append(use2)
    return [p1,p2]
#=============================================================================================================================================
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
def MainBattle(p1,p2,p1chp,p2chp): 
    p1chp = p1chp #Player 1 Current Hp
    p2chp = p2chp #Player 2 Current Hp
    p = Battle(p1,p2,p1chp,p2chp)
    move1,move2 = p[0],p[1]
    Respect = Priority(move1,move2)
    for i in Respect:
        if i in p1:
            dmg = (Damaging(i,p1,p2))
            p2chp -= (Damaging(i,p1,p2))
            print(p1[0],'has do',(dmg),'damges!!')
            print(p2[0],'got',p2chp,'Hp left!!')
            print('=================================')
            if p1chp <=0:
                print(p2[0],'Won the battle!!')
                break
            elif p2chp <=0:
                print(p1[0],'Won the battle!!')
                break
        elif i in p2:
            dmg = (Damaging(i,p1,p2))
            p1chp -= (Damaging(i,p1,p2))
            print(p2[0],'has do',(dmg),'damges!!')
            print(p1[0],'got',p1chp,'Hp left!!')
            print('=================================')
            if p1chp <=0:
                print(p2[0],'Won the battle!!')
                break
            elif p2chp<=0:
                print(p1[0],'Won the battle!!')
                break
    if p1chp >=0 and p2chp >=0:
        p1.pop(2)
        p2.pop(2)
        MainBattle(p1,p2,p1chp,p2chp) 

#======================================================================================================================
q1 = True
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
    battle_confirm = input("Press 'Battle' to start the battle!!\n :")
MainBattle(PokemonP1,PokemonP2,Hp(PokemonP1[0]),Hp(PokemonP2[0]))
    