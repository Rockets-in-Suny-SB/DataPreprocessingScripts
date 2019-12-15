import mysql.connector
import json

demographic = {"White": 0,
               "Black or African American": 1,
               "Asian": 2,
               "Native Hawaiian and Other Pacific Islander": 3,
               "Two or more races": 4,
               "American Indian and Alaska Native": 5,
               "Some Other Race": 6
               }

state_id = {'Illinois': 0, "Ohio": 1, "Oregon": 2}
state_ids = {'Illinois': 17, "Ohio": 39, "Oregon": 41}
party_id = {'democratic': 0, 'republican': 1, 'others': 2}
mydb = mysql.connector.connect(
    host="mysql4.cs.stonybrook.edu",
    user="rockets",
    passwd="changeit",
    database="rockets"
)
mycursor = mydb.cursor()

inp = open('../processedData/districts_data.json', 'r')
loaded_json = json.load(inp)

state = 'Oregon'
for district in loaded_json[state]:
    district_id = state_ids[state] * 1000 + int(district)
    district_name = "Congressional District " + str(district)
    district = loaded_json[state][district]
    population = int(district['demographic']['Total'])
    sql = "INSERT INTO district (district_id, geo_json, name, population) VALUES (%s, %s, %s, %s)"
    val = (district_id, '', district_name, population)
    mycursor.execute(sql, val)
    for group in district['demographic']:
        if group != "Total":
            sql = "INSERT INTO district_minority_group_population (district_id, minority_group_population, minority_group_population_key) VALUES (%s, %s, %s)"
            val = (district_id, district['demographic'][group], demographic[group])
            mycursor.execute(sql, val)
    for party in district['vote2018']:
        sql = "INSERT INTO district_party_votes (district_id, party_votes, party_votes_key) VALUES (%s, %s, %s)"
        val = (district_id, district['vote2018'][party]['Votes'], party_id[party])
        mycursor.execute(sql, val)
    sql = "INSERT INTO state_districts (state_name, state_status, districts_district_id,districts_key) VALUES (%s, %s, %s,%s)"
    val = (state_id[state], 0, district_id,district_id)
    mycursor.execute(sql, val)
    val = (state_id[state], 1, district_id,district_id)
    mycursor.execute(sql, val)

mydb.commit()
