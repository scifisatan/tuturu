import json
import os


class Assign:
    _path = ""
    _assign = {}

    def __init__(self, path):
        self._path = path
        try:
            with open(self._path, "r") as f:
                self._assign = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass


    def get(self, name):
        return self._assign[name] if name in self._assign else False

    def write(self, name, content):
        self._assign[name] = content
        self._save()


    def _save(self):
        os.makedirs(os.path.dirname(self._path), exist_ok=True)
        with open(self._path, "w") as f:
            json.dump(self._assign, f)
