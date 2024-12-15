import json
import os
from typing import Dict, List

def env(k: str) -> str:
    return os.getenv(
        key=k
    )

def config(path: str) -> Dict[str, List[int]]:
    if os.path.isfile(path=path) is False:
        raise FileExistsError
    
    with open(path, "r") as file:
        data = json.load(file)

    return data

def lang(path: str = "./src/langs/ru.json") -> Dict[str, Dict[str, str]]:
    if os.path.isfile(path=path) is False:
        raise FileExistsError
    
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)

    return data