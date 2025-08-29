distances = {
    "Voyager 1": "163.7",
    "Voyager 2": "134.7",
    "Pioneer 10": "82.5",
    "Pioneer 11": "70.6",
    "New Horizons": "6.5"
}


def main():
    for name in distances.keys():  # use the keys() method to iterate over the dictionary
        # print(f"{name}: {distances[name]} AU from Earth")
        print(f"{name}: {convert_au_to_meters(float(distances[name]))} meters from Earth")
        
    for distance in distances.values():
        print(f"{distance} AU is {convert_au_to_meters(float(distance))} meters")

# convert au to meters
def convert_au_to_meters(au):
    return au * 149597870700  # 1 AU in meters

      
main()
    