class Kent():
    '''number of undefeatable kentavrs are fighting with heroes, those are ore
    by one coming to fight any kentavr, that's not fighting now.
    Heroes are differing one from another by strength (whole numbers).
    Srength is the number of minutes, this hero will wigthstand the undefeatable
    kentavr before kentavr defeats him.
    the function get_time takes the list of heroes with individual strengths
    and the number of kentavrs as the arguments. The function should return
    the time from the start of the battle to the moment the last hero
    is defeated.
    as an example - 2 kentavrs fight with heroes [2,3,2,4]
    with first two heroes two kentavrs started fighting simultaneously, after
    2 minutes first kentavr finishes with his hero and starts to fight next
    hero with strength 2. After a minute second kentavr finishes fight his
    first hero with strength 3 and starts fight with the last hero with strength
    4. So, all 4 battles will be finished after 7 minutes from start'''
    kents = list()
    def __init__(self, name):
        ''' the functoion gets the name and creates the instance of Kent
        class. Besides of that it appends self to the list of Kent class
        instances'''
        Kent.kents.append(self) #appending the new instance to instance list
        self.battles = list()
        self.name = name
    def __str__(self):
        ''' prints in a fancy form which battles this instanse has stepped in'''
        return '{} with battles having timings {} with {} total time'\
        .format(self.name, self.battles, self.bat_time())
    def fight(self, hero):
        '''records the battle to consecutive battles list'''
        print('{} starts fighting hero with strength {}'.format(self.name, hero))
        self.battles.append(hero)
    def bat_time(self):
        ''' just puts the sum function to the metod to make code readable'''
        return sum(self.battles)
    def free_kent():
        '''defines, which kent finishes his battles first'''
        free_kent = Kent.kents[0]
        min_time = Kent.kents[0].bat_time()
        for kent in Kent.kents[1:]:
            if kent.bat_time() < min_time:
                min_time = kent.bat_time()
                free_kent = kent
        print('{} with total timing of battles {} has finished with his heroes\
 first and is free now'.format(free_kent.name, free_kent.bat_time()))
        return free_kent
    def max_battles_time():
        max_time = 0
        for kent in Kent.kents:
            if kent.bat_time() > max_time:
                max_time = kent.bat_time()
        return max_time

def get_time(heroes, kents_numb):
    kents = [Kent('kent ' + str(i+1)) for i in range(0, kents_numb)]
    input('{} kentavrs are created and ready to fight. Come in, one by one'\
    .format(len(kents)))
    for hero in heroes:
        print('***')
        print('Just to remind - actual kents list with kent battles is:')
        for kent in kents: print(kent)
        print('***')
        print('Just to remind - heroes list is: ' + str(heroes))
        print('***')
        Kent.free_kent().fight(hero)
        input('hero {} with strength {} started battle. Next hero, please'\
        .format(heroes.index(hero) + 1, hero))
        print()
    print('All heroes are gone. Last battle finished after {} units of time'\
    .format(Kent.max_battles_time()))
    return Kent.max_battles_time()

get_time([1,2,3,30,5,30,5,4,3,2,34,3,2,34,5,6],4)
