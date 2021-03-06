import os
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from cv2 import trace
from loguru import logger

from View import ViewWindow
from Worker import Worker


class MainController:
    def __init__(self, view: ViewWindow) -> None:
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.showFullScreen()
        self.view.app = QApplication.instance()  # 实例化APP，获取app的指针
        self.view.Worker = Worker(self.view)
        self.view.Worker.finished.connect(self.view.setDefaultView)

    def btnStart_clicked(self):
        self.view.btnStart.setEnabled(False)
        self.view.LabelFront.setText('加载中')
        self.view.LabelRear.setText('加载中')
        self.view.BarCodeValue.setFocus()
        self.view.Worker.start()
        self.view.Worker.FrontImage.connect(self.view.UpdateFrontSlot)
        self.view.Worker.RearImage.connect(self.view.UpdateRearSlot)
        self.view.Worker.Alert.connect(self.view.runAlert)

    def btnStop_clicked(self):
        self.view.Worker.stop()
        self.view.btnStart.setEnabled(True)

    def shutdown(self):
        self.view.Worker.stop()
        self.view.btnStart.setEnabled(True)
        logger.info('quit app')
        self.view.app.quit()

    def getConfig(self):
        left_lensPos = self.view.left_lensPos_value.value()
        left_exp_time = self.view.left_exp_time_value.value()
        left_sens_ios = self.view.left_sens_ios_value.value()
        right_lensPos = self.view.right_lensPos_value.value()
        right_exp_time = self.view.right_exp_time_value.value()
        right_sens_ios = self.view.right_sens_ios_value.value()
        return [left_lensPos, left_exp_time, left_sens_ios, right_lensPos, right_exp_time, right_sens_ios, self.view.Worker.Mxids]

    def btn_save(self):
        self.view.BarCodeValue.setFocus()
        try:
            self.view.Worker.save_yml(self.getConfig())
        except Exception as e:
            print(traceback.print_exc())
            logger.error(e)

    def barcode_edit(self):
        barcode = self.view.BarCodeValue.text().strip()
        if len(barcode) != 0 and not self.view.btnStart.isEnabled():
            self.view.Worker.left_send_barcode.send(barcode)
            self.view.Worker.right_send_barcode.send(barcode)
            self.view.Worker.bar_code = barcode
            self.view.BarCodeValue.clear()

    def change_left_lenPos(self):
        self.view.BarCodeValue.setFocus()
        self.view.left_lensPos_edit.setText(str(self.view.left_lensPos_value.value()))
        self.view.Worker.left_new_value['lenPos_new'].value = self.view.left_lensPos_value.value()
        self.view.autofocusleft.setChecked(False)

    def change_left_exp_time(self):
        self.view.BarCodeValue.setFocus()
        self.view.left_exp_time_edit.setText(str(self.view.left_exp_time_value.value()))
        self.view.Worker.left_new_value['exp_time_new'].value = self.view.left_exp_time_value.value()
        self.view.autoexpleft.setChecked(False)

    def change_left_sens_ios(self):
        self.view.BarCodeValue.setFocus()
        self.view.left_sens_ios_edit.setText(str(self.view.left_sens_ios_value.value()))
        self.view.Worker.left_new_value['sens_ios_new'].value = self.view.left_sens_ios_value.value()
        self.view.autoexpleft.setChecked(False)

    def change_right_lenPos(self):
        self.view.BarCodeValue.setFocus()
        self.view.right_lensPos_edit.setText(str(self.view.right_lensPos_value.value()))
        self.view.Worker.right_new_value['lenPos_new'].value = self.view.right_lensPos_value.value()
        self.view.autofocusright.setChecked(False)

    def change_right_exp_time(self):
        self.view.BarCodeValue.setFocus()
        self.view.right_exp_time_edit.setText(str(self.view.right_exp_time_value.value()))
        self.view.Worker.right_new_value['exp_time_new'].value = self.view.right_exp_time_value.value()
        self.view.autoexpright.setChecked(False)

    def change_right_sens_ios(self):
        self.view.BarCodeValue.setFocus()
        self.view.right_sens_ios_edit.setText(str(self.view.right_sens_ios_value.value()))
        self.view.Worker.right_new_value['sens_ios_new'].value = self.view.right_sens_ios_value.value()
        self.view.autoexpright  .setChecked(False)

    def change_edit_value(self):
        self.view.BarCodeValue.setFocus()

    def change_left_auto_exp(self):
        self.view.BarCodeValue.setFocus()
        if self.view.autoexpleft.isChecked():
            self.view.Worker.left_status['auto_exp_status'].value = 2
        else:
            self.view.Worker.left_status['auto_exp_status'].value = 1

    def change_left_auto_focus(self):
        self.view.BarCodeValue.setFocus()
        if self.view.autofocusleft.isChecked():
            self.view.Worker.left_status['auto_focus_status'].value = 2
        else:
            self.view.Worker.left_status['auto_focus_status'].value = 1
    
    def change_right_auto_exp(self):
        self.view.BarCodeValue.setFocus()
        if self.view.autoexpright.isChecked():
            self.view.Worker.right_status['auto_exp_status'].value = 2
        else:
            self.view.Worker.right_status['auto_exp_status'].value = 1

    def change_right_auto_focus(self):
        self.view.BarCodeValue.setFocus()
        if self.view.autofocusright.isChecked():
            self.view.Worker.right_status['auto_focus_status'].value = 2
        else:
            self.view.Worker.right_status['auto_focus_status'].value = 1
    
    def clicked_Openpath(self):
        start_directory = 'images'
        os.startfile(start_directory)
        self.view.BarCodeValue.setFocus()
    
    def setAllScreen(self):
        self.view.setWindowState(Qt.WindowFullScreen)
        self.view.BarCodeValue.setFocus()

    def setNoAllScreen(self):
        self.view.setWindowState(Qt.WindowActive)
        self.view.BarCodeValue.setFocus()