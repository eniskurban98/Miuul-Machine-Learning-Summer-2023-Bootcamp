# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS

# Fonksiyonlar
# Koşullar
# Döngüler
# Comprehensions


####################################################
# Fonksiyon Okuryazarlığı
#####################################################
#
# print("a")
# print('a')
#
# print("a", "b")
# print("a" "b")
#
# print("a","b", sep = "__")
#
# print(help(print))   # or you can type in python console as ?print
#
#
#


#######################################
# Fonksiyon Tanımlama
#######################################


# girilen sayıları 2 ile çarpacak bir fonksiyon
# a function that multiply any given number with 2
#
# def calculate(x):
#     print(x * 2)
#
#
# calculate(5)

# According to Python PEP-8 rules in order to get better code visibility, developer should adapt some rules like
# with after any given function you should space two lines etc.


# tr. iki argümanlı/parametreli bir fonksiyon tanımlayalım
# en. let's define a function with two arguments/parameters
#
# def summer(arg1, arg2):
#     print(arg1 + arg2)
#
# summer(5,8)
#
# summer(arg2 = 8, arg1 = 51) # we can assign the arguments like this if we want to change orders


##########################3
# Docstring
###########################

#
# def summer(arg1, arg2):
#     """
#     Sum of two numbers
#
#     Args:
#         arg1: int, float
#         arg2: int, float
#
#     Returns:
#         int, float
#
#     Examples:
#
#     Notes:
#
#     """
#     print(arg1, arg2)
#


#################################################
# Fonksiyonların statement/body bölümü
################################################


# def function_name(parameters/arguments):
#     statements (function body)

#
# def say_hi(string):
#     print(string)
#     print("Hi")
#     print("Hello")
#
# say_hi("miuul")


# girilen iki sayıyı çarpıp bunu bir nesnede tutan ve sonrasında onu yazdıran bir fonksiyon yazalım.

# def multiplication(a, b):
#     c = a * b
#     print(c)
#
# multiplication(10, 9)


# girilen değerleri bir liste içinde saklayacak fonksiyon tanımlayalım

# list_store = []
#
# def add_element(a, b):
#     c = a * b
#     list_store.append(c)
#     print(list_store)
#
# add_element(1, 8)
# add_element(18, 8)
# add_element(180, 10)


##########################################
# Ön tanımlı argümanlar/parametreler (Default arguments/parameters)
###########################################

# def divide(a,b):
#     print(a / b)
#
# divide(1,2)
#
#
# def divide(a, b=1):
#     print(a / b)
#
# divide(1)
#
#
# def say_hi(string= "Merhaba"):
#     print(string)
#     print("Hi")
#     print("Hello")
#
# say_hi("mrb")
#


################################################
# Ne zaman fonksiyon yazma ihtiyacımız olur?
################################################


# warm, moisture, charge

# (56 + 15) / 80
# (17 + 45) / 70
# (52 + 45) / 80
#
# # DRY
#
# def calculate(warm, moisture, charge):
#     print((warm + moisture) / charge)
#
# calculate(98, 12, 78)


##################################################
# Return: Fonksiyon çıktılarını girdi olarak kullanmak
##################################################

# def calculate(warm, moisture, charge):
#     print((warm + moisture) / charge)
#
# # calculate(98, 12, 78)
#
# def calculate(warm, moisture, charge):
#     return((warm + moisture) / charge)
#
# calculate(98, 12, 78) * 10
#
# a = calculate(98, 12, 78) * 10
#
#
# def calculate(warm, moisture, charge):
#     warm = warm * 2
#     moisture = moisture * 2
#     charge = charge * 2
#
#     output = (warm + moisture) / charge
#
#     return warm, moisture, charge, output
#
#
# print(calculate(98, 12, 78))
# print(type(calculate(98, 12, 78)))
#
# warm, moisture, charge, output = calculate(98, 12, 78)


########################################################
# Fonksiyon içerisinden fonksiyon çağırmak
########################################################


# def calculate(warm, moisture, charge):
#     return int((warm + moisture) / charge)
#
# print(calculate(90, 12, 12) * 10)
#
#
# def standardization(a, p):
#     return a * 10 / 100 * p * p
#
# print(standardization(45, 1))
#
#
# def all_calculation(warm, moisture, charge, a, p):
#     print(calculate(warm, moisture, charge))
#     b = standardization(a, p)
#     print(b * 10)
#
# print(all_calculation(1, 3, 5, 19, 12))



#####################################################################################
# Local ve Global Değişkenler
#####################################################################################

# list_store = [1,2]
# print(type(list_store))
#
# def add_element(a, b):
#     c = a * b
#     list_store.append(c)
#     print(list_store)
#
# add_element(1, 9)


##############################################################3
# Quiz- Fonksiyonlar
###############################################################

# 1)
# Verilen kod parçasının çıktısı nedir?

# def square(a):
#     return a**2
#
# square("hello")

# ------->  Hata verir


# 2)
# Bir fonksiyon tanımlamak için "def" ifadesinden sonra aşağıdakilerden hangisi gelmelidir?

# ---------> fonksiyon ismi


# 3.
# Verilen kod parçası sonucunda oluşan hatanın giderilmesi için aşağıdakilerden hangisi yapılabilir?

# def calc(wage, hour):
#     print(wage, hour)
#
# calc(10, 40) - 200

# ---------> print yerine return kullanılmalı

# 4.
# Verilen kod parçasının çıktısı aşağıdakilerden hangisidir?

# store = []
#
# def add_variable(a,b):
#     c = a**b
#     store.append(c)
#     print(store)
#
# add_variable(4,3)

# 5.
# Fonksiyonun içinde tanımlanan değişkenlere … , fonksiyonun dışında tanımlanan değişkenlere … adı verilir.
# Yukarıdaki cümlede boş kalan yerlere aşağıdakilerden hangisi gelmelidir?


# -------> lokal değişkenler, global değişkenler