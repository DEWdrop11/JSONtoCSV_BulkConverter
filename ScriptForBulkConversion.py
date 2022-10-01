import json
from pprint import pprint
# we are using pprint for making the output more readable.
with open('descriptions/ISIC_0000000') as f:
    data = json.load(f)
    pprint(data)
    
    
import os
import json
import csv

def get_list_of_json_files():
    list_of_files = os.listdir('descriptions')
    return list_of_files

def create_list_from_json(jsonfile):

    with open(jsonfile) as f:
        data = json.load(f)

    data_list = []  # create an empty list

    # append the items to the list in the same order.
    data_list.append(data['_id'])
    data_list.append(data['_modelType'])
    data_list.append(data['creator']['_id'])
    data_list.append(data['creator']['name'])
    data_list.append(data['dataset']['_accessLevel'])
    data_list.append(data['dataset']['_id'])
    data_list.append(data['dataset']['description'])
    data_list.append(data['dataset']['name'])
    data_list.append(data['meta']['acquisition']['image_type']) #here we are reading in the nested JSON
    data_list.append(data['meta']['acquisition']['pixelsX'])
    data_list.append(data['meta']['acquisition']['pixelsY'])
    data_list.append(data['meta']['clinical']['age_approx'])
    data_list.append(data['meta']['clinical']['benign_malignant'])
    data_list.append(data['meta']['clinical']['diagnosis'])
    data_list.append(data['meta']['clinical']['diagnosis_confirm_type'])
    data_list.append(data['meta']['clinical']['melanocytic'])
    data_list.append(data['meta']['clinical']['sex'])
    data_list.append(data['meta']['unstructured']['diagnosis'])
    # In few json files, the race was not there so using KeyError exception to add '' at the place
    try:
        data_list.append(data['meta']['unstructured']['race'])
    except KeyError:
        data_list.append("")  # will add an empty string in case race is not there.
    data_list.append(data['name'])

    return data_list
  
    
    
  def write_csv():
    list_of_files = get_list_of_json_files()
    for file in list_of_files:
        row = create_list_from_json(f'descriptions/{file}')  # create the row to be added to csv for each file (json-file)
        with open('output.csv', 'a') as c:
            writer = csv.writer(c)
            writer.writerow(row)
        c.close()
        
if __name__=="__main__":
    write_csv()
    
import pandas as pd
import json

with open('example_1.json') as f:
    data = json.load(f)
    
    
    
from pandas.io.json import json_normalize
df = json_normalize(data)
print(df)

# Output
#   color  fruit   size
# 0   Red  Apple  Large



df.to_csv('output_u.csv', index=False)

import pandas as pd
import json
from pandas.io.json import json_normalize
with open('ISIC_0000000', 'r') as f:
    data = json.load(f)
df = json_normalize(data)
print(df.columns)

# Output

Index(['_id', '_modelType', 'created', 'creator._id', 'creator.name',
       'dataset._accessLevel', 'dataset._id', 'dataset.description',
       'dataset.license', 'dataset.name', 'dataset.updated',
       'meta.acquisition.image_type', 'meta.acquisition.pixelsX',
       'meta.acquisition.pixelsY', 'meta.clinical.age_approx',
       'meta.clinical.anatom_site_general', 'meta.clinical.benign_malignant',
       'meta.clinical.diagnosis', 'meta.clinical.diagnosis_confirm_type',
       'meta.clinical.melanocytic', 'meta.clinical.sex',
       'meta.unstructured.diagnosis', 'meta.unstructured.id1',
       'meta.unstructured.localization', 'meta.unstructured.site', 'name',
       'notes.reviewed.accepted', 'notes.reviewed.time',
       'notes.reviewed.userId', 'notes.tags', 'updated'],
      dtype='object')



to_be_dropped = ['created','dataset.license', 'dataset.updated', 'meta.clinical.anatom_site_general', 'meta.unstructured.id1',
       'meta.unstructured.localization', 'meta.unstructured.site',
       'notes.reviewed.accepted', 'notes.reviewed.time',
       'notes.reviewed.userId', 'notes.tags', 'updated' ]
df.drop(columns = to_be_dropped, inplace = True)



df.to_csv('output.csv', index=False)


 
