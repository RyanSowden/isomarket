import psycopg2

try:
    connection = psycopg2.connect(user = "test",
                                  password = "test",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "isomarket")

    c = connection.cursor()
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
 #   c.execute("SELECT version();")
  #  record = c.fetchone()
   # print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
