def choosing_name():
    condition = 1
    while condition == 1:
        name = input("Entre com um nome para o seu personagem: ")
        print(f"Tem certeza que deseja manter o nome {name} para o seu personagem?")
        condition_value = input("0 - SIM\n"
                              "Qualquer outra tecla - NÃO")

        if condition_value.isdigit():
            condition = int(condition_value)
            if condition == 0:
                return name
        condition = 1

def choosing_class():
    class_name = 0
    while (class_name < 1) or (class_name > 3):

        print("Escolha uma das classes abaixo: ")
        print("1: Anão\n"
              "2: Elfo\n"
              "3: Humano")
        class_name_value = input()

        if class_name_value.isdigit():
            class_name = int(class_name_value)
            if class_name == 1:
                return "dwarf"
            elif class_name == 2:
                return "elf"
            elif class_name == 3:
                return "human"
        class_name = 0


def choosing_race():
    race_name = 0
    while (race_name < 1) or (race_name > 3):

        print("Escolha uma das raças abaixo: ")
        print("1: A\n"
              "2: \n"
              "3: ")
        race_number = input()

        if race_number.isdigit():
            race_name = int(race_number)
            if race_name == 1:
                return ""
            elif race_name == 2:
                return ""
            elif race_name == 3:
                return ""
        class_name = 0