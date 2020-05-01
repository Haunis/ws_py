"""
就是演练类的使用,没啥技术含量

一个类的属性,可以是另外一个类的对象
"""


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return self.name + ": " + str(self.area)
        # return "%s ,%d" % (self.name, self.area)


class Room:
    def __init__(self, room_type, total_area):
        self.room_type = room_type
        self.total_area = total_area
        # self.furniture_list = []
        self.furniture_list = None

    def add_furniture(self, furniture):
        if self.furniture_list is None:
            self.furniture_list = []
        if furniture.area <= self.get_rest_area():
            self.furniture_list.append(furniture)
        else:
            print("剩余面积不足; 剩余面积=%d,家具面积%d" % (self.get_rest_area(), furniture.area))

    def get_rest_area(self):
        if self.furniture_list is None:
            return 0
        if len(self.furniture_list) == 0:
            return self.total_area
        else:
            area = 0
            for furniture in self.furniture_list:
                area += furniture.area
            return self.total_area - area

    def __str__(self):
        return (("room_type:%s\ntotal_area:%d\nrest_area:%d\nfurniture:%s"
                 % (self.room_type, self.total_area, self.get_rest_area(), self.furniture_list)))


room = Room("两室一厅", 60)

bed = Furniture("床", 30)
desk = Furniture("书桌", 30)
print(bed)

room.add_furniture(bed)
room.add_furniture(desk)
print(room)
