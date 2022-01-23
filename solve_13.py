"""
    Showcase example of multiple level inheritance

"""


class electronic_device:

    def __init__(self):
        self.Battery = input("Enter is it on Battery (1) OR Charger (0) ")
        self.vendor = input("Enter Amazon OR FlipKart ")
        self.device_size = input("Enter Small OR Big ")

    def print_elc_device(self):
        return f"\nDevice was purchased from {self.vendor} with device size as{self.device_size}" \
               f"and battery {self.Battery}"


class pocket_gaget(electronic_device):
    is_pocket = input("Enter it's a pocket size Y -Yes and N -No")

    def print_pocket_gaget(self):
        return f"\nIs device a pocket size device : {self.is_pocket} "


class phone(pocket_gaget):
    memory = input("Enter size of the memory : ")

    def print_phone(self):
        return f"\nThe memory of phone is {self.memory}"


my_phone = phone()
print(my_phone.print_elc_device())
print(my_phone.print_pocket_gaget())
print(my_phone.print_phone())
