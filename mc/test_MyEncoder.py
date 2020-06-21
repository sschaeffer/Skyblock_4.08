from MyEncoder import MyEncoder,NoIndent
import json

# Example of using it to do get the results you want.

alfa = [('a','b','c'), ('d','e','f'), ('g','h','i')]
data = [(1,2,3), (2,3,4), (4,5,6)]

data_struct = {
    'data': [NoIndent(elem) for elem in data],
    'alfa': [NoIndent(elem) for elem in alfa],
}

print(json.dumps(data_struct, cls=MyEncoder, sort_keys=True, indent=4))

# test custom JSONEncoder with json.dump()
with open('data_struct.json', 'w') as fp:
    json.dump(data_struct, fp, cls=MyEncoder, sort_keys=True, indent=4)
    fp.write('\n')  # Add a newline to very end (optional).