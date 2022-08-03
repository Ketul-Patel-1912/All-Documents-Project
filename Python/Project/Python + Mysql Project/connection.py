def create_server_connection(host_name,user_name,user_pass):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_pass)
        print("mySQl Database Connection Sucessful")
        
    except Error as err:
        print(f"Error: '{err}'")
        
    return connection   

pw = "root"
connection = create_server_connection("localhost","root",pw)


# mydb=mysql.connector.connect(host="127.0.0.1",
#                                     port="3307",
#                                     user="root",
#                                     password="root")