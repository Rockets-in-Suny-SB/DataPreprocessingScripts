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
mydb = mysql.connector.connect(
    host="mysql4.cs.stonybrook.edu",
    user="rockets",
    passwd="changeit",
    database="rockets"
)

mycursor = mydb.cursor()
state = {'Illinois': 0, 'Ohio': 1, 'Oregon': 2}

with open('../processed_data/Illinois_precincts_demographic.json', 'r') as inp:
    state_id = state['Illinois']
    loaded_json = json.load(inp)
    state_demo_dic = {} #Storing population for each group in a state
    for precinct in loaded_json['precincts']:
        precinct = loaded_json['precincts'][precinct]
        for group in precinct['demographic']:
            state_demo_dic.setdefault(group,0)
            state_demo_dic[group]+= int(precinct['demographic'][group]) #Calculate state total population and for each group
    sql = "INSERT INTO state (name, status, population) VALUES (%s, %s, %s)"
    val = (state_id, 0, state_demo_dic["Total"])
    mycursor.execute(sql, val)
    val = (state_id, 1, state_demo_dic["Total"])
    mycursor.execute(sql, val)
    for group in state_demo_dic:
        if group != 'Total':
            sql = "INSERT INTO state_demographic_group (state_name, state_status, population,demographic_group) VALUES (%s, %s, %s, %s)"
            val = (state_id, 0, state_demo_dic[group],demographic[group])
            mycursor.execute(sql, val)
            val = (state_id, 1, state_demo_dic[group],demographic[group])
            mycursor.execute(sql, val)
    for precinct in loaded_json['precincts']:
        precinct = loaded_json['precincts'][precinct]
        precinct_id = int(precinct['info']['id'])
        sql = "INSERT INTO state_precincts (state_name, state_status, precincts_precinct_id) VALUES (%s, %s, %s)"
        val = (state_id, 0, precinct_id)
        mycursor.execute(sql, val)
        val = (state_id, 1, precinct_id)
        mycursor.execute(sql, val)
    print("commit")
mydb.commit()