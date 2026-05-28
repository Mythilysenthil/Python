myfam={'child1':{"name":"Naveen","year":"2002"},
       'child2':{"name":"Mythily","year":"2002"}}
print(myfam["child2"]['name'])


thisdict={"brand":"Ford","model":"Mustang","years":1964}
print(thisdict)
del thisdict["model"]
print(thisdict)
#traversal
for x in thisdict :
    print(x,thisdict[x])