import mysql.connector
import json
import csv

mydb = mysql.connector.connect(
    host="mysql4.cs.stonybrook.edu",
    user="rockets",
    passwd="changeit",
    database="rockets"
)

mycursor = mydb.cursor()

#ENUM id
dic = {"White": 0,
       "Black or African American": 1,
       "Asian": 2,
       "Native Hawaiian and Other Pacific Islander": 3,
       "Two or more races": 4,
       "American Indian and Alaska Native": 5,
       "Some Other Race": 6
       }
party_id = {'democratic': 0, 'republican': 1, 'others': 2}
election = {'2016 Congressional': 0, "2016 Presidential": 1, "2018 Congressional": 2}

#COUNTY
inp = open('processed_data/county_table.csv', 'r')
reader = csv.reader(inp)
row = next(reader, None)
for row in reader:
    id = row[2]
    name = row[1]
    sql = "INSERT INTO county (id, name) VALUES (%s, %s)"
    val = (row[2], row[1])
    mycursor.execute(sql, val)

#MAP
with open('../processed_data/Illinois_geo.json','r') as inp:
    geojson = json.load(inp)

#PRECINCT
with open('processed_data/IL_precicnts_demographic.json', 'r') as inp:

    loaded_json = json.load(inp)
    precincts = loaded_json['precincts']
    for precinct in precincts:
        precinct_id = int(precinct['info']['id'])
        name = str(precinct['name'])
        population = int(precinct['demographic']['Total'])
        county = int(precinct['info']['countyid'])
        for geo_precinct in geojson['features']:
            if name == geo_precinct['properties']['NAME']:
                geo = geo_precinct['coordinates']
        sql = "INSERT INTO precinct (precinct_id, geo_json,name, population, county_id_id) VALUES (%s, %s, %s,%s,%s)"
        val = (precinct_id, geo, name, population,county)
        mycursor.execute(sql, val)

        demographic = precincts[precinct]['demographic']
        for g in dic.keys():
            group_id = dic[g]
            population = demographic[g]
            sql = "INSERT INTO minority_name_group_population (precinct_id, group_population, minority_name) VALUES (%s, %s, %s)"
            val = (precinct_id, population, group_id)
            mycursor.execute(sql, val)

        election_id = election['2016 Congressional']
        total_votes = int(precincts[precinct]['vote2016']['republican']) + int(
            precincts[precinct]['vote2016']['democratic']) + int(precincts[precinct]['vote2016']['others'])
        winning_party_name = party_id[precincts[precinct]['vote2016']['winner']]
        winning_votes = int(precincts[precinct]['vote2016'][precincts[precinct]['vote2016']['winner']])
        sql = "INSERT INTO vote (election, id, total_votes, winning_party_name, winning_votes) VALUES (%s, %s, %s, %s,%s)"
        val = (election_id, precinct_id, total_votes, winning_party_name, winning_votes)
        mycursor.execute(sql, val)

        for p in party_id.keys():
            party_name = party_id[p]
            party_votes = precincts[precinct]['vote2016'][p]
            sql = "INSERT INTO vote_party_votes (vote_id, election, party_votes, party_name) VALUES (%s, %s, %s,%s)"
            val = (precinct_id, election_id, party_votes, party_name)
            mycursor.execute(sql, val)

        sql = "INSERT INTO precinct_votes (precinct_id, votes_election, votes_id, election) VALUES (%s, %s, %s, %s)"
        val = (precinct_id, election_id, precinct_id, election_id)
        mycursor.execute(sql, val)

        print(precinct_id)
    print('COMMIT')

mydb.commit()