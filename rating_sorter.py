import json 

with open('students.json') as jsonfile:

    json_str = jsonfile.read()

    data = json.loads(json_str) 

    students = sorted(data,key = lambda x : int(x['score']))

    for i, student in enumerate(students, start=1):
        student['rank'] = i

    json_str = json.dumps(students,indent=4)

with open('rating.json','w') as jsonfile:

    jsonfile.write(json_str)