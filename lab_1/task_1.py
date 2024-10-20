numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missed_element_index = 4
elements_number = len(numbers)
element_sum = sum(numbers[:missed_element_index] + numbers[missed_element_index + 1:])
numbers[missed_element_index] = element_sum / elements_number
print("Измененный список:", numbers)
