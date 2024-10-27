money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен, в долях

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money_in_current_month = 0
month_without_debt = 0

money_in_current_month += money_capital  # добавляем сумму из подушки безопасности
while True:
    money_in_current_month -= spend
    money_in_current_month += salary
    if money_in_current_month < 0:
        break
    month_without_debt += 1  # сначало нужно убедиться, что money_in_current_month >= 0, потом прибавлять
                             # один месяц без долгов
    spend *= (1 + increase)  # т.к. рост цен на spend начинается после первого месяца, то это строка
                             # должна быть после того, как отняли траты spend

print("Количество месяцев, которое можно протянуть без долгов:", month_without_debt)
