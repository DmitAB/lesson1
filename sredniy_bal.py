grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
spisok=list(students)
print(spisok)
abc=sorted(spisok)
print(abc)
Aaron=(sum(grades[0])/len(grades[0]))
print(Aaron)
Bilbo=(sum(grades[1])/len(grades[1]))
print(Bilbo)
Johnny=(sum(grades[2])/len(grades[2]))
print(Johnny)
Khendrik=(sum(grades[3])/len(grades[3]))
print(Khendrik)
Steve=(sum(grades[4])/len(grades[4]))
print(Steve)
sr_bal={abc[0]:Aaron,abc[1]:Bilbo,abc[2]:Johnny,abc[3]:Khendrik,abc[4]:Steve}
print(sr_bal)

