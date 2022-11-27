import json
import os.path

class FileStorage():
    __file_path  = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects 
    
    def new(self, obj):
        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj
    
    def save(self):
        new_obj = {}
        for key,value in FileStorage.__objects.items():
            new_obj[key] = value.to_dict()
            with open(FileStorage.__file_path, "w") as json_file:
                json.dump(new_obj, json_file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                for key,value in json.loads(json_file.read()).items():
                    FileStorage.__objects[key] = value
