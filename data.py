

import mysql.connector
cn=mysql.connector.connect(user="root",database="student",password="root")
cr=cn.cursor()
cr.execute("Insert into mark(regno,name,mark,result)values({0},'{1}',{2},'{3})".format(3,'xxx',90,'pass'))
cn.commit()
 print("Record inserted")
cr.close()
cn.close()
