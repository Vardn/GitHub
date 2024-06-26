import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

from gevent import os
from git import Repo

from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QLabel, QVBoxLayout, QInputDialog, QLineEdit, QMessageBox, \
    QMainWindow, QMenu, QMenuBar, QTableWidgetItem

from TundirBis import Ui_MainWindow
from Home_Page import Ui_Home
from kasa_r import Ui_Casa
from Cucak_caxser import Ui_Caxser
from Tundir_Ashxatavardz import Ui_Casa_ashx
from Vajarqpy import Ui_Vajarq
from TundirBis_2 import Ui_TundirBis_2
from Cupener import Ui_Cupener
from TundirCupe_1 import Ui_Cupe_1
from TundirCupe_2 import Ui_Cupe_2
from TundirCupe_3 import Ui_Cupe_3
from TundirCupe_4 import Ui_Cupe_4
from Jnjumner import Ui_Jnjumner







app = QtWidgets.QApplication(sys.argv)
Home = QtWidgets.QMainWindow()
ui = Ui_Home()
ui.setupUi(Home)
Home.show()


a = 0


# logic...
def openOtherWindow():
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    Home.close()
    MainWindow.show()


    def returnToHome():

        MainWindow.close()
        color_bis_1()
        Home.show()



    ui.pushButton_19.clicked.connect(returnToHome)
    ui.Hastatel.clicked.connect(returnToHome)
def color_bis_1():

    color_Bis_1 = open(r'C:\Users\varda\PycharmProjects\sel\Bis_1_Chek.txt', 'r', encoding='utf-8')
    Color_Bis_1 = color_Bis_1.read()
    color_Bis_1.close()
    color_Bis_2 = open(r'C:\Users\varda\PycharmProjects\sel\Bis_2_Chek.txt', 'r', encoding='utf-8')
    Color_Bis_2 = color_Bis_2.read()
    color_Bis_2.close()

    color_1 = open(r'C:\Users\varda\PycharmProjects\sel\Cupe_1_Chek.txt', 'r', encoding='utf-8')
    Color_1 = color_1.read()
    color_1.close()
    color_4 = open(r'C:\Users\varda\PycharmProjects\sel\Cupe_4_Chek.txt', 'r', encoding='utf-8')
    Color_4 = color_4.read()
    color_4.close()
    color_3 = open(r'C:\Users\varda\PycharmProjects\sel\Cupe_3_Chek.txt', 'r', encoding='utf-8')
    Color_3 = color_3.read()
    color_3.close()
    color_2 = open(r'C:\Users\varda\PycharmProjects\sel\Cupe_2_Chek.txt', 'r', encoding='utf-8')
    Color_2 = color_2.read()
    color_2.close()

    if len(Color_1) > 1 or len(Color_2) > 1 or len(Color_3) > 1 or len(Color_4) > 1:
        ui.Cupe.setStyleSheet('background: rgb(255,0,0);')
    else:
        ui.Cupe.setStyleSheet('background: rgb(255,255,255);')
    # if len(Color_1) == 0 and len(Color_2) == 0 and len(Color_3) == 0 and len(Color_4) == 0:
    #     return QtGui.QColor('#9C0006')

    if len(Color_Bis_1) > 1:
        ui.Bistro_1.setStyleSheet('background: rgb(255,0,0);')
    else:
        ui.Bistro_1.setStyleSheet('background: rgb(255,255,255);')
    # if len(Color_Bis_1) == 0:
    #     return QtGui.QColor('#9C0006')

    if len(Color_Bis_2) > 1:
        ui.Bistro_2.setStyleSheet('background: rgb(255,0,0);')
    else:
        ui.Bistro_2.setStyleSheet('background: rgb(255,255,255);')
    # if len(Color_Bis_2) == 0:
    #     return QtGui.QColor('#9C0006')



color_bis_1()

def Bistro_2():
    global TundirBis_2
    TundirBis_2 = QtWidgets.QMainWindow()
    ui = Ui_TundirBis_2()
    ui.setupUi(TundirBis_2)
    Home.close()
    TundirBis_2.show()
    def closBistro_2():
        TundirBis_2.close()
        color_bis_1()
        Home.show()
    ui.Hastatel_Bis_2.clicked.connect(closBistro_2)
    ui.pushButton_hetBistro_2.clicked.connect(closBistro_2)

