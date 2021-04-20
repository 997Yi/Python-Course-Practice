import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute("update employee set salary=salary-5000 where kpi = 'D';")

a = cursor.execute("select * from employee order by salary desc;")
for i in a:
    print(",".join(str(j) for j in i))

connection.close();
