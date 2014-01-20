
import mysql.connector
cn=mysql.connector.connect(user="root",database="employee",password="root")
cr=cn.cursor()
cr.execute("select * from salary")
for(r,n,m,rs) in cr:
 print("{0<5}|{1:^20}|{2:<5}|{3:>10}".format(r,n,m,rs))
cr.close()
cn.close()
