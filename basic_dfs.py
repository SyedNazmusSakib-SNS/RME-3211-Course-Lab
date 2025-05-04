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
def map_color(graph, colors, regions, coloring = None):

    if coloring is None:
        coloring = {}
    
    print(f"Colored: ", coloring.items())

    if len(regions) == 0:
        return coloring

    
    current_region = regions[0]
    remaining_region = regions[1:]

    print("Currently I am in : ",current_region)
    print("Remaining to Explore: ",remaining_region)

    for color in colors:
        coloring[current_region] = color

        
        valid = True

        for neighbor in graph[current_region]:
            
            if neighbor in coloring and coloring[neighbor] == color:
                valid = False
                break

        if valid:
            result = map_color(graph, colors, remaining_region, coloring.copy())

            if result is not None:
                return result

    return None

map_colored = map_color(contraint_graph, domain, var)

for k, v in map_colored.items():
    print(f"{k} : {v}")

