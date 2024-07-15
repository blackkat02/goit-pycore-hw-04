def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()

            total = 0
            count_employ = 0

            for line in lines:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count_employ += 1
                except ValueError:
                    print(f"Неправильний формат рядка: {line.strip()}")

            if count_employ == 0:
                raise ValueError("Файл не містить коректних даних про зарплати.")

            average = total / count_employ
            return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None


total, average = total_salary(r"C:\Users\Admin\PycharmProjects\goit-pycore-hw-04+/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
