import cx_Oracle
# import db_config

dns_tns = cx_Oracle.makedsn(host='192.168.1.8', port='1521', sid='ORCL' )
# dns_tns = cx_Oracle.makedsn(DBConfig['Host'],DBConfig['ServiceName'],DBConfig['Port'])
# conn = cx_Oracle.connect(user=DBConfig['UserName'],password=DBConfig['Paassword'],dsn=dns_tns)
con = cx_Oracle.connect(user='scott', password='scott', dsn=dns_tns)


cur = con.cursor()
cur.execute("select * from dept order by deptno")
res = cur.fetchall()
for row in res:
    print(row)
