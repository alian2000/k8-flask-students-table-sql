#https://www.geeksforgeeks.org/working-with-mysql-blob-in-python/?ref=lbp
#https://www.geeksforgeeks.org/how-to-read-image-from-sql-using-python/?ref=lbp
#GOLDEN SCRIPT WORKED WITH MYSQL MICROSERVICE IN MY K8 cluster, in flask namespace
#https://towardsdatascience.com/how-to-deploy-a-flask-api-in-kubernetes-and-connect-it-with-other-micro-services-af16965b67fe
import mysql.connector


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB(student_id,student_pic):
    print("Reading BLOB data from students table")

    try:
        connection = mysql.connector.connect(host='192.168.86.32',
                                        port='32251',
								        database='flaskapi', 
										user='root', 
										password='admin')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from students where student_id = %s"""

        cursor.execute(sql_fetch_blob_query, (student_id,))
        record = cursor.fetchall()
        for row in record:
            print("student_id = ", row[0], )
            print("student_name = ", row[1])
            print("student_email = ", row[2])
            image = row[3]
            print("student_password = ", row[4])
            print("Storing employee image and bio-data on disk \n")
            write_file(image, student_pic)
            

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#ENTER the STUDENT ID BELOW SO YOU CAN SELECT?RETRIVE STUDENT RECORDS
readBLOB(3,"/mnt/c/Users/salian/Downloads/usama2_photo.png")
#readBLOB(1,"Shubham","shubham@aol.com","C:\Users\salian\Downloads\eric_photo.png","password123")
#readBLOB(2, "D:\Python\Articles\my_SQL\query_output\scott_photo.png",
#         "D:\Python\Articles\my_SQL\query_output\scott_bioData.txt")
