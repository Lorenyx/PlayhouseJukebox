dc = {'name': 12, 'age': 45, 'height':69}

print([x for x in dc.items() if x in ['name', 'age']])