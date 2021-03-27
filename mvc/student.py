
class Student:

    def __init__(self):
        self.__name = None
        self.__age = None

    def set_name(self, name) -> None:
        self.__name = name

    def set_age(self, age) -> None:
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class StudentControler:

    def __init__(self):
        self.model = None
        self.view = None

    def set_model(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view

    # for the user
    def set_name(self, name):
        self.model.set_name(name=name)

    def set_age(self, age):
        self.model.set_age(age=age)

    # for the view
    def get_name(self):
        return self.model.get_name()

    def get_age(self):
        return self.model.get_age()

    def update_view(self):
        self.view.print_message(name=self.model.get_name(), age=self.model.get_age())


class View:
    @staticmethod
    def print_message(name, age):
        print("\nnom = ", name)
        print("age = ", age, " ans")


class View_EN:
    @staticmethod
    def print_message(name, age):
        print("\nname : ", name)
        print("age : ", age, " years")

class View_one_line:
    @staticmethod
    def print_message(name, age):
        print("\nVotre nom est ", name, "et vous avez ", age, " ans")


def main():
    my_stud = Student()

    my_view = View()
    my_view_en = View_EN()
    my_view_one = View_one_line()

    my_controler = StudentControler()

    my_controler.set_model(model=my_stud)
    my_controler.set_view(view=my_view)

    my_controler.set_name("mimi")
    my_controler.set_age(6)

    my_controler.update_view()

    my_controler.set_view(view=my_view_en)
    my_controler.update_view()

    my_controler.set_view(view=my_view_one)
    my_controler.update_view()



if __name__ == "__main__":
    main()