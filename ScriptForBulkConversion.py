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
  
