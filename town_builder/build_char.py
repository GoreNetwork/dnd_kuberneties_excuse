import random
import yaml
import os
from common_functions import import_yaml_file

script_dir = os.path.dirname(os.path.abspath(__file__))
npc_yaml_path = os.path.join(script_dir, 'npcs', 'race_names.yaml')
motivation_yaml_path = os.path.join(script_dir, 'npcs', 'modivations.yaml')
npc_data = import_yaml_file(npc_yaml_path)
nps_motivation = import_yaml_file(motivation_yaml_path)



class NPCCharacter:
    def __init__(self):
        self.race = self.get_random_race()
        self.gender = self.get_random_gender()
        self.first_name = self.get_random_first_name()
        self.last_name = self.get_random_last_name()
        self.motivation = self.get_random_motivation()

    def get_random_race(self):
        races = list(npc_data['race'].keys())
        return random.choice(races)

    def get_random_gender(self):
        genders = list(npc_data['race'][self.race]['first_name'].keys())
        return random.choice(genders)

    def get_random_first_name(self):
        first_names = npc_data['race'][self.race]['first_name'][self.gender]
        return random.choice(first_names)



    def get_random_last_name(self):
        last_names = npc_data['race'][self.race]['last_name']
        return random.choice(last_names)

    def get_random_motivation(self):
        nps_motivations = nps_motivation['npc_motivations']
        return random.choice(nps_motivations)['description']

