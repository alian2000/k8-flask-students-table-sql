#https://www.geeksforgeeks.org/working-with-mysql-blob-in-python/?ref=lbp
#https://www.geeksforgeeks.org/how-to-read-image-from-sql-using-python/?ref=lbp
#GOLDEN SCRIPT WORKED WITH MYSQL MICROSERVICE IN MY K8 cluster, in flask namespace
#https://towardsdatascience.com/how-to-deploy-a-flask-api-in-kubernetes-and-connect-it-with-other-micro-services-af16965b67fe

import mysql.connector


# Convert images or files data to binary format
def convert_data (file_name):
	with open(file_name, 'rb') as file:
		binary_data = file.read()
	return binary_data

try:
	connection = mysql.connector.connect(host='192.168.86.32',
                                        port='32251',
								        database='flaskapi', 
										user='root', 
										password='admin')
	print("done with conn")
	cursor = connection.cursor()
	# create table query
	create_table = """CREATE TABLE students(student_id INT PRIMARY KEY,\
	student_name VARCHAR (255) NOT NULL, student_email VARCHAR(255), student_pic BLOB NOT NULL, \
	student_password VARCHAR (255) NOT NULL) """

	# Execute the create_table query first
	#cursor.execute(create_table)
	# printing successful message
	print("Table created Successfully")

	query = """ INSERT INTO students(student_id, student_name, student_email, student_pic,student_password)\
	VALUES (%s,%s,%s,%s,%s)"""

	# First Data Insertion
	student_id = "3"
	student_name = "Nour"
	student_email= "nour@aol.com"
	student_pic = convert_data("usama.png")
	student_password= "xyzd123"
	

	# Inserting the data in database in tuple format
	result = cursor.execute(
		query, (student_id, student_name, student_email, student_pic, student_password))
	# Committing the data
	connection.commit()
	print("Successfully Inserted Values")

# Print error if occurred
except mysql.connector.Error as error:
	print(format(error))

finally:

	# Closing all resources
	if connection.is_connected():
	
		cursor.close()
		connection.close()
		print("MySQL connection is closed")
