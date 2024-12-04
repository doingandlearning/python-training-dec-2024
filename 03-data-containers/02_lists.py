empty_list = []

print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo"]
print(beatles[0])  # sublisting/indexing
print(beatles[0:2])
print(beatles[1:])
print(beatles)

beatles.append("Douglas")
print(beatles)

beatles.extend(["Andrew", "Ewan", "Ella"])
print(beatles)

beatles.remove("Douglas")
print(beatles)

beatles.insert(2, "Josh")
print(beatles)

new_beatles = beatles.copy()
new_beatles.remove("John")

print(new_beatles)
print(beatles)

if "Douglas" in beatles:
    print("Great!")
else:
    print("😢")

for member in beatles:
    print(f"{member} is in the beatles")


bands = [beatles, ["Jenny", "Andrew", "Alex"], True, (1,2,3),([1,2,3], 2)]
print(bands)