def show_manty_ingredients(total_kg):
    meat = 0.5*total_kg
    flour = 0.2*total_kg
    carrot = 0.05*total_kg
    pumpkin = 0.1*total_kg
    onion = 0.1*total_kg
    potato = 0.1*total_kg
    template = """ Для %s кг порций мант вам потребуется:
   - мясо %.2f кг,
   - мука %.2f кг,
   - морковь %.2f кг,
   - тыква %.2f кг
   - лук %.2f кг,
   - картофель %.2f кг,
    """
    message = template % ( total_kg, meat, flour, carrot, pumpkin, onion, potato)
    print(message)
    return int(total_kg * 2)  # Количества порции



user_in = input("Сколько килограммов мантов вам нужно")
user_kg= float(user_in)
show_manty_ingredients(user_kg)
portions = show_manty_ingredients(user_kg)
print("Всего порций", portions)