import mesa

#resource classes
#agents
#=========================================
# sugar ageent
#=========================================
class sugar(mesa.Agent):
    '''
    shugar:
    - Sugar agent with an amount of sugar.
    - grows one amount of sugar each turn
    '''
    
    def __init__(self):
        print("i am sugar")
#=========================================
#spice agend
#=========================================
class spice(mesa.Agent):
    '''
    spice:
    - Spice agent with an amount of spice.
    - grows one amount of spice each turn
    '''
    def __init__(self):
        print("i am spice")
#=========================================
# trader class
# most complex
#=========================================

class trader(mesa.Agent):
    '''
    trader:
    - has a metabolism for sugar and spice
    - harvests and trades sugar and spice to survive and thrive
    '''
    def __init__(self):
        print("i am trader")
#=========================================
#  model class
#=========================================
class sugarscapeG1mt(mesa.Agent):
    '''
    sugarscapeGlmt:
    - a model class to manage sugarscape with traders (G1mt)
    - from groing artificial societies by axtel and epstein
    '''
    def __init__(self):
        self.spice = spice()
        self.sugar = sugar()
        self.trader = trader()
        
        
model = sugarscapeG1mt()