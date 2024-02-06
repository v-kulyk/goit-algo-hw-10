from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

if __name__ == "__main__":
    # Створення моделі
    model = LpProblem("Production_Optimization", LpMaximize)

    # Оголошення змінних рішення
    x1 = LpVariable("Lemonade_units", lowBound=0, cat='Integer')
    x2 = LpVariable("Fruit_Juice_units", lowBound=0, cat='Integer')

    # Цільова функція (максимізація виробництва)
    model += x1 + x2, "Total_Products"

    # Обмеження ресурсів
    model += 2 * x1 + x2 <= 100, "Water_constraint"
    model += x1 <= 50, "Sugar_constraint"
    model += x1 <= 30, "Lemon_Juice_constraint"
    model += 2 * x2 <= 40, "Fruit_Puree_constraint"

    # Розв'язання моделі
    model.solve()

    # Виведення результатів
    print(LpStatus[model.status])
    print(f"Total cost = {value(model.objective)}")
    print(f"Lemonade = {x1.varValue}")
    print(f"Juice = {x2.varValue}")
