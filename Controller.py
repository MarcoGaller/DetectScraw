from View import ViewWindow
from Model import Model
from Infrastructure.Worker import Worker

class MainController:
    def __init__(self, model: Model, view: ViewWindow) -> None:
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.show()

    def btnStart_clicked(self):
        self.view.Worker = Worker()
        self.view.Worker.start()
        self.view.Worker.ImageUpdate.connect(self.view.ImageUpdateSlot)

    def btnStop_clicked(self):
        self.view.Worker.stop()




