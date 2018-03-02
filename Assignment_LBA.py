import json

with open('data/tokyo-metro-data.json') as json_data:
    d = json.load(json_data)

def greedy_find_path(origin, destination):
    position = origin
    path = []
    while True:
        path.append(str(position))
        min_time_connection = d[position]["connections"][0]

        for connection in d[position]["connections"]:
            if connection["target_id"] == destination:
                path.append(str(connection["target_id"]))
                return path
            if connection["duration"] < min_time_connection["duration"]:
                min_time_connection = connection["target_id"]

        position = min_time_connection["target_id"]

print greedy_find_path("I18", "I15")




import json

with open('data/tokyo-metro-data.json') as json_data:
    d = json.load(json_data)

def greedy_find_path(origin, destination):
    position = origin
    path = []
    while True:
        print position
        path.append(str(position))
        min_time_connection = None

        for connection in d[position]["connections"]:
            if connection["target_id"] == destination:
                path.append(str(connection["target_id"]))
                return path
            if connection["target_id"] not in path:
                if min_time_connection != None:
                    if connection["duration"] < min_time_connection["duration"]:
                        min_time_connection = connection["target_id"]
                else:
                    min_time_connection = connection["target_id"]

        position = min_time_connection["target_id"]

print greedy_find_path("I18", "I15")
