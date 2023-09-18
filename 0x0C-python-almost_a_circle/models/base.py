#!/usr/bin/python3
"""defines a base class"""
import json
import csv
import os
import turtle


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """new Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes to JASON string representation of list_objs to a file"""

        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w", encoding="utf-8") as file:
            list = []
            if len(list_objs) == 0 or list_objs is None:
                json.dump(json.loads(cls.to_json_string(list)), file)
            else:
                for element in list_objs:
                    list.append(element.to_dictionary())
                json.dump(json.loads(cls.to_json_string(list)). file)

    @staticmethod
    def from_json_string(json_string):
        """returns the deserialization of JSON string"""

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, encoding="utf-8") as file:
                list = []
                dict = cls.from_json_string(json.dumps(json.load(file)))
                for element in dict:
                    list.append(cls.create(**element))
                return list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write teh csv serialization of a list of objects to csv file"""

        file_name = cls.__name__ + ".csv"
        with open(file_name, mode="w", newline="") as file:
            if list_objs == [] or list_objs is None:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserialiuze csv from a file"""

        file_name = cls.__name__ + "csv"
        list = []

        if os.path.exists(file_name):
            with open(file_name, mode="r") as file:
                reader = csv.reader(file, delimiter=",")
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    field_names = ["id", "size", "x", "y"]
                for i, row in enumerate(reader):
                    if i > 0:
                        element = cls(1, 1)
                        for j, k in enumerate(row):
                            if k:
                                setattr(element, field_names[j], int(k))
                        list.append(element)
        return list
