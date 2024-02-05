import json
import requests

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
vitsi = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(vitsi).json()
print("\n" , vastaus["value"])


"""   

print(json.dumps(vastaus, indent=2))
{   
  "categories": [],
  "created_at": "2020-01-05 13:42:24.142371",
  "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
  "id": "GCZEXNKjQVaCGWxgWbuq9A",
  "updated_at": "2020-01-05 13:42:24.142371",
  "url": "https://api.chucknorris.io/jokes/GCZEXNKjQVaCGWxgWbuq9A",
  "value": "Chuck Norris can charge a cars battery by connecting the cables to his nipples"
}

"""