def Jnjumner_fan():
    global Jnjumner
    Jnjumner = QtWidgets.QMainWindow()
    ui = Ui_Jnjumner()
    ui.setupUi(Jnjumner)
    Home.close()
    Jnjumner.show()

    bolor_Bar = []
    Jnj = open(r'C:\Users\varda\PycharmProjects\sel\Redact_Folder.txt', 'r', encoding='utf-8')
    jnj = Jnj.readlines()
    Jnj.close()

    vandax_index = 0
    anun_index = -1
    for i in range(0, len(jnj), 3):
        vandax_index += 1

        ui.tableWidget_Jnj.setRowCount(vandax_index)
        ui.tableWidget_Jnj.setColumnCount(3)
        ui.tableWidget_Jnj.setHorizontalHeaderLabels(('apranqanishi anvanum', 'qanak',  'Time'))
        ui.tableWidget_Jnj.setColumnWidth(0, 310)
        ui.tableWidget_Jnj.setColumnWidth(1, 90)
        ui.tableWidget_Jnj.setColumnWidth(2, 100)
        anun_index += 1
        ui.tableWidget_Jnj.setItem(anun_index, 0, QTableWidgetItem(str(jnj[i].replace('\n', ''))))
        ui.tableWidget_Jnj.setItem(anun_index, 1, QTableWidgetItem(str(jnj[i + 1].replace('\n', ''))))
        ui.tableWidget_Jnj.setItem(anun_index, 2, QTableWidgetItem(str(jnj[i + 2].replace('\n', ''))))


        print(Jnj)


    def Jnjumner_close():
        Jnjumner.close()
        Home.show()

    ui.pushButton_Jnjumner_het.clicked.connect(Jnjumner_close)


def Cup():
    global Cupener
    Cupener = QtWidgets.QMainWindow()
    ui = Ui_Cupener()
    ui.setupUi(Cupener)
    Home.close()

    color_bis_1()
    Cupener.show()
    def closCupener():
        Cupener.close()
        color_bis_1()
        Home.show()
    ui.pushButton_Cupe_het.clicked.connect(closCupener)

    def Cup_1():
        global Cupe_1
        Cupe_1 = QtWidgets.QMainWindow()
        ui = Ui_Cupe_1()
        ui.setupUi(Cupe_1)
        Cupener.close()
        Cupe_1.show()
        def closCupe_1():
            Cupe_1.close()
            color_bis_1()
            Home.show()

        ui.Hastatel_Cupe_1.clicked.connect(closCupe_1)
        ui.pushButton_hetCupe_1.clicked.connect(closCupe_1)
    def Cup_2():
        global Cupe_2
        Cupe_2 = QtWidgets.QMainWindow()
        ui = Ui_Cupe_2()
        ui.setupUi(Cupe_2)
        Cupener.close()
        Cupe_2.show()

        def closCupe_2():
            Cupe_2.close()
            color_bis_1()
            Home.show()

        ui.Hastatel_Cupe_2.clicked.connect(closCupe_2)
        ui.pushButton_hetCupe_2.clicked.connect(closCupe_2)
    def Cup_3():
        global Cupe_3
        Cupe_3 = QtWidgets.QMainWindow()
        ui = Ui_Cupe_3()
        ui.setupUi(Cupe_3)
        Cupener.close()
        Cupe_3.show()


        def closCupe_3():
            Cupe_3.close()
            color_bis_1()
            Home.show()

        ui.Hastatel_Cupe_3.clicked.connect(closCupe_3)
        ui.pushButton_hetCupe_3.clicked.connect(closCupe_3)
    def Cup_4():
        global Cupe_4
        Cupe_4 = QtWidgets.QMainWindow()
        ui = Ui_Cupe_4()
        ui.setupUi(Cupe_4)
        Cupener.close()
        Cupe_4.show()


        def closCupe_4():
            Cupe_4.close()
            color_bis_1()
            Home.show()

        ui.Hastatel_Cupe_4.clicked.connect(closCupe_4)
        ui.pushButton_hetCupe_4.clicked.connect(closCupe_4)

    ui.pushButton_Cupe_4.clicked.connect(Cup_4)
    ui.pushButton_Cupe_3.clicked.connect(Cup_3)
    ui.pushButton_Cupe_1.clicked.connect(Cup_1)
    ui.pushButton_Cupe_2.clicked.connect(Cup_2)


