
import csv

class Items:
     
    # if we are define outside of init is call call atribute     
    pay_rate=0.8
    
    all=[]
                        
    # we are defined in init is call intance attribute
    
    def __init__(self,name: str,price: float,quantity=0):  ## accept value perticular same datatype
        
        ## Run validations to the recevied arguments 
       
        assert price>=0,f'Price {price} is not greater than or equal'
        assert quantity>=0,f'Price {quantity} is not greater than or equal'
        
        ## Assigning self object

        self.__name=name
        self.price=price
        self.quantity=quantity
        
        # actine to execute 
        
        Items.all.append(self)
    
    @property
    # property decorator = read only attribute
    def name(self):
        return self.__name
      
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_dicount(self):
        self.price=self.price * self.pay_rate
        
        
    @staticmethod
    def is_integer(num):  # is method works like regular our function
        
        # we will count the floats that are point zero
        # For i.e. 5.0 , 10.0 
        
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        
        else:
            False
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
            
        for item in items:
            Items(
                  name=item.get('name'),
                  price=float(item.get('price')),
                  quantity=float(item.get('quantity'))
                )

    def __repr__(self):       
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

    #@property decorator is allow to read only 
    #  decorator is pre- execute after method will execute 
    
    # @property
    # def read_only_name(self):
    #     return "AAA"
   
