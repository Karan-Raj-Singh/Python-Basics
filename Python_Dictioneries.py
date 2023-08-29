x={
    "name":"karan","age":24
}
print(x)
print(x["name"])
print(x.get("name"))

# List of dictioneries
z=[{"name":"karan","age":24},{"name":"raj","age":24}]
print(z)
x={
    "name":"karan","age":24
}
#adding new key-value pair in the dictionery
x["specialisation"]="python"
print(x)
#ammend the key value pair
x["name"]="singh"
print(x)
# for loop for extracting the key value pair  .items()
for keys,values in x.items():
    print(keys)
    print(values)
