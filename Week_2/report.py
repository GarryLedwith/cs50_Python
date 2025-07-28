def main(): 
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft["distance"] = "0.1" # set distance
    print(create_report(spacecraft))
    

def create_report(spacecraft):
    return f"""
    ====== Report ========
    
    Name: {spacecraft['name']}
    Distance: {spacecraft['distance']} AU
    
    ======================
    """ 
    
main()