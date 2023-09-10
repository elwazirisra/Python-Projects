import sqlite3
import requests

connection = sqlite3.connect('database3.db')

url = ("https://newsdata.io/api/1/news?apikey=pub_2890955f4ae4844cf0509182c6efa0cb8ce47&q=yemen")
      

response = requests.get(url)


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


 
for n in response.json()["results"]:
    if n["language"] == 'english':

     
      cur.execute("INSERT INTO yemennews (created, title, Description, content) VALUES (?, ?, ?, ?)",
                (n["pubDate"], n["title"],n["description"], n["content"])
                )

   

connection.commit()
connection.close()