immutable_var = "hello", 1, 1.4, True
print(immutable_var)
#immutable_var[0] = "bye"
#print(immutable_var)
# Вывод невозможен из за невозможности изменения кортежа
mutable_list = ["hello", 1, 1.4, True]
print(mutable_list)
mutable_list [0] = "bye"
mutable_list [1] = 2.2
mutable_list [2] = 4
mutable_list [3] = False
print(mutable_list)
