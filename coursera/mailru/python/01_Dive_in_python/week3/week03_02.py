import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if body_whl == '':
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0
        else:
            self.body_width = float(body_whl.split('x')[0])
            self.body_height = float(body_whl.split('x')[1])
            self.body_length = float(body_whl.split('x')[2])

    def get_body_volume(self):
        return (self.body_width * self.body_height * self.body_length)


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                try:
                    print(row)
                    if ((row[0] and row[1] and row[3] and row[5])  != ''):
                        if (row[0] == 'car' and row[2] != ''):
                            car_list.append(Car(row[1], row[3], float(row[5]), int(row[2])))
                        elif (row[0] == 'truck'):
                            car_list.append(Truck(row[1], row[3], float(row[5]), row[4]))
                        elif (row[0] == 'spec_machine' and row[6]):
                            car_list.append(SpecMachine(row[1], row[3], float(row[5]), row[6]))
                except IndexError:
                    continue
    except IOError as ex:
        print(ex)
    return car_list