from re import match
import re


class Processing:

    def __init__(self, data, params):
        self.filter_params = []  # Пока пусто
        self.sort_params = []  # Пока пусто
        self.data = data  # Данные
        self.params = params  # Переданные параметры
        self.warnings = []  # Пока пусто
        # Запускаем метод, который наполнит переменные
        self._separate_params()

    def _separate_params(self):
        print("Received parameters:", self.params)  # Печать всех параметров запроса
        for key, value in self.params.items():
            print(f"Processing key: {key}, value: {value}")  # Печать каждого параметра
            # Если параметр сортировки
            if match := re.match(r'sort\[(.+?)\]', key):
                field = match.group(1)  # Достаём имя поля, например "name"
                self.sort_params.append({field: value})  # Наполняем список сортировки

            # Если параметр фильтрации
            elif match := re.match(r'filter\[(.+?)\]\[(.+?)\]', key):
                field, operation = match.groups()
                print(f"Filter found: field={field}, operation={operation}, value={value}")  # Печать фильтров
                self.filter_params.append({f"{field}_{operation}": value})  # Наполняем список фильтров

    def apply_sort(self, data):
        sorted_data = data
        for sort_param in self.sort_params:
            for field, value in sort_param.items():
                if value == "asc":
                    sorted_data = sorted(data, key=lambda x: x[field])
                elif value == "desc":
                    sorted_data = sorted(data, key=lambda x: x[field], reverse=True)
        return sorted_data

    def apply_filter(self, item):
        if not isinstance(item, dict):
            return False
        print("Applying filter to item:", item)  # Печать текущего элемента, к которому применяется фильтр
        for filter_item in self.filter_params:
            print(f"Checking filter: {filter_item}")  # Печать фильтров
            if not self._match_filter(filter_item, item):
                return False
        return True

    def _match_filter(self, filter_item, item):
        for key, value in filter_item.items():
            field, operation = key.split("_", 1)
            print(f"Matching filter: field={field}, operation={operation}, value={value}")  # Печать текущего фильтра

            if isinstance(item[field], int):
                value = int(value)
            elif isinstance(item[field], float):
                value = float(value)

            if operation == "$in":
                if value in item[field]:
                    return True
                else:
                    return False
            elif operation == "$eq":
                if item[field] == value:
                    return True
                return False
            elif operation == "$gt":
                if item[field] > value:
                    return True
                return False
            elif operation == "$lt":
                if item[field] < value:
                    return True
                return False
            elif operation == "$gte":
                if item[field] >= value:
                    return True
                return False
            elif operation == "$lte":
                if item[field] <= value:
                    return True
                return False
            else:
                print(f"Operation {operation} is not supported")
                warning = {
                    "message": f"Operation {operation} is not supported",
                    "field": field
                }
                if warning not in self.warnings:
                    self.warnings.append(warning)
                return True
        return True

    def process_data(self):
        filtered_data = [item for item in self.data if self.apply_filter(item)]
        print("Filtered data:", filtered_data)  # Печать отфильтрованных данных
        sorted_data = self.apply_sort(filtered_data)
        print("Sorted data:", sorted_data)  # Печать отсортированных данных
        return {
            "data": sorted_data,
            "warnings": self.warnings
        }
