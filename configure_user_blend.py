from typing import List, Dict, Any
import json

users_blend_path = 'data/blends/01.json'

def load_users_data() -> List[Dict[str, Any]]:
    data = []

    with open(users_blend_path, 'r') as users_file:
        data = json.load(users_file)

    return data