import json
import pprint
vaccinelist = []
jsonvaccinelist = {}
vaccineNum = int(input("Enter number of received vaccine: "))
for i in range(vaccineNum):
    vaccinename = input("Enter vaccine name ({}): ".format(i+1))
    vaccinelist.append("Received vaccine({})".format(i+1))
    vaccinelist.append(vaccinename)
vaccinelistJson = {vaccinelist[i]: vaccinelist[i + 1] for i in range(0, len(vaccinelist), 2)}
pretty_print_json = pprint.pformat(vaccinelistJson).replace("'", '"')
pretty_print_json = json.loads(pretty_print_json)
print(pretty_print_json)
print(type(pretty_print_json))