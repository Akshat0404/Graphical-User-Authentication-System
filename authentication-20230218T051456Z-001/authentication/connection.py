import mysql.connector as sql
import pymysql
import io
from PIL import Image

class connection():
    mydb = sql.connect(
        host="localhost",
        user="root",
        password="tiger123",database='projectex')

def signupuser(s):
    query = connection.mydb.cursor(buffered=True)
    query.execute(f"{s}")
    connection.mydb.commit()

def log(s):
    query = connection.mydb.cursor(buffered=True)
    query.execute(f"{s}")
    return query.fetchone()


# for x in range(1,100+1):
#     with open(f"/Users/ayush/Downloads/photo/{x}.jpeg","rb") as f:
#         data = f.read()
#         query = connection.mydb.cursor(buffered=True)
#         query.execute("""insert into default_img(id, image) values(%s,%s)""",(x,data))
#         connection.mydb.commit()

def cimg():
    query = connection.mydb.cursor(buffered=True)
    query.execute(f"""select image from default_img where id=1""")
    m = query.fetchall()
    h = io.BytesIO(m[0][0])
    img1=Image.open(h)
    return img1.show()

# for i in range(1,100+1):
#     query = connection.mydb.cursor(buffered=True)
#     query.execute(f"""select image from default_img where id={i}""")
#     m = query.fetchall()
#     for x in m:
#         data = x[0]
#     a = str(i)
#     with open('/Users/ayush/Downloads/project_ex/project/static/d_images/'+a+'.jpg', 'wb') as f:
#         f.write(data)
