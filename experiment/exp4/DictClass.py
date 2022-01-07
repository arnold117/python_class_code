class DictClass:
    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        if key in self.dict.keys():
            assert isinstance(key, object)
            del self.dict[key]
            return self.dict
        else:
            return "not found"

    def get_dict(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return "not found"

    def get_key(self, key):
        for key in self.dict.keys():
            print(key, end=', ')

    def update_dict(self, dict2):
        self.dict.update(dict2)
        for value in dict.values():
            print(value, end=', ')
        return self.dict


if __name__ == '__main__':
    dict1 = {"name": "Arnold", "age": "19", "gender": "male"}
    a = DictClass(dict1)
    key1 = str(input("What are you looking for?"))
    print(a.get_dict(key1))
    key2 = str(input("What do you want to delete?"))
    print(a.del_dict(key2))
    key3 = str(input("Are you looking for any keys?"))
    print(a.get_key(key3))
