from bot.settings import *


def track_processed_items(func):
    processed_items = set()
    def wrapper(self, dictionary):
        for key, value in dictionary.items():
            if key not in processed_items: 
                func(self, {key: value})
                processed_items.add(key)      
    return wrapper

pages = set()