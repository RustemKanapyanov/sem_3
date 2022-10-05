# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

new_list = [2, 5, 8, 10]
result_list = []
for i in range((len(new_list)+1)//2):
    result_list.append(new_list[i]*new_list[len(new_list)-1-i])
print(result_list)