import random
import yaml
import os
from common_functions import import_yaml_file, find_files_by_extension
from pprint import pprint
from build_char import NPCCharacter
from build_store import StoreBuilder, store_types
from build_service import BuildServices, service_types
from fastapi import FastAPI, HTTPException
from fastapi.requests import Request

script_dir = os.path.dirname(os.path.abspath(__file__))
town_data_yaml_path = os.path.join(script_dir, 'town_data', 'town_name_data.yml')
town_name_data = import_yaml_file(town_data_yaml_path)

store_types_keys = list(store_types.keys())
service_types_keys = list(service_types.keys())
print (store_types_keys)
print (service_types_keys)

def build_town_name():
    town_first_name = random.choice(town_name_data['names']['first'])
    town_last_name = random.choice(town_name_data['names']['second'])
    town_name = f"{town_first_name} {town_last_name}"
    return town_name

def build_town():    
    town = {'town_name': build_town_name()}

    for each in store_types_keys:
        town[each] = StoreBuilder(each).build_store()
    for each in service_types_keys:
        town[each] = BuildServices(each).build_service()
    town['mayor'] = NPCCharacter().__dict__
    town['guard_1'] = NPCCharacter().__dict__
    town['guard_2'] = NPCCharacter().__dict__
    town['guy_at_bar_1'] = NPCCharacter().__dict__
    town['guy_at_bar_2'] = NPCCharacter().__dict__
    town['random_npc'] = []
    for i in range(0, 5):
        town['random_npc'].append(NPCCharacter().__dict__)
    return town

pprint (build_town())


