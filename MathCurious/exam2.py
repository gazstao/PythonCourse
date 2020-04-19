class MyClass:
    class_property = 'Hello'

object_one = MyClass()
object_two = MyClass()

MyClass.class_property = "Goodbye"

print(object_two.class_property)