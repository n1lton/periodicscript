from interpretator import Interpretator


class Wheelchair:
    name = None
    len_arguments = None


    def __init__(self, interpretator: Interpretator):
        self.interpretator: Interpretator = interpretator


    def handle(self, arguments):
        pass


    def start_operator(self, arguments):
        if len(arguments) != self.len_arguments:
            self.interpretator.drop_exception("ууккааззаанныы ннее ввссее ааррггууммееннттыы")

        self.handle(arguments)

