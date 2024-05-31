#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import psycopg2

def lambda_handler(event, context):
    # TODO implement
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response_data = response.json()
    
    latitude = response_data['iss_position']['latitude']
    longitude = response_data['iss_position']['longitude']
    timestamp = response_data['timestamp']
    message = response_data['message']
    
    connection = psycopg2.connect(
        host='localhost',
        port=5432,
        user='postgres',
        password='1996',
        database='spacestation'
    )
    
    cursor = connection.cursor()
    table_creation = """create table space_station(id serial primary key, latitude float, longitude float, timestamp integer, message varchar(50))"""
    try:
        cursor.execute(table_creation)
        print("table created successfully")
    except:
        print("table already created")
    
    connection.commit()
    
    #Inserting Values
    insert_query = """insert into space_station(latitude, longitude, timestamp, message) values(%s, %s, %s, %s)"""
    data = (latitude, longitude, timestamp, message)
    
    try:
        cursor.execute(insert_query, data)
        print("data inserted successfully")
    except:
        print("data insertion failed")
    
    
    cursor.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

