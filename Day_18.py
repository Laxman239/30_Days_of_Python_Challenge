class Meta(type):
    def __new__(self, class_name, bases, attrs):

        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, a)
    

class Car(metaclass = Meta):
    x = "tata"
    y = "mahindra"

    def hello(self):
        return "hi"

d = Car()
print(d.HELLO())