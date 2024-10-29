# TODO  Напишите функцию count_letters
def count_letters(text: str) -> dict:

    letter_count_dict = {}
    default_count = 0

    lower_text = text.lower()
    for symbol in lower_text:
        if symbol.isalpha():
            letter_count_dict[symbol] = letter_count_dict.get(symbol, default_count) + 1

    return letter_count_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_dict: dict) -> dict:

    all_letters_sum = sum(letter_dict.values())
    letter_frequency_dict = {}

    for symbol in letter_dict:
        letter_frequency_dict[symbol] = letter_dict.get(symbol) / all_letters_sum

    return letter_frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letter_count_dict = count_letters(main_str)
letter_frequency_dict = calculate_frequency(letter_count_dict)

for symbol, frequency in letter_frequency_dict.items():
    print(f"{symbol}: {frequency:.2f}")
