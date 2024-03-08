
from PySide6.QtWidgets import QHBoxLayout


class ModelSelector(QHBoxLayout):
        a = "Helo"
        def __init__(self):
                QHBoxLayout.__init__(self)
                b = "asda{self.a}"
                print(b)

                print(asdas)
                print()
                print("sad{}")

if __name__=="__main__":
        model_selector = ModelSelector()