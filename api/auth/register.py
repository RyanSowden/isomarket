import flask
from flask import jsonify, request
from passlib.hash import bcrypt
from db import connection
import psycopg2

c = connection.cursor()

class login:

    def __init__(self):
        self.username = username
        self.password = password
        self.confirmPassword =  confirmPassword
        self.hashed = hashed

    def newUser():
        #getting username and password
        username = request.form['username']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        #checking if passwords match
        if confirmPassword == password:
           hashed =  bcrypt.hash(confirmPassword) #If passwords match, hashpassword
           #commiting all to the database & returning successful string
           c.execute("INSERT INTO users (username,password) VALUES(%s, %s)",(username,hashed))
           connection.commit()
           c.close()

        return('User successfully created') 


        





        


#password1 = input('Please enter password: ')
#password2 = bcrypt.hash(password1)

#password3 = input('Please confirm password: ')
#result = password3

#print(bcrypt.verify(password3, password2))

