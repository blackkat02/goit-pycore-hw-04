def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            cats_info = []

            for line in lines:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Неправильний формат рядка: {line.strip()}")

            return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None


print(get_cats_info(r"C:\Users\Admin\PycharmProjects\goit-pycore-hw-04+/cats_info.txt"))
