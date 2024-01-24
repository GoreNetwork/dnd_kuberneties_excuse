import random
import yaml
import os
from common_functions import import_yaml_file, find_files_by_extension
from pprint import pprint
from build_char import NPCCharacter

def get_store_types():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    npc_yaml_path = os.path.join(script_dir, 'store_items')
    store_types_with_path = find_files_by_extension(npc_yaml_path, '.yml')
    store_types = {}
    for each in store_types_with_path:
        tmp = each.split('/')[-1].split('.')[0]
        tmp = tmp.split('\\')[-1].split('.')[0]
        store_types[tmp] = import_yaml_file(each)
    return store_types

store_types = get_store_types()

script_dir = os.path.dirname(os.path.abspath(__file__))
npc_yaml_path = os.path.join(script_dir, 'store_items')
store_types_with_path = find_files_by_extension(npc_yaml_path, '.yml')
store_types = {}
for each in store_types_with_path:
    tmp = each.split('/')[-1].split('.')[0]
    tmp = tmp.split('\\')[-1].split('.')[0]
    store_types[tmp] = import_yaml_file(each)
# pprint (store_types)

class StoreBuilder():
    def __init__(self, store_type):
        self.store_type = store_type
        self.store_info= store_types[self.store_type]
        self.owner_data = NPCCharacter()

    def build_store(self):
        store_name = self.combine_names()
        rare_items = self.get_random_rare_items()
        common_items = self.get_common_items()
        owner_data = {
            'race': self.owner_data.race,
            'gender': self.owner_data.gender,
            'name': f'{self.owner_data.first_name} {self.owner_data.last_name}',
            'motivation': self.owner_data.motivation

        }
        output = {
            'store_name': store_name,
            'rare_items': rare_items,
            'common_items': common_items,
            'owner_data': owner_data,
        }

        return output

    def combine_names(self):
        first_name = self.get_first_names()
        second_name = self.get_second_names()
        return f"{first_name} {second_name}"

    def get_first_names(self):
        first_names = self.store_info['names']['first']
        return random.choice(first_names)

    def get_second_names(self):
        second_names = self.store_info['names']['second']
        return random.choice(second_names)

    def get_random_rare_items(self):
        rare_items_keys = list(self.store_info['rare'].keys())
        selected_items = []
        for _ in range(3):
            selected_item = random.choice(rare_items_keys)
            selected_items.append(selected_item)
        rare_items_and_prices = {}
        for each in selected_items:
            rare_items_and_prices[each] = self.store_info['rare'][each]

        return rare_items_and_prices

    def get_common_items(self):
        return self.store_info['common']


    def import_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data

    def get_store_items_folder_path(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        store_items_folder_path = os.path.join(script_dir, 'store_items')
        return store_items_folder_path


