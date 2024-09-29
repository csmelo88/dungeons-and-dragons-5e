
def set_by_list(ability, standard_ability_list):

    condition = 0
    while condition == 0:
        print(standard_ability_list)
        number = input(f"Escolha, dos valores acima, o número para {ability}:")
        if number.isdigit():
            chosen_number = int(number)
            if chosen_number in standard_ability_list:
                standard_ability_list.remove(chosen_number)
                return chosen_number
            else:
                print("O número selecionado não está disponível, tente outro!")


def set_initial_ability_by_standard_score():

    standard_ability_list = [15, 14, 13, 12, 10, 8]

    while len(standard_ability_list) != 0:
        strength = set_by_list("FORÇA", standard_ability_list)
        dexterity = set_by_list("DESTREZA", standard_ability_list)
        constitution = set_by_list("CONSTITUIÇÃO", standard_ability_list)
        intelligence = set_by_list("INTELIGÊNCIA", standard_ability_list)
        wisdom = set_by_list("CONHECIMENTO", standard_ability_list)
        charisma = set_by_list("CARISMA", standard_ability_list)

    return strength, dexterity, constitution, intelligence, wisdom, charisma

def set_manually(ability):

    condition = 1
    while condition == 1:
        chosen_number = input(f"Digite um valor para a habilidade {ability}:")
        if chosen_number.isdigit():
            number = int(chosen_number)
            print(f"Tem certeza que deseja manter o valor {number} para a habilidade {ability}?")
            condition_value = input("0 - SIM\n"
                                    "Qualquer outra tecla - NÃO")
            if condition_value.isdigit():
                condition = int(condition_value)
                if condition == 0:
                    return number
            condition = 1
        else:
            print("Entrada inválida. Digite um valor numérico.")

def set_initial_ability_manually():

    strength = set_manually("FORÇA")
    dexterity = set_manually("DESTREZA")
    constitution = set_manually("CONSTITUIÇÃO")
    intelligence = set_manually("INTELIGÊNCIA")
    wisdom = set_manually("CONHECIMENTO")
    charisma = set_manually("CARISMA")

    return strength, dexterity, constitution, intelligence, wisdom, charisma


def set_initial_ability():

    condition = 0
    while condition == 0:
        print("ESCOLHA UM MÉTODO DE PREENCHIMENTO DE HABILIDADE:")
        chosen_number = input("1: Preenchimento a partir de conjunto de scores padrão\n"
              "2: Preenchimento manual")
        if chosen_number.isdigit():
            condition = int(chosen_number)
            if condition == 1:
                return set_initial_ability_by_standard_score()
            elif condition == 2:
                return set_initial_ability_manually()
            else:
                print("Insira uma entrada válida.")
        condition = 0
