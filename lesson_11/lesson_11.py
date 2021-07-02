import json

fpath = 'HW.json'
fpath_res = 'HW_result_task_done.json'
data = {}
result = {}
with open(fpath) as json_file:
    data = json.load(json_file)

# loop thrhoug keys in dict from json file
for key, lst in data.items():
    dict_intitial = {}
    # loop through elements in list of employee
    for el in lst:
        # el is a dict with info for employee
        firstName = el.get('firstName')
        lastName = el.get('lastName')
        fullName = '{} {}'.format(firstName, lastName)
        d_types = {
            'int': 'int',
            'str': 'string',
            'float': 'float',
            'NoneType': 'none_type',
            'bool': 'bool'
        }
        d_res = dict.fromkeys(d_types.values(), [])
        # generate list of tuples
        lst_tpl =  [(tpl[0], tpl[1].__class__.__name__) for tpl in el.items()]
        for tpl in lst_tpl:
            value, typeValye = tpl
            # value = str(value)
            custom_value = d_types.get(typeValye)
            d_res[custom_value] = d_res.get(custom_value, []) + [value]
        dict_intitial[fullName] = d_res
    result[key] = dict_intitial

with open(fpath_res, 'w') as file:
    json.dump(result, file, indent=2)


