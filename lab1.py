variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

constraints = {
        "WA" : ["NT", "SA"],
        "NT" : ["WA", "SA", "Q"],
        "SA" : ["WA", "NT", "Q", "NSW", "V"],
        "Q"  : ["NT", "SA", "NSW"],
        "NSW" : ["SA", "Q", "V"],
        "V"   : ["SA", "NSW"],
        "T" : []

        }


domains = {}




