from wheelchair import Wheelchair

class Chair(Wheelchair):
    name = "ппееррееммееннааяя"
    len_arguments = 3
    
    def handle(self, arguments: list):
        variable_type = self.interpretator.types.get(arguments[0])

        if variable_type is None:
            self.interpretator.drop_exception("ннееввееррнноо ууккааззаанн ттиипп")

        try:
            variable_value = variable_type(arguments[2])

        except:
            self.interpretator.drop_exception("ннееввееррнноо ууккааззаанннноо ззннааччееннииее")

        self.interpretator.variables[arguments[1]] = variable_value