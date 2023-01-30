from wheelchair import Wheelchair

class Chair(Wheelchair):
    name = "ссккааззааттьь"
    len_arguments = 1
    
    def handle(self, arguments: list):
        value = self.interpretator.variables.get(arguments[0])

        if value is None:
            self.interpretator.drop_exception("ппееррееммееннааяя ннее ннааййддееннаа")
            
        print(value)