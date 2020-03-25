class buck:
    
    Vout,Vin,Duty= 0.0,0.0,0.0
    
    def __init__(self,vin,vout,duty):
        self.Vin = vin
        self.Vout = vout
        self.Duty = duty
        
    def calc(self):
        self.Duty = self.Vout/self.Vin

class buck_boost:
    
    Vout,Vin,Duty= 0.0,0.0,0.0
    
    def __init__(self,vin,vout,duty):
        self.Vin = vin
        self.Vout = vout
        self.Duty = duty
        
    def calc(self):
        self.Duty = self.Vout/(self.Vin+self.Vout)

class boost:
    
    Vout,Vin,Duty= 0.0,0.0,0.0
    
    def __init__(self,vin,vout,duty):
        self.Vin = vin
        self.Vout = vout
        self.Duty = duty
        
    def calc(self):
        self.Duty = (self.Vout - self.Vin)/self.Vout