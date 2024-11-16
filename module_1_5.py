immutable_var=1,2,False,"Car",5.5
print(immutable_var)
#immutable_var[0]=25
#print(immutable_var)
#пишет: Traceback (most recent call last):
#  File "C:\Users\Дмитрий\Desktop\URBAN\PROJECTS\Lesson0\module_1_5.py", line 3, in <module>
#   immutable_var[0]=25
#TypeError: 'tuple' object does not support item assignment
# кортеж нельзя изменить,потому что это не изменяемый тип данных по сравнению со списками
immutable_var=[1,2,False,"Car",5.5]
immutable_var[0]=True
immutable_var[1]="Truck"
immutable_var[2]=25
immutable_var[3]=2.8
immutable_var[4]=44
immutable_var.extend(["Urban",333])
print(immutable_var)