def Vaj():
    global Vajarq
    Vajarq = QtWidgets.QMainWindow()
    ui = Ui_Vajarq()
    ui.setupUi(Vajarq)
    Home.close()
    Vajarq.show()


    bolor_Bar = []
    hamemat = open(r'C:\Users\varda\PycharmProjects\sel\Vajarq.txt', 'r', encoding='utf-8')
    Hamemat = hamemat.readlines()
    hamemat.close()

    Bar_Alkohol = open(r'C:\Users\varda\PycharmProjects\sel\Bis_1_7f.txt', 'r', encoding='utf-8')
    bar_alkohol = Bar_Alkohol.read()
    Bar_Alkohol.close()

    Bar_Voch_Alkohol = open(r'C:\Users\varda\PycharmProjects\sel\Bis_1_8f.txt', 'r', encoding='utf-8')
    bar_voch_alkohol = Bar_Voch_Alkohol.read()
    Bar_Voch_Alkohol.close()

    b1_index_cordinat_valuedr = 0

    for _ in range(bar_alkohol.count('@')):
        b1_name_start_index_valuedr = bar_alkohol.find('@', b1_index_cordinat_valuedr)
        name_and_index_valuedr = bar_alkohol.find('#', b1_index_cordinat_valuedr + 1)
        b1_index_cordinat_valuedr = name_and_index_valuedr
        bolor_Bar_detals = bar_alkohol[b1_name_start_index_valuedr + 1: name_and_index_valuedr]

        bolor_Bar.append(bolor_Bar_detals)

    b1_index_cordinat_valuedr = 0

    for _ in range(bar_voch_alkohol.count('@')):
        b1_name_start_index_valuedr = bar_voch_alkohol.find('@', b1_index_cordinat_valuedr)
        name_and_index_valuedr = bar_voch_alkohol.find('#', b1_index_cordinat_valuedr + 1)
        b1_index_cordinat_valuedr = name_and_index_valuedr
        bolor_Bar_detals = bar_voch_alkohol[b1_name_start_index_valuedr + 1: name_and_index_valuedr]

        bolor_Bar.append(bolor_Bar_detals)


    Bar = []
    Xohanoc = []
    xohanoc_index = 0
    xohanoc_anun_index = -1
    vandax_index = 0
    anun_index = -1
    for i in range(0, len(Hamemat), 2):
        if bolor_Bar.count(Hamemat[i].replace('\n','')) > 0:
            vandax_index += 1

            ui.tableWidget_Bar.setRowCount(vandax_index)
            ui.tableWidget_Bar.setColumnCount(2)
            ui.tableWidget_Bar.setHorizontalHeaderLabels(('apranqanishi anvanum', 'qanak'))
            ui.tableWidget_Bar.setColumnWidth(0, 310)
            ui.tableWidget_Bar.setColumnWidth(1, 110)
            anun_index += 1
            ui.tableWidget_Bar.setItem(anun_index, 0, QTableWidgetItem(str(Hamemat[i].replace('\n',''))))
            ui.tableWidget_Bar.setItem(anun_index, 1, QTableWidgetItem(str(Hamemat[i + 1].replace('\n',''))))

        else:
            xohanoc_index += 1
            ui.tableWidget_Xohanoc.setRowCount(xohanoc_index)
            ui.tableWidget_Xohanoc.setColumnCount(2)
            ui.tableWidget_Xohanoc.setHorizontalHeaderLabels(('apranqanishi anvanum', 'qanak'))
            ui.tableWidget_Xohanoc.setColumnWidth(0, 310)
            ui.tableWidget_Xohanoc.setColumnWidth(1, 110)
            xohanoc_anun_index += 1
            ui.tableWidget_Xohanoc.setItem(xohanoc_anun_index, 0, QTableWidgetItem(str(Hamemat[i].replace('\n', ''))))
            ui.tableWidget_Xohanoc.setItem(xohanoc_anun_index, 1, QTableWidgetItem(str(Hamemat[i + 1].replace('\n', ''))))


    def Search_element():
        name_element = ui.plainTextEdit.toPlainText()
        hamemat_element = open(r'C:\Users\varda\PycharmProjects\sel\Vajarq.txt', 'r', encoding='utf-8')
        Hamemat_element = hamemat_element.readlines()
        hamemat_element.close()


        print(name_element)

        for name in range(len(Hamemat_element)):
            if name_element == Hamemat_element[name].replace('\n',''):
                print('stex em')
                ui.tableWidget_Result.setRowCount(1)
                ui.tableWidget_Result.setColumnCount(2)
                ui.tableWidget_Result.setHorizontalHeaderLabels(('apranqanishi anvanum', 'qanak'))
                ui.tableWidget_Result.setColumnWidth(0, 220)
                ui.tableWidget_Result.setColumnWidth(1, 50)
                ui.tableWidget_Result.setItem(0, 0, QTableWidgetItem(str(Hamemat_element[name].replace('\n',''))))
                ui.tableWidget_Result.setItem(0, 1, QTableWidgetItem(str(Hamemat_element[name + 1].replace('\n', ''))))



    ui.pushButton_2.clicked.connect(Search_element)
    def Vaj_close():
        Vajarq.close()
        Home.show()
    def Vaj_tvyalner():

        Calendar = ui.calendarWidget.selectedDate().toString('yyyy-MM-dd')
    ui.pushButton_Vajarq_het.clicked.connect(Vaj_close)
    ui.calendarWidget.clicked.connect(Vaj_tvyalner)
