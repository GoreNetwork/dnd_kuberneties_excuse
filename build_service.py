import random
import yaml
import os
from common_functions import import_yaml_file, find_files_by_extension
from pprint import pprint
from build_char import NPCCharacter

def get_service_types():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    npc_yaml_path = os.path.join(script_dir, 'services')
    service_types_with_path = find_files_by_extension(npc_yaml_path, '.yml')
    service_types = {}
    for each in service_types_with_path:
        tmp = each.split('/')[-1].split('.')[0]
        tmp = tmp.split('\\')[-1].split('.')[0]
        service_types[tmp] = import_yaml_file(each)
    return service_types

service_types = get_service_types()

class BuildServices():
    def __init__(self, service_type):
        self.service_type = service_type
        self.service_info= service_types[self.service_type]
        self.owner_data = NPCCharacter()

    def build_service(self):
        service_name = self.combine_names()
        services = self.get_services()
        owner_data = {
            'race': self.owner_data.race,
            'gender': self.owner_data.gender,
            'name': f'{self.owner_data.first_name} {self.owner_data.last_name}',
            'motivation': self.owner_data.motivation

        }
        output = {
            'name': service_name,
            'services': services,
            'owner_data': owner_data,
        }

        return output

    def get_services(self):
        final_services = {}
        for each in self.service_info['services']:
            low_value = self.service_info['services'][each][0]
            high_value = self.service_info['services'][each][1]
            final_services[each] = f'{random.randint(low_value, high_value)} C'
        return final_services

    def combine_names(self):
        first_name = self.get_first_names()
        second_name = self.get_second_names()
        return f"{first_name} {second_name}"

    def get_first_names(self):
        first_names = self.service_info['names']['first']
        return random.choice(first_names)

    def get_second_names(self):
        second_names = self.service_info['names']['second']
        return random.choice(second_names)


    def import_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data

    def get_store_items_folder_path(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        store_items_folder_path = os.path.join(script_dir, 'service')
        return store_items_folder_path


