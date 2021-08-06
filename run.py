from view import countdown, countdown2, countdown3
from utils import ClassDecorator

countdown(123)
countdown2("A")
countdown3(1 + 2)


decorator = ClassDecorator()
decorator.function()