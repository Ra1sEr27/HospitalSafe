import os
import json
directory_patient = 'section3_staff'
for filename in os.listdir(directory_patient): #encrypt local patient's documents and upload to MongoDB
        f = os.path.join(directory_patient, filename)
        # checking if it is a file
        if os.path.isfile(f):
            
            #print('patient sec :',target_section)
            
            with open(f, 'rb') as file:
                local_file = file.read()
                local_file = local_file.decode('ISO-8859-1')
            data = json.loads(local_file)
            doc_string = json.dumps(data)
            # print(type(local_file))
            # print(local_file)
            print(type(doc_string))
            print(doc_string)