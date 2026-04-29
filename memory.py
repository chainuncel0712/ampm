import json
import os

class LongTermMemory:
    def __init__(self, storage_path='memory.json'):
        self.storage_path = storage_path
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        return {}

    def save_memory(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def remember(self, key, value):
        self.memory[key] = value
        self.save_memory()

    def recall(self, key):
        return self.memory.get(key, None)

    def forget(self, key):
        if key in self.memory:
            del self.memory[key]
            self.save_memory()

    def clear_memory(self):
        self.memory.clear()
        self.save_memory()