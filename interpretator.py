import time, os


class Interpretator:
    __instance = None

    types = {
        "ссттррооккаа": str,
        "ччииссллоо": int,
    }


    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


    def __init__(self):
        print("Ккооммппооссттеерр ттоопп")
        self.handling_now = 0
        self.variables = {}
        self.wheelchairs = {}

        self.get_wheelchairs()


    def drop_exception(self, reason: str):
        print("Оошшииббккаа: " + reason + "\nНнооммеерр ссттррооккии: " + str(self.handling_now))
        exit()


    def get_wheelchairs(self):
        files = os.listdir("wheelchairs")
        for file in files:
            if not file.endswith(".py"):
                continue

            module_name = file[:-3]
            exec(f"from wheelchairs import {module_name} as module\nchair = module.Chair(self)\nself.wheelchairs[chair.name] = chair")
            

            


    def interpretate(self, code: str):
        for line in code.split("\n"):
            self.handling_now += 1

            line = line.strip()

            words = line.split(" ")
            operator = words[0].lower()
            arguments = words[1:]

            self.handle_line(operator, arguments)

            time.sleep(1)


    def handle_line(self, operator: str, arguments: list):
        chair = self.wheelchairs.get(operator)

        if chair is None:
            self.drop_exception("ооппееррааттоорр ннее ннааййддеенн")

        chair.start_operator(arguments)

        