def Kasa():
    global Casa
    Casa = QtWidgets.QMainWindow()
    ui = Ui_Casa()
    ui.setupUi(Casa)
    Home.close()
    Casa.show()
    def tvyalner():
        tvyalner_arevtur = open(r'C:\Users\varda\PycharmProjects\sel\Baza.txt', 'r', encoding='utf-8')
        Tvyalner_arevtur = tvyalner_arevtur.read()
        tvyalner_arevtur.close()
        print(len(Tvyalner_arevtur))
        distace = 32 - len(Tvyalner_arevtur)
        ui.listWidget_800.addItem(' ' * distace + 'Arevtur')
        ui.listWidget_800.addItem(' ' * distace + str(Tvyalner_arevtur) + 'դր')
        amboxj_caxs = open(r'C:\Users\varda\PycharmProjects\sel\caxser_amboxjovin.txt', 'r', encoding='utf-8')
        Amboxj = amboxj_caxs.read()
        amboxj_caxs.close()

        distace_cax = 17 - len(Amboxj)
        ui.listWidget_901.addItem(' ' * distace_cax + 'Caxs')
        ui.listWidget_901.addItem(' ' * distace_cax + str(Amboxj) + 'դր')

        amboxj_caxs = open(r'C:\Users\varda\PycharmProjects\sel\amboxjakan_ash.txt', 'r', encoding='utf-8')
        Amboxj_Ash = amboxj_caxs.read()
        amboxj_caxs.close()

        distance_ash = 17 - len(Amboxj_Ash)
        ui.listWidget_1001.addItem(' ' * distance_ash + 'Ashxatavardz')
        ui.listWidget_1001.addItem(' ' * distance_ash + str(Amboxj_Ash) + 'դր')



        kasa = int(Tvyalner_arevtur) - int(Amboxj) - int(Amboxj_Ash)
        distance_kasa = 15 - len(str(kasa))


        ui.listWidget_900.addItem(' ' * distance_kasa + str(kasa) + 'դր')

    def ash():
        global Ashxatavardzz
        Ashxatavardzz = QtWidgets.QMainWindow()
        ui = Ui_Casa_ashx()
        ui.setupUi(Ashxatavardzz)
        Casa.close()
        Ashxatavardzz.show()


        def Ash_close():
            cucak_save = open(r'C:\Users\varda\PycharmProjects\sel\Ash_tiv.txt', 'r', encoding='utf-8')
            Cucak_save = cucak_save.read()
            cucak_save.close()

            cucak_nsh_save = open(r'C:\Users\varda\PycharmProjects\sel\Ash_name.txt', 'r', encoding='utf-8')
            Cucak_nsh_save = cucak_nsh_save.read()
            cucak_nsh_save.close()

            cucak_coin_tiv = Cucak_save.count('@')
            cucak_coin_nsh = Cucak_nsh_save.count('!')
            index_nsh = 0
            index_tv = 0
            cucakner = [ui.plainTextEdit_28, ui.plainTextEdit_29, ui.plainTextEdit_33,
                        ui.plainTextEdit_43, ui.plainTextEdit_42, ui.plainTextEdit_41,
                        ui.plainTextEdit_40, ui.plainTextEdit_39, ui.plainTextEdit_38,
                        ui.plainTextEdit_37, ui.plainTextEdit_36, ui.plainTextEdit_35,
                        ui.plainTextEdit_34, ui.plainTextEdit_45, ui.plainTextEdit_44,
                        ui.plainTextEdit_47, ui.plainTextEdit_57, ui.plainTextEdit_60,
                        ui.plainTextEdit_53, ui.plainTextEdit_59, ui.plainTextEdit_46,
                        ui.plainTextEdit_50, ui.plainTextEdit_58, ui.plainTextEdit_52,
                        ui.plainTextEdit_48, ui.plainTextEdit_55, ui.plainTextEdit_56,
                        ui.plainTextEdit_54, ui.plainTextEdit_51, ui.plainTextEdit_49]
            cucak_nshumner = [ui.plainTextEdit, ui.plainTextEdit_25, ui.plainTextEdit_24,
                        ui.plainTextEdit_23, ui.plainTextEdit_22, ui.plainTextEdit_21,
                        ui.plainTextEdit_20, ui.plainTextEdit_19, ui.plainTextEdit_18,
                        ui.plainTextEdit_17, ui.plainTextEdit_16, ui.plainTextEdit_15,
                        ui.plainTextEdit_14, ui.plainTextEdit_13, ui.plainTextEdit_12,
                        ui.plainTextEdit_11, ui.plainTextEdit_2, ui.plainTextEdit_6,
                        ui.plainTextEdit_4, ui.plainTextEdit_3, ui.plainTextEdit_10,
                        ui.plainTextEdit_9, ui.plainTextEdit_8, ui.plainTextEdit_5,
                        ui.plainTextEdit_7, ui.plainTextEdit_32, ui.plainTextEdit_31,
                        ui.plainTextEdit_26, ui.plainTextEdit_30, ui.plainTextEdit_27]

            for pl in range(0, cucak_coin_tiv):
                cuvcak_save_start = Cucak_save.find('@', index_tv)
                cuvcak_save_start += 1
                cuvcak_save_end = Cucak_save.find('#', cuvcak_save_start)
                index_tv = cuvcak_save_end
                itog_tv = Cucak_save[cuvcak_save_start:cuvcak_save_end]
                print(itog_tv)
                cucakner[pl].setPlainText(str(itog_tv))

            for to in range(0, cucak_coin_nsh):
                cuvcak_save_startr = Cucak_nsh_save.find('!', index_nsh)
                cuvcak_save_startr += 1
                cuvcak_save_endr = Cucak_nsh_save.find('%', cuvcak_save_startr)
                index_nsh = cuvcak_save_endr
                itog_tvr = Cucak_nsh_save[cuvcak_save_startr:cuvcak_save_endr]
                cucak_nshumner[to].setPlainText(str(itog_tvr))

        Ash_close()

        def point_ash():

            caxser_bolor_tvyalner = []
            bolor_t_toxer = 0
            cucakner = [ui.plainTextEdit_28, ui.plainTextEdit_29, ui.plainTextEdit_33,
                        ui.plainTextEdit_43, ui.plainTextEdit_42, ui.plainTextEdit_41,
                        ui.plainTextEdit_40, ui.plainTextEdit_39, ui.plainTextEdit_38,
                        ui.plainTextEdit_37, ui.plainTextEdit_36, ui.plainTextEdit_35,
                        ui.plainTextEdit_34, ui.plainTextEdit_45, ui.plainTextEdit_44,
                        ui.plainTextEdit_47, ui.plainTextEdit_57, ui.plainTextEdit_60,
                        ui.plainTextEdit_53, ui.plainTextEdit_59, ui.plainTextEdit_46,
                        ui.plainTextEdit_50, ui.plainTextEdit_58, ui.plainTextEdit_52,
                        ui.plainTextEdit_48, ui.plainTextEdit_55, ui.plainTextEdit_56,
                        ui.plainTextEdit_54, ui.plainTextEdit_51, ui.plainTextEdit_49]

            for i in range(0, 30):
                bolor_toxer = cucakner[i].toPlainText()
                if type(bolor_toxer) == str:
                    try:
                        bolor_toxer = int(bolor_toxer)

                        print('bolor_toxer_r', bolor_toxer)
                    except ValueError or TypeError:
                        bolor_toxer = 0

                    bolor_t_toxer += bolor_toxer
                    print('bolor_t_toxer', bolor_t_toxer)

                caxser_bolor_tvyalner.append('@' + str(bolor_toxer) + '#')

            TVER = open(r'C:\Users\varda\PycharmProjects\sel\Ash_tiv.txt', 'w', encoding='utf-8')
            TVER_POINT = TVER.write(str(caxser_bolor_tvyalner))
            TVER.close()
            amboxjakan = open(r'C:\Users\varda\PycharmProjects\sel\amboxjakan_ash.txt', 'w', encoding='utf-8')
            Amboxj = amboxjakan.write(str(bolor_t_toxer))
            amboxjakan.close()
            cucak_nshumner = [ui.plainTextEdit, ui.plainTextEdit_25, ui.plainTextEdit_24,
                              ui.plainTextEdit_23, ui.plainTextEdit_22, ui.plainTextEdit_21,
                              ui.plainTextEdit_20, ui.plainTextEdit_19, ui.plainTextEdit_18,
                              ui.plainTextEdit_17, ui.plainTextEdit_16, ui.plainTextEdit_15,
                              ui.plainTextEdit_14, ui.plainTextEdit_13, ui.plainTextEdit_12,
                              ui.plainTextEdit_11, ui.plainTextEdit_2, ui.plainTextEdit_6,
                              ui.plainTextEdit_4, ui.plainTextEdit_3, ui.plainTextEdit_10,
                              ui.plainTextEdit_9, ui.plainTextEdit_8, ui.plainTextEdit_5,
                              ui.plainTextEdit_7, ui.plainTextEdit_32, ui.plainTextEdit_31,
                              ui.plainTextEdit_26, ui.plainTextEdit_30, ui.plainTextEdit_27]
            nshumner = []
            for l in range(0, 30):
                nshumner_her = cucak_nshumner[l].toPlainText()

                # if len(nshumner_her) == 0:
                #     nshumner_her = 'None'

                nshumner.append('!' + nshumner_her + '%')

            TVER_NSHUMNER = open(r'C:\Users\varda\PycharmProjects\sel\Ash_name.txt', 'w', encoding='utf-8')
            Tver_nshumner = TVER_NSHUMNER.write(str(nshumner))
            TVER_NSHUMNER.close()

            Ashxatavardzz.close()
            Home.show()

        ui.pushButton_2001.clicked.connect(point_ash)



    tvyalner()


    def Caxs_kasa():
        global Cucak
        Cucak = QtWidgets.QMainWindow()
        ui = Ui_Caxser()
        ui.setupUi(Cucak)
        Casa.close()
        Cucak.show()

        def clos_cucak():
            Cucak.close()
            Home.show()

        def save_cucak():
            cucak_save = open(r'C:\Users\varda\PycharmProjects\sel\caxser.txt', 'r', encoding='utf-8')
            Cucak_save = cucak_save.read()
            cucak_save.close()

            cucak_nsh_save = open(r'C:\Users\varda\PycharmProjects\sel\Tver_Nshumner.txt', 'r', encoding='utf-8')
            Cucak_nsh_save = cucak_nsh_save.read()
            cucak_nsh_save.close()

            cucak_coin_tiv = Cucak_save.count('@')
            cucak_coin_nsh = Cucak_nsh_save.count('!')
            index_nsh = 0
            index_tv = 0
            cucakner = [ui.plainTextEdit, ui.plainTextEdit_3, ui.plainTextEdit_5,
                        ui.plainTextEdit_17, ui.plainTextEdit_15, ui.plainTextEdit_13,
                        ui.plainTextEdit_11, ui.plainTextEdit_9, ui.plainTextEdit_7]
            cucak_nshumner = [ui.plainTextEdit_2, ui.plainTextEdit_4, ui.plainTextEdit_6,
                              ui.plainTextEdit_18, ui.plainTextEdit_16, ui.plainTextEdit_14,
                              ui.plainTextEdit_12, ui.plainTextEdit_10, ui.plainTextEdit_8]


            for pl in range(0,cucak_coin_tiv):


                cuvcak_save_start = Cucak_save.find('@',index_tv)
                cuvcak_save_start += 1
                cuvcak_save_end = Cucak_save.find('#',cuvcak_save_start)
                index_tv = cuvcak_save_end
                itog_tv = Cucak_save[cuvcak_save_start:cuvcak_save_end]
                print(itog_tv)
                cucakner[pl].setPlainText(str(itog_tv))

            for to in range(0, cucak_coin_nsh):
                cuvcak_save_startr = Cucak_nsh_save.find('!', index_nsh)
                cuvcak_save_startr += 1
                cuvcak_save_endr = Cucak_nsh_save.find('%', cuvcak_save_startr)
                index_nsh = cuvcak_save_endr
                itog_tvr = Cucak_nsh_save[cuvcak_save_startr:cuvcak_save_endr]
                cucak_nshumner[to].setPlainText(str(itog_tvr))


        save_cucak()

        def point():

            caxser_bolor_tvyalner = []
            bolor_t_toxer = 0
            cucakner = [ui.plainTextEdit,ui.plainTextEdit_3,ui.plainTextEdit_5,
                        ui.plainTextEdit_17,ui.plainTextEdit_15,ui.plainTextEdit_13,
                        ui.plainTextEdit_11,ui.plainTextEdit_9,ui.plainTextEdit_7]

            for i in range(0,9):
                bolor_toxer = cucakner[i].toPlainText()
                if type(bolor_toxer) == str:
                    try:
                        bolor_toxer = int(bolor_toxer)

                        print('bolor_toxer_r', bolor_toxer)
                    except ValueError or TypeError:
                        bolor_toxer = 0

                    bolor_t_toxer += bolor_toxer
                    print('bolor_t_toxer',bolor_t_toxer)






                caxser_bolor_tvyalner.append('@' + str(bolor_toxer) + '#')


            TVER = open(r'C:\Users\varda\PycharmProjects\sel\caxser.txt', 'w', encoding='utf-8')
            TVER_POINT = TVER.write(str(caxser_bolor_tvyalner))
            TVER.close()
            amboxjakan = open(r'C:\Users\varda\PycharmProjects\sel\caxser_amboxjovin.txt', 'w', encoding='utf-8')
            Amboxj = amboxjakan.write(str(bolor_t_toxer))
            amboxjakan.close()
            cucak_nshumner = [ui.plainTextEdit_2,ui.plainTextEdit_4,ui.plainTextEdit_6,
                        ui.plainTextEdit_18,ui.plainTextEdit_16,ui.plainTextEdit_14,
                        ui.plainTextEdit_12,ui.plainTextEdit_10,ui.plainTextEdit_8]
            nshumner = []
            for l in range(0, 9):

                nshumner_her = cucak_nshumner[l].toPlainText()


                # if len(nshumner_her) == 0:
                #     nshumner_her = 'None'

                nshumner.append('!' + nshumner_her + '%')

            TVER_NSHUMNER = open(r'C:\Users\varda\PycharmProjects\sel\Tver_Nshumner.txt', 'w', encoding='utf-8')
            Tver_nshumner = TVER_NSHUMNER.write(str(nshumner))
            TVER_NSHUMNER.close()


        # Caxseri cucakna
        ui.pushButton_2.clicked.connect(point)
        ui.het.clicked.connect(clos_cucak)


    # Kasayin verabervox
    ui.pushButton_2.clicked.connect(Caxs_kasa)

    ui.pushButton_3.clicked.connect(ash)

    def Kasa_return():

        Casa.close()
        Home.show()
    ui.pushButton_4.clicked.connect(Kasa_return)

ui.Jnjum.clicked.connect(Jnjumner_fan)
ui.Cupe.clicked.connect(Cup)
ui.Bistro_2.clicked.connect(Bistro_2)
ui.Vajarq.clicked.connect(Vaj)
ui.Kassa.clicked.connect(Kasa)
ui.Bistro_1.clicked.connect(openOtherWindow)

sys.exit(app.exec_())