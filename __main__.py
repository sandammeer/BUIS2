import glob
import importlib
# add imports here
reader = importlib.import_module("read_csv")
distancecalc = importlib.import_module("distance_calc")
speedcalc = importlib.import_module("speed_calc")
quality = importlib.import_module("streetQuality")
writer = importlib.import_module("write_index")
relevant = importlib.import_module("relevant_streets")


counter = 0
uni_routes = []
#print(datetime.now())
for item in glob.glob("Ecosense\*.csv"):
    print(item)
    if relevant.uni_street_in_route(item):
        uni_routes.append(item)