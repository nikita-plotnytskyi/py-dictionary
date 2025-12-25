from typing import Any


class Dictionary:

    def __init__(self) -> None:
        self.my_dict = ["", "", "", "", "", "", "", "", ]
        self.max_length = 8
        self.max_items = self.max_length * 2 // 3

    def __setitem__(self, key: Any, value: Any) -> None:
        if len(self) >= self.max_items:
            self.old_list = self.reset_dict()
            for item in self.old_list:
                if item != "":
                    self.add_new_item(*item)

        self.add_new_item(key, value)

    def __getitem__(self, key: Any) -> Any:
        index_key = hash(key) % self.max_length
        change_index = index_key
        try:
            while True:
                if self.my_dict[change_index][0] == key:
                    return self.my_dict[change_index][1]
                change_index = (change_index + 1) % self.max_length
                if change_index == index_key:
                    raise KeyError(key)
        except IndexError:
            raise KeyError(key)

    def __len__(self) -> int:
        return len([elem for elem in self.my_dict if elem != ""])

    def add_new_item(self, key: Any, value: Any) -> None:
        index_key = hash(key) % self.max_length

        while self.my_dict[index_key] != "":
            if self.my_dict[index_key][0] == key:
                break
            index_key = (index_key + 1) % self.max_length

        self.my_dict[index_key] = (key, value)

    def reset_dict(self) -> list:
        self.max_length *= 2
        self.max_items = self.max_length * 2 // 3
        old_dict = self.my_dict.copy()
        self.my_dict = [""] * self.max_length
        return old_dict
