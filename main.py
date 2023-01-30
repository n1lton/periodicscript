from interpretator import Interpretator

def main():
    interpretator = Interpretator()

    file_name = input("Имя файла: ").strip(" ")
    if not file_name.endswith(".pidaras"):
        print("Файл не является скриптом PeriodicScript")
        return

    with open(file_name, "r", encoding="utf-8") as f:
        interpretator.interpretate(f.read())
        print("Ссккрриипптт ззааввеерршшеенн")

if __name__ == "__main__":
    main()
    
