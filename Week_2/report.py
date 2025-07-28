def main(): 
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": "0.1"})  # set distance using update method
    # spacecraft["distance"] = "0.1"  # set distance using direct assignment
    print(create_report(spacecraft))
    

def create_report(spacecraft):
    return f"""
    ====== Report ========
    
    Name: {spacecraft['name']}
    Distance: {spacecraft.get("distance", "Unknown")} AU 
    
    ======================
    """ 
    
main()