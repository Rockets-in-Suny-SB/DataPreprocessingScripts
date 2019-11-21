import mysql.connector
import json

mydb = mysql.connector.connect(
  host="mysql4.cs.stonybrook.edu",
  user="rockets",
  passwd="changeit",
  database="rockets"
)

mycursor = mydb.cursor()

#party id in the ENUM
PARTYID = {'democrat':0,'republican':1,'others':2}

def insertDistrict(file):
    with open(file, 'r') as inp:
        loaded_json = json.load(inp)
        for dist in loaded_json['features']:
            #Parse District ID
            property = dist['properties']
            name = str(property['NAMELSAD'])
            id = int(name.split(' ')[2])
            population = int(property['demographic']['Total'])
            sql = "INSERT INTO district (district_id, geo_json, name, population) VALUES (%s, %s, %s, %s)"
            val = (id,'',name,population)
            mycursor.execute(sql, val)
        return

def insertDistrictVotes(file):
    with open(file, 'r') as inp:
        loaded_json = json.load(inp)
        for dist in loaded_json['features']:
            # Parse District ID
            property = dist['properties']
            name = str(property['NAMELSAD'])
            id = int(name.split(' ')[2])
            for party in property['votes'].keys():
                if str(party) in ['democrat','republican','others']:
                    sql = "INSERT INTO district_party_votes (district_id, party_votes, party_votes_key) VALUES (%s, %s, %s)"
                    val = (id, property['votes'][party],PARTYID[str(party)])
                    mycursor.execute(sql, val)
        return

CONGRESSIONALGEOJSON = '../processed_data/Oregon_congressional_geo_processed.json'
insertDistrict(CONGRESSIONALGEOJSON)
insertDistrictVotes(CONGRESSIONALGEOJSON)
mydb.commit()