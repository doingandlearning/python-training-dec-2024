empty_dict = {}

print(empty_dict)
print(type(empty_dict))

cities = {
    "Scotland": "Edinburgh",
    "Wales": "Cardiff",
    "England": "London",
    1: "my favourite city",
    (1,2,3): "this has a tuple key,"
}
print(cities)
print(cities["Scotland"])

if "Wales" in cities:
    print("It is!")

print(cities.keys())
print(cities.values())
print(cities.items())

print(tuple(cities.keys()))
print(list((1,2,3)))
print(dict([('Ireland', "Dublin"), ("France", "Paris")]))

cities["Spain"] = "Madrid"
print(cities)
