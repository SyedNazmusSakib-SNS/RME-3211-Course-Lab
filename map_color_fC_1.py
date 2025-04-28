var = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

domain = ["Red", "Green", "Blue"]

contraint_graph = {
        "WA" :["NT", "SA"],
        "NT" : ["WA", "SA", "Q"],
        "SA" : ["WA", "NT", "Q", "NSW", "V"],
        "Q" : ["NT", "NSW", "SA"],
        "NSW" : ["SA", "Q"],
        "V" : ["SA", "NSW"],
        "T" : []
        }

print(contraint_graph.items())
   
