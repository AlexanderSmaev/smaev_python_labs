# TODO Найдите количество книг, которое можно разместить на дискете
disket_volume_in_Mb = 1.44 # размер в Мб
page_number = 100
string_number_per_page = 50
symbol_per_string = 25
volume_to_store_per_sybmol = 4 # в байтах

disket_volume_in_byte = 1.44 * 1024 * 1024

book_number = int(disket_volume_in_byte / (page_number * string_number_per_page * symbol_per_string * volume_to_store_per_sybmol))
print("Количество книг, помещающихся на дискету:", book_number)
