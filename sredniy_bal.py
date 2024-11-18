grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
spisok=list(students)
print(spisok)
abc=sorted(spisok)
print(abc)
a=(sum(grades[0])/len(grades[0]))
print(a)
b=(sum(grades[1])/len(grades[1]))
print(b)
c=(sum(grades[2])/len(grades[2]))
print(c)
d=(sum(grades[3])/len(grades[3]))
print(d)
e=(sum(grades[4])/len(grades[4]))
print(e)
sr_bal={abc[0]:a,abc[1]:b,abc[2]:c,abc[3]:d,abc[4]:e}
print(sr_bal)

