import random
body_pocitac = 0
body_hrac = 0
def hra():
    global body_hrac, body_pocitac
    moznosti = ['kamen','papier','noznice']
    hrac = input('kamen/papier/noznice? ' ).lower()
    if hrac not in moznosti:
        print('vyber si jednu z moznosti! ' )
        hra()
    pocitac = random.choice(moznosti)
    print('poicitac si vybral: ', pocitac )
    if pocitac == hrac:
        print('remiza ' )
        
    elif pocitac == 'kamen' and hrac == 'papier' or pocitac == 'papier' and hrac == 'noznice' or pocitac == 'noznice' and hrac == 'kamen':
        print('vyhral si')
        body_hrac += 1
    else:
        print('prehral si')
        body_pocitac += 1
    print(f'stav: pocitac {body_pocitac} ty {body_hrac}')
    pokracovat()
    
def pokracovat():
    chces = input('chces hrat znovu? (ano/nie) ' )
    if chces not in ['ano','nie']:
        return pokracovat()
    elif chces == 'ano':
        hra()
    elif chces == 'nie':
        quit()

hra()
