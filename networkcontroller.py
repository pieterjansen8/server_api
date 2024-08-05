import requests
import time
import json
class network_controller: 
    def create_game():
        url = "https://test-fac11-default-rtdb.europe-west1.firebasedatabase.app/"
        r = requests.get(url=url+"game_id.json")
        j = r.json()
        id = j["num"]+1
        body = {
            "game_num": id
        }
        requests.put(json=body, url=url+str(id)+".json")
        requests.put(json={"num":id}, url=url+"game_id.json")
        return id
