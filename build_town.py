import random
import yaml
import os
from common_functions import import_yaml_file, find_files_by_extension
from pprint import pprint
from build_char import NPCCharacter
from build_store import StoreBuilder, store_types
from build_service import BuildServices, service_types

store_types_keys = list(store_types.keys())
service_types_keys = list(service_types.keys())
print (store_types_keys)
print(service_types_keys)

town = {}

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

pprint(town)


