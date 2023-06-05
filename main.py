import requests
def trace(*args):
  """Used for debug output"""
  print (*args)  # Comment out this line to remove debug output
  pass

name = input ("""Enter the number of the character you want to you like to learn more about?
Luke Skywalker (1)
R2-D2 (3)
Darth Vader (4)
Yoda (20)
Princess Leia (5)
""")

BASE_URL = "https://swapi.dev/api"

URL = BASE_URL + "/people/"+ name 

# Get data from the web site and put it into Python collections
trace ("Calling", URL)
response = requests.get(URL) # Get data from the URL
response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

# See what the raw data looks like
#trace ("\nText returned:", response.text)
# print (data["name"])
while True :
  info = input("""what would you like to learn more about your character?
  birth year
  homeworld
  exit
  """)
  
  if info == 'birth year':
    print(data["birth_year"])
    
  if info == 'homeworld':
    HWURL = (data["homeworld"])
    trace ("Calling", HWURL)
    response = requests.get(HWURL) # Get data from the URL
    response.raise_for_status()  # Throw an exception if the request failed
    data = response.json()
    print(data["name"])
    HWinfo = input("would you like to learn more about " + 
   (data["name"])+" ")
    if HWinfo == 'yes':
      print(data["name"] + ": climate = " + data["climate"] + " terrain = " + data["terrain"] + " population = " + data["population"])
    if HWinfo == 'no':
      break

        


  if info == 'exit':
    break




  

  
  
  
  