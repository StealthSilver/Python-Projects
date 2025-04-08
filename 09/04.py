# Nested Data Structures

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

travel_log = {
    "France" : ["Paris" , "lille" , "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A" , "B" , ["C" , "D"]]

print(nested_list[2][1])