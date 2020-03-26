print("@author: EETRAA")
print("@version: beta x.x")
print("converter args:Vout,Vinmax,Vinmin,Duty,Io,Il,r,SwitchingFrequency,Von,Voff,L")
'''
method strategies:max,min,current(temp),value_with_condition,run_all(calc all accessable results)

ieads:
    calc_max_duty,calc_duty_max
    calc values with no declaration
    self.Il-->
    Vin,Io-->variables,refer to "TI smps stage" app.
    variables classes-->calculated,assigned
'''
class buck:
    
    Vout,Vinmax,Vinmin,Duty,Io,Il,r,SwitchingFrequency,Von,Voff,L= 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
    
    def __init__(self,Vout,Vinmax,Vinmin,Duty,Io,Il,r,SwitchingFrequency,L):
        
        self.Vout = Vout
        self.Vinmax = Vinmax
        self.Vinmin = Vinmin
        self.Duty = Duty                #wondering if this value ought to be saved?
        self.Io = Io
        self.Il = Il
        self.r = r                      #wondering if this value ought to be saved?
        self.SwitchingFrequency = SwitchingFrequency
        self.L = L
    def calc_min_duty(self):
        self.Dutymin = self.Vout/self.Vinmax
        return self.Dutymin
    def calc_max_duty(self):
        self.Dutymax = self.Vout/self.Vinmin
        return self.Dutymax
    def calc_current_duty(self,VinCurrent):
        self.Dutycurrent = self.Vout/VinCurrent
    def calc_max_r(self):
        self.rmax = (self.Vinmax*(self.calc_min_duty()/self.SwitchingFrequency))/(self.L*self.Il)
    def calc_min_r(self):
        self.rmin = (self.Vinmin*(self.calc_max_duty()/self.SwitchingFrequency))/(self.L*self.Il)
    def calc_current_r(self,VinCurrent):
        self.rcurrent = (VinCurrent*(self.Duty/self.SwitchingFrequency))/(self.L*self.Il)
    def calc_il(self):
        self.Il = self.Io

class boost:
    
    Vout,Vinmax,Vinmin,Duty,Io,Il,r,SwitchingFrequency,Von,Voff,L= 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
    
    def __init__(self,Vout,Vinmax,Vinmin,Duty,Io,Il,r,SwitchingFrequency):
        
        self.Vout = Vout
        self.Vinmax = Vinmax
        self.Vinmin = Vinmin
        self.Duty = Duty
        self.Io = Io
        self.Il = Il
        self.r = r
        self.SwitchingFrequency = SwitchingFrequency
        
    def calc_min_duty(self):
        self.Duty = (self.Vout - self.Vinmax)/self.Vout
    def calc_max_duty(self):
        self.Duty = (self.Vout - self.Vinmin)/self.Vout
    def calc_current_duty(self,VinCurrent):
        self.Duty = (self.Vout - VinCurrent)/self.Vout
    def calc_il(self):
        self.Il = self.Io/(1 - self.Duty)

class buck_boost:
    
    Vout,Vinmax,Vinmin,Duty,Io,Il,r,SwitchingFrequency,Von,Voff,L= 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
    
    def __init__(self,Vout,Vinmax,Vinmin,Duty,Io,Il,r,SwitchingFrequency):
        
        self.Vout = Vout
        self.Vinmax = Vinmax
        self.Vinmin = Vinmin
        self.Duty = Duty
        self.Io = Io
        self.Il = Il
        self.r = r
        self.SwitchingFrequency = SwitchingFrequency
        
    def calc_min_duty(self):
        self.Duty = self.Vout/(self.Vinmax+self.Vout)
    def calc_max_duty(self):
        self.Duty = self.Vout/(self.Vinmin+self.Vout)
    def calc_current_duty(self,VinCurrent):
        self.Duty = self.Vout/(VinCurrent+self.Vout)
    def calc_il(self):
        self.Il = self.Io/(1 - self.Duty)
