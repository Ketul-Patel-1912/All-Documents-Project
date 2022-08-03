
from Items import Items

class phone(Items):
    
    def __init__(self,name: str,price: float,quantity=0,broken_phone=0):
        
        ## call to super function to have access to all arguments and methods
        
        super().__init__(name,price,quantity)
        
        self.broken_phone=broken_phone
            
