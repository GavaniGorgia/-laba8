import sys
import psycopg2
from PyQt5.QtWidgets import ( QApplication, QWidget, QTabWidget, QAbstractScrollArea,
                              QVBoxLayout, QHBoxLayout, QTableWidget, QGroupBox,
                              QTableWidgetItem, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt

class Window (QWidget):
    def __init__(self):
        super(Window,self).__init__()

        self.setWindowTitle("Shedule")

        self._connect_to_db()

        self.tabs = QTabWidget(self)
        self.vbox = QVBoxLayout(self)

        self.vbox.addWidget(self.tabs)

        self._create_sum()
        self._create_shedule0_tab()
        self._create_subject_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="last3",
                                     user="postgres",
                                     password="lolo2002",
                                     host="localhost",
                                     port="5432")
        self.cursor = self.conn.cursor()

    def _create_sum(self):
        self.sum_tab = QWidget()
        self.sum_tab_tabs = QTabWidget(self)
        self.sum_tab_vbox = QVBoxLayout(self)

        self.any_tab = QWidget()

        self.sum_tab.setLayout(self.sum_tab_vbox)
        self.sum_tab_vbox.addWidget(self.sum_tab_tabs)
        self.tabs.addTab(self.sum_tab,"any")

        self._create_shedule_tab()
        self._create_shedule1_tab()
        self._create_shedule2_tab()
        self._create_shedule3_tab()
        self._create_shedule4_tab()
        self._create_shedule5_tab()


    def _create_shedule0_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "teacher")

        self.monday_gbox = QGroupBox("teacher")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_teacher_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_teacher_table)
        self.shedule_tab.setLayout(self.svbox)

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.sum_tab_tabs.addTab(self.shedule_tab, "Monday")
        self.monday_gbox = QGroupBox("Monday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()


        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)


        self.shbox1.addWidget(self.monday_gbox)

        self._create_monday_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_monday_table)
        self.shedule_tab.setLayout(self.svbox)

    def _create_shedule2_tab(self):
        self.shedule_tab = QWidget()
        self.sum_tab_tabs.addTab(self.shedule_tab, "Wednesday")

        self.monday_gbox = QGroupBox("Wednesday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_Wednesday_table()


        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_Wednesday_table)
        self.shedule_tab.setLayout(self.svbox)

    def _create_shedule1_tab(self):
        self.shedule_tab = QWidget()
        self.sum_tab_tabs.addTab(self.shedule_tab, "Thuseday")

        self.monday_gbox = QGroupBox("Thuseday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_thusday_table()



        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_thusday_table)

        self.shedule_tab.setLayout(self.svbox)

    def _create_shedule3_tab(self):
        self.shedule_tab = QWidget()
        self.sum_tab_tabs.addTab(self.shedule_tab, "Thursday")

        self.monday_gbox = QGroupBox("Thursday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_Thursday_table()


        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_Thursday_table)
        self.shedule_tab.setLayout(self.svbox)

    def _create_shedule4_tab(self):
        self.shedule_tab = QWidget()
        self.sum_tab_tabs.addTab(self.shedule_tab, "Friday")

        self.monday_gbox = QGroupBox("Friday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_Friday_table()



        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_Friday_table)
        self.shedule_tab.setLayout(self.svbox)

    def _create_shedule5_tab(self):
        self.shedule_tab = QWidget()
        self.sum_tab_tabs.addTab(self.shedule_tab, "Saturday")

        self.monday_gbox = QGroupBox("Saturday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_Saturday_table()


        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_Saturday_table)
        self.shedule_tab.setLayout(self.svbox)

    def _create_subject_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Subject")


        self.monday_gbox = QGroupBox("Subject")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_Subject_table()




        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_Subject_table)
        self.shedule_tab.setLayout(self.svbox)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(5)
        self.teacher_table.setHorizontalHeaderLabels(["id","full_name","subject"])

        self._update_teacher_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.teacher_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_monday_table (self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(7)
        self.monday_table.setHorizontalHeaderLabels(["id","day","Subject","Room","Time","Join","Delete"])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_thusday_table (self):
        self.thusday_table = QTableWidget()
        self.thusday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thusday_table.setColumnCount(7)
        self.thusday_table.setHorizontalHeaderLabels(["id","day","Subject","Room","Time","Join","Delete"])

        #self.monday_table.setEditTriggers(QTableWidget.NoEditTriggers)


        self._update_thusday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thusday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_Wednesday_table (self):
        self.Wednesday_table = QTableWidget()
        self.Wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Wednesday_table.setColumnCount(7)
        self.Wednesday_table.setHorizontalHeaderLabels(["id","day","Subject","Room","Time","Join","Delete"])

        self._update_Wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Wednesday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_Thursday_table(self):
        self.Thursday_table = QTableWidget()
        self.Thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Thursday_table.setColumnCount(7)
        self.Thursday_table.setHorizontalHeaderLabels(["id","day","Subject","Room","Time","Join","Delete"])

        self._update_Thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Thursday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_Friday_table(self):
        self.Friday_table = QTableWidget()
        self.Friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Friday_table.setColumnCount(7)
        self.Friday_table.setHorizontalHeaderLabels(["id","day","Subject","Room","Time","Join","Delete"])

        self._update_Friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Friday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_Saturday_table(self):
        self.Saturday_table = QTableWidget()
        self.Saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Saturday_table.setColumnCount(7)
        self.Saturday_table.setHorizontalHeaderLabels(["id","day","Subject","Room","Time","Join","Delete"])

        self._update_Saturday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Saturday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_Subject_table(self):
        self.Subject_table = QTableWidget()
        self.Subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Subject_table.setColumnCount(4)
        self.Subject_table.setHorizontalHeaderLabels(["id", "name"])

        self._update_Subject_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Subject_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _update_teacher_table(self):
        self.cursor.execute("SELECT * FROM teacher")

        records = list(self.cursor.fetchall())

        self.teacher_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            self.teacher_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.teacher_table.item(i,0).setFlags(self.teacher_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.teacher_table.setItem(i, 1, QTableWidgetItem( str(r[1])))
            self.teacher_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            self.teacher_table.setCellWidget(i, 3, joinButton)
            self.teacher_table.setCellWidget(i, 4, DeleteButton)
            DeleteButton.clicked.connect(lambda ch, num=i: self._delete_teacher_from_table(num))
            joinButton.clicked.connect(lambda ch, num=i: self._change_teacher_from_table(num))
        self.teacher_table.setRowCount(len(records) + 1)
        addButton = QPushButton("add")
        self.teacher_table.setCellWidget(len(records), 3, addButton)
        addButton.clicked.connect(lambda ch, num=len(records): self._add_teacher_for_table(num))
        self.teacher_table.resizeRowsToContents()

    def _update_Friday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Пт'")

        records = list(self.cursor.fetchall())
       

        self.Friday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            self.Friday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.Friday_table.item(i, 0).setFlags(self.Friday_table.item(i, 0).flags() ^ Qt.ItemIsEditable)
            self.Friday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.Friday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.Friday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.Friday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            self.Friday_table.setCellWidget(i, 5, joinButton)
            self.Friday_table.setCellWidget(i, 6, DeleteButton)

            day = str('Пт')
            DeleteButton.clicked.connect(lambda ch, num=i: self._Delete_day_from_table(num, day))
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table (num,day))
        self.Friday_table.setRowCount(len(records)+1)
        addButton = QPushButton("add")
        self.Friday_table.setCellWidget(len(records), 5, addButton)
        addButton.clicked.connect(lambda ch, num=len(records): self._add_day_for_table(num,day))
        self.Friday_table.resizeRowsToContents()

    def _update_Saturday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Сб'")

        records = list(self.cursor.fetchall())
      

        self.Saturday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            self.Saturday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.Saturday_table.item(i, 0).setFlags(self.Saturday_table.item(i, 0).flags() ^ Qt.ItemIsEditable)
            self.Saturday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.Saturday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.Saturday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.Saturday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            self.Saturday_table.setCellWidget(i, 5, joinButton)
            self.Saturday_table.setCellWidget(i, 6, DeleteButton)

            day = str('Сб')
            DeleteButton.clicked.connect(lambda ch, num=i: self._Delete_day_from_table(num, day))
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table (num,day))
        self.Saturday_table.setRowCount(len(records) + 1)
        addButton = QPushButton("add")
        self.Saturday_table.setCellWidget(len(records), 5, addButton)
        addButton.clicked.connect(lambda ch, num=len(records): self._add_day_for_table(num,day))
        self.Saturday_table.resizeRowsToContents()

    def _update_Thursday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Чт'")

        records = list(self.cursor.fetchall())
      


        self.Thursday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            self.Thursday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.Thursday_table.item(i, 0).setFlags(self.Thursday_table.item(i, 0).flags() ^ Qt.ItemIsEditable)
            self.Thursday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.Thursday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.Thursday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.Thursday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            self.Thursday_table.setCellWidget(i, 5, joinButton)
            self.Thursday_table.setCellWidget(i, 6, DeleteButton)

            day = str('Чт')
            DeleteButton.clicked.connect(lambda ch, num=i: self._Delete_day_from_table(num, day))
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table (num,day))
        self.Thursday_table.setRowCount(len(records) + 1)
        addButton = QPushButton("add")
        self.Thursday_table.setCellWidget(len(records), 5, addButton)
        addButton.clicked.connect(lambda ch, num=len(records): self._add_day_for_table(num,day))
        self.Thursday_table.resizeRowsToContents()

    def _update_Wednesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Ср'")

        records = list(self.cursor.fetchall())

        self.Wednesday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            self.Wednesday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.Wednesday_table.item(i, 0).setFlags(self.Wednesday_table.item(i, 0).flags() ^ Qt.ItemIsEditable)
            self.Wednesday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.Wednesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.Wednesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.Wednesday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            self.Wednesday_table.setCellWidget(i, 5, joinButton)
            self.Wednesday_table.setCellWidget(i, 6, DeleteButton)

            day = str('Ср')
            DeleteButton.clicked.connect(lambda ch, num=i: self._Delete_day_from_table(num, day))
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table (num,day))
        self.Wednesday_table.setRowCount(len(records) + 1)
        addButton = QPushButton("add")
        self.Wednesday_table.setCellWidget(len(records), 5, addButton)
        addButton.clicked.connect(lambda ch, num=len(records): self._add_day_for_table(num,day))
        self.Wednesday_table.resizeRowsToContents()

    def _update_thusday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Вт'")

        records = list(self.cursor.fetchall())

        self.thusday_table.setRowCount(len(records))

        for i , r in enumerate(records):
            r = list(r)
            self.thusday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.thusday_table.item(i, 0).setFlags(self.thusday_table.item(i, 0).flags() ^ Qt.ItemIsEditable)
            self.thusday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.thusday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.thusday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.thusday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            self.thusday_table.setCellWidget(i, 5, joinButton)
            self.thusday_table.setCellWidget(i, 6, DeleteButton)

            day = str('Вт')
            DeleteButton.clicked.connect(lambda ch, num=i: self._Delete_day_from_table(num, day))
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table (num,day))
        self.thusday_table.setRowCount(len(records) + 1)
        addButton = QPushButton("add")
        self.thusday_table.setCellWidget(len(records), 5, addButton)
        addButton.clicked.connect(lambda ch, num=len(records): self._add_day_for_table(num,day))

        self.thusday_table.resizeRowsToContents()

    def _update_monday_table(self):
        while self.monday_table.rowCount()>0:
            self.monday_table.removeRow(0)

        self.cursor.execute("SELECT * FROM timetable WHERE day='Пн'")

        records = list(self.cursor.fetchall())

        

        self.monday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            self.monday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.monday_table.item(i, 0).setFlags(self.monday_table.item(i, 0).flags() ^ Qt.ItemIsEditable)
            self.monday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.monday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            self.monday_table.setCellWidget(i, 5, joinButton)
            self.monday_table.setCellWidget(i, 6, DeleteButton)


            day =str('Пн')
            DeleteButton.clicked.connect(lambda ch, num=i: self._Delete_day_from_table(num, day))
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table (num,day))
        self.monday_table.setRowCount(len(records) + 1)
        addButton = QPushButton("add")
        self.monday_table.setCellWidget(len(records), 5, addButton)
        addButton.clicked.connect(lambda ch, num=len(records): self._add_day_for_table(num,day))

        self.monday_table.resizeRowsToContents()

    def _update_Subject_table(self):
        self.cursor.execute("SELECT * FROM subject")

        records = list(self.cursor.fetchall())

        self.Subject_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            self.Subject_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.Subject_table.item(i, 0).setFlags(self.Subject_table.item(i, 0).flags() ^ Qt.ItemIsEditable)
            self.Subject_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            joinButton = QPushButton("Join")
            DeleteButton = QPushButton("Delete")
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records12 = self.cursor.fetchall()
            result12 = ''
            for arr in records12:
                for word in arr:
                    result12 += str(word)
                    result12 += ','
            g = result12.split(',')

            self.cursor.execute("SELECT subject FROM timetable")
            self.conn.commit()
            records1 = self.cursor.fetchall()
            result1 = ' '
            for arr in records1:
                for word in arr:
                    result1 += str(word)
                    result1 += ','
            w = result1.split(',')

            self.cursor.execute("SELECT subject FROM teacher")
            self.conn.commit()
            records2 = self.cursor.fetchall()
            result2 = ' '
            for arr in records2:
                for word in arr:
                    result2 += str(word)
                    result2 += ','
            q = result2.split(',')

            intersection = []
            intersection1 = []
            
            for u in w:
                if u in g:
                    intersection.append(u)
            for u in q:
                if u in g:
                    intersection1.append(u)

            if r[1] in intersection or r[1] in intersection1:
                self.Subject_table.item(i, 1).setFlags(self.Subject_table.item(i, 1).flags() ^ Qt.ItemIsEditable)

            self.Subject_table.setCellWidget(i, 2, joinButton)
            self.Subject_table.setCellWidget(i, 3, DeleteButton)
            DeleteButton.clicked.connect(lambda ch, num=i: self._delete_subject_from_table(num))
            joinButton.clicked.connect(lambda ch, num=i: self._change_subject_from_table(num,intersection,intersection1))

        self.Subject_table.setRowCount(len(records) + 1)
        addButton = QPushButton("add")
        self.Subject_table.setCellWidget(len(records), 2, addButton)
        addButton.clicked.connect(lambda ch, num=len(records): self._add_subject_for_table(num))

        self.Subject_table.resizeRowsToContents()

    def _change_subject_from_table(self, rowNumb, mas1,mas2):
        row = list()
        for i in range(self.Subject_table.columnCount()):
            try:
                row.append(self.Subject_table.item(rowNumb, i).text())

            except:
                row.append(None)

        if row[1] not in mas1:
            self.cursor.execute(
                f"UPDATE subject SET name = '{row[1]}' WHERE id = '{row[0]}' ")
            self.conn.commit()
            self._update_Subject_table()
        else:
            QMessageBox.about(self, "Error", "Предмет нельзя изменить пока он находится в других таблицах")



    def _change_day_from_table (self, rowNumb,day):

        row = list()
        if day =='Пн':
            for i in range(self.monday_table.columnCount()):
                try:
                    row.append(self.monday_table.item(rowNumb, i).text())
                    
                except:
                    row.append(None)
            times = ['9:30', '11:20', '13:10', '15:25', '17:00', '9:30:00', '11:20:00', '13:10:00', '15:25:00',
                     '17:00:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''

            
            if row[4] in times:
                if row[1] != 'Пн':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:
                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None or row[3] == '':
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"UPDATE timetable SET day = '{row[1]}',subject ='{row[2]}', room='{row[3]}',time='{row[4]}' WHERE id = '{row[0]}' ")
                            self.conn.commit()
                            self._update_monday_table()
                            self._update_Subject_table()
                            
            else:
                QMessageBox.about(self, "Error", "Неверно введено время")

        if day == 'Вт':
            for i in range(self.thusday_table.columnCount()):
                try:
                    row.append(self.thusday_table.item(rowNumb, i).text())
                    
                except:
                    row.append(None)
            times = ['9:30', '11:20', '13:10', '15:25', '17:00', '9:30:00', '11:20:00', '13:10:00', '15:25:00',
                     '17:00:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''

            
            if row[4] in times:
                if row[1] != 'Вт':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:
                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None or row[3] == '':
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"UPDATE timetable SET day = '{row[1]}',subject ='{row[2]}', room='{row[3]}',time='{row[4]}' WHERE id = '{row[0]}' ")
                            self.conn.commit()
                            self._update_thusday_table()
                            self._update_Subject_table()
                            
            else:
                QMessageBox.about(self, "Error", "Неверно введено время")

        if day == 'Ср':
            for i in range(self.Wednesday_table.columnCount()):
                try:
                    row.append(self.Wednesday_table.item(rowNumb, i).text())
                    
                except:
                    row.append(None)
            times = ['9:30', '11:20', '13:10', '15:25', '17:00', '9:30:00', '11:20:00', '13:10:00', '15:25:00',
                     '17:00:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''


            if row[4] in times:
                if row[1] != 'Ср':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:
                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None or row[3] == '':
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"UPDATE timetable SET day = '{row[1]}',subject ='{row[2]}', room='{row[3]}',time='{row[4]}' WHERE id = '{row[0]}' ")
                            self.conn.commit()
                            self._update_Wednesday_table()
                            self._update_Subject_table()
                            
            else:
                QMessageBox.about(self, "Error", "Неверно введено время")

        if day == 'Чт':
            for i in range(self.Thursday_table.columnCount()):
                try:
                    row.append(self.Thursday_table.item(rowNumb, i).text())
                   
                except:
                    row.append(None)
            times = ['9:30', '11:20', '13:10', '15:25', '17:00', '9:30:00', '11:20:00', '13:10:00', '15:25:00',
                     '17:00:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''


            if row[4] in times:
                if row[1] != 'Чт':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:
                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None or row[3] == '':
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"UPDATE timetable SET day = '{row[1]}',subject ='{row[2]}', room='{row[3]}',time='{row[4]}' WHERE id = '{row[0]}' ")
                            self.conn.commit()
                            self._update_Thursday_table()
                            self._update_Subject_table()
                           
            else:
                QMessageBox.about(self, "Error", "Неверно введено время")

        if day == 'Пт':
            for i in range(self.Friday_table.columnCount()):
                try:
                    row.append(self.Friday_table.item(rowNumb, i).text())
                    
                except:
                    row.append(None)

            times = ['9:30', '11:20', '13:10', '15:25', '17:00', '9:30:00', '11:20:00', '13:10:00', '15:25:00',
                     '17:00:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''

            if row[4] in times:
                if row[1] != 'Пт':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:
                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None or row[3] == '':
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"UPDATE timetable SET day = '{row[1]}',subject ='{row[2]}', room='{row[3]}',time='{row[4]}' WHERE id = '{row[0]}' ")
                            self.conn.commit()
                            self._update_Friday_table()
                            self._update_Subject_table()
                            
            else:
                QMessageBox.about(self, "Error", "Неверно введено время")

        if day == 'Сб':
            for i in range(self.Saturday_table.columnCount()):
                try:
                    row.append(self.Saturday_table.item(rowNumb, i).text())
                   
                except:
                    row.append(None)

            times = ['9:30', '11:20', '13:10', '15:25', '17:00','9:30:00', '11:20:00', '13:10:00', '15:25:00', '17:00:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''

            
            if row[4] in times:
                if row[1] != 'Сб':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:
                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None or row[3] == '':
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"UPDATE timetable SET day = '{row[1]}',subject ='{row[2]}', room='{row[3]}',time='{row[4]}' WHERE id = '{row[0]}' ")
                            self.conn.commit()
                            self._update_Saturday_table()
                            self._update_Subject_table()
                            
            else:
                QMessageBox.about(self, "Error", "Неверно введено время")



    def _change_teacher_from_table(self, rowNumb):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNumb, i).text())
                
            except:
                row.append(None)
        self.cursor.execute("SELECT subject FROM teacher")
        self.conn.commit()
        records = self.cursor.fetchall()
        result = ''
        for arr in records:
            for word in arr:
                result += str(word)
                result += ''
        # result=array(result)
        if row[2] in result:
            self.cursor.execute(
                f"UPDATE teacher SET full_name = '{row[1]}', subject = '{row[2]}' WHERE id = '{row[0]}' ")
            self.conn.commit()
            self._update_teacher_table()
            self._update_Subject_table()
          
        else:
            QMessageBox.about(self, "Error", "Необходимо ввести предмет который существует в таб. subject")


    def _add_day_for_table (self,rowNumb, day):
        if day == 'Пн':
            row = list()
            for i in range(self.monday_table.columnCount()):
                try:
                    row.append(self.monday_table.item(rowNumb, i).text())
                except:
                    row.append(None)

            times =['9:30','11:20','13:10','15:25','17:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result =' '
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''
            #

         


            if row[4] in times:
                if row[1]!='Пн':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:

                    if row[2]== None or row[2] not in result or row[2]==' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3]==None:
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"INSERT INTO timetable (day,subject,room,time) VALUES  ('{row[1]}', '{row[2]}','{row[3]}','{row[4]}')")
                            self.conn.commit()
                          
                            self._update_monday_table()
                            self._update_Subject_table()
            else:
                QMessageBox.about(self, "Error", "Неверно введено время или не заполнены данные")




        if day == 'Вт':
            row = list()
            for i in range(self.thusday_table.columnCount()):
                try:
                    row.append(self.thusday_table.item(rowNumb, i).text())
                   
                except:
                    row.append(None)

            times = ['9:30', '11:20', '13:10', '15:25', '17:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''
            # result=array(result)

        

            if row[4] in times:
                if row[1] != 'Вт':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:

                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None:
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"INSERT INTO timetable (day,subject,room,time) VALUES  ('{row[1]}', '{row[2]}','{row[3]}','{row[4]}')")
                            self.conn.commit()
                          
                            self._update_thusday_table()
                            self._update_Subject_table()
            else:
                QMessageBox.about(self, "Error", "Неверно введено время или не заполнены данные")


        if day == 'Ср':
            row = list()
            for i in range(self.Wednesday_table.columnCount()):
                try:
                    row.append(self.Wednesday_table.item(rowNumb, i).text())
                   
                except:
                    row.append(None)
            times = ['9:30', '11:20', '13:10', '15:25', '17:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''
            # result=array(result)


            if row[4] in times:
                if row[1] != 'Ср':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:

                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None:
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"INSERT INTO timetable (day,subject,room,time) VALUES  ('{row[1]}', '{row[2]}','{row[3]}','{row[4]}')")
                            self.conn.commit()
                          
                            self._update_Wednesday_table()
                            self._update_Subject_table()
            else:
                QMessageBox.about(self, "Error", "Неверно введено время или не заполнены данные")

        if day == 'Чт':
            row = list()
            for i in range(self.Thursday_table.columnCount()):
                try:
                    row.append(self.Thursday_table.item(rowNumb, i).text())
                  
                except:
                    row.append(None)
            times = ['9:30', '11:20', '13:10', '15:25', '17:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''
            # result=array(result)

        

            if row[4] in times:
                if row[1] != 'Чт':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:

                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None:
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"INSERT INTO timetable (day,subject,room,time) VALUES  ('{row[1]}', '{row[2]}','{row[3]}','{row[4]}')")
                            self.conn.commit()
                         
                            self._update_Thursday_table()
                            self._update_Subject_table()
            else:
                QMessageBox.about(self, "Error", "Неверно введено время или не заполнены данные")

        if day == 'Пт':
            row = list()
            for i in range(self.Friday_table.columnCount()):
                try:
                    row.append(self.Friday_table.item(rowNumb, i).text())
                   
                except:
                    row.append(None)
            times = ['9:30', '11:20', '13:10', '15:25', '17:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''
            

          

            if row[4] in times:
                if row[1] != 'Пт':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:

                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None:
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"INSERT INTO timetable (day,subject,room,time) VALUES  ('{row[1]}', '{row[2]}','{row[3]}','{row[4]}')")
                            self.conn.commit()
                          
                            self._update_Friday_table()
                            self._update_Subject_table()
            else:
                QMessageBox.about(self, "Error", "Неверно введено время или не заполнены данные")

        if day == 'Сб':
            row = list()
            for i in range(self.Saturday_table.columnCount()):
                try:
                    row.append(self.Saturday_table.item(rowNumb, i).text())
                   
                except:
                    row.append(None)
            times = ['9:30', '11:20', '13:10', '15:25', '17:00']
            self.cursor.execute("SELECT * FROM subject")
            self.conn.commit()
            records = self.cursor.fetchall()
            result = ''
            for arr in records:
                for word in arr:
                    result += str(word)
                    result += ''
            # result=array(result)

            

            if row[4] in times:
                if row[1] != 'Сб':
                    QMessageBox.about(self, "Error", "Неверно введен или не заполнен день")
                else:

                    if row[2] == None or row[2] not in result or row[2] == ' ':
                        QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
                    else:
                        if row[3] == None:
                            QMessageBox.about(self, "Error", "Требуется заполнить room")
                        else:
                            self.cursor.execute(
                                f"INSERT INTO timetable (day,subject,room,time) VALUES  ('{row[1]}', '{row[2]}','{row[3]}','{row[4]}')")
                            self.conn.commit()
                           
                            self._update_Saturday_table()
                            self._update_Subject_table()
            else:
                QMessageBox.about(self, "Error", "Неверно введено время или не заполнены данные")


    def _add_subject_for_table(self, rowNumb):
        row = list()
        for i in range(self.Subject_table.columnCount()):
            try:
                row.append(self.Subject_table.item(rowNumb, i).text())
              
            except:
                row.append(None)

        if row[1] == None:
            QMessageBox.about(self, "Error", "Требуется заполнить subject")
        else:
            self.cursor.execute(
                f"INSERT INTO subject (name) VALUES  ('{row[1]}')")
            self.conn.commit()
          
            self._update_Subject_table()


    def _add_teacher_for_table(self, rowNumb):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNumb, i).text())
             
            except:
                row.append(None)

        self.cursor.execute("SELECT * FROM subject")
        self.conn.commit()
        records = self.cursor.fetchall()
        result = ''
        for arr in records:
            for word in arr:
                result += str(word)
                result += ''
       

        if row[2] == None or row[2] not in result or row[2] == ' ':
            QMessageBox.about(self, "Error", "Данный предмет отсутвует в таблице subject")
        else:
            if row[1] == None:
                QMessageBox.about(self, "Error", "Требуется заполнить full_name")
            else:
                self.cursor.execute(
                    f"INSERT INTO teacher (full_name,subject) VALUES  ('{row[1]}', '{row[2]}')")
                self.conn.commit()
             
                self._update_teacher_table()
                self._update_Subject_table()




    def _delete_subject_from_table(self, rowNumb):
        row = list()
        for i in range(self.Subject_table.columnCount()):
            try:
                row.append(self.Subject_table.item(rowNumb, i).text())
              
            except:
                row.append(None)

        self.cursor.execute("SELECT subject FROM timetable")
        self.conn.commit()
        records = self.cursor.fetchall()
        result = ''
        for arr in records:
            for word in arr:
                result += str(word)
                result += ''
     

        self.cursor.execute("SELECT subject FROM teacher")
        self.conn.commit()
        records1 = self.cursor.fetchall()
        result1 = ''
        for arr in records1:
            for word in arr:
                result1 += str(word)
                result1 += ''
    

        if (row[1] not in result) and (row[1] not in result1):
            self.cursor.execute(
                f"DELETE FROM subject WHERE id = '{row[0]}' ")
            self.conn.commit()
            self._update_Subject_table()
        else:
            QMessageBox.about(self, "Error", "Нельзя удалить используемый предмет")




    def _Delete_day_from_table(self, rowNumb, day):
        row = list()
        if day == 'Пн':
            for i in range(self.monday_table.columnCount()):
                try:
                    row.append(self.monday_table.item(rowNumb, i).text())
                  
                except:
                    row.append(None)
            self.cursor.execute(
                f"DELETE FROM timetable WHERE id = '{row[0]}' ")
            self.conn.commit()
           
            self._update_monday_table()

        if day == 'Вт':
            for i in range(self.thusday_table.columnCount()):
                try:
                    row.append(self.thusday_table.item(rowNumb, i).text())
                 
                except:
                    row.append(None)

            self.cursor.execute(
                f"DELETE FROM timetable WHERE id = '{row[0]}' ")
            self.conn.commit()
            self._update_thusday_table()
         

        if day == 'Ср':
            for i in range(self.Wednesday_table.columnCount()):
                try:
                    row.append(self.Wednesday_table.item(rowNumb, i).text())
                   
                except:
                    row.append(None)

            self.cursor.execute(
                f"DELETE FROM timetable WHERE id = '{row[0]}' ")
            self.conn.commit()
            self._update_Wednesday_table()
           


        if day == 'Чт':
            for i in range(self.Thursday_table.columnCount()):
                try:
                    row.append(self.Thursday_table.item(rowNumb, i).text())
                
                except:
                    row.append(None)

            self.cursor.execute(
                f"DELETE FROM timetable WHERE id = '{row[0]}' ")
            self.conn.commit()
            self._update_Thursday_table()
         

        if day == 'Пт':
            for i in range(self.Friday_table.columnCount()):
                try:
                    row.append(self.Friday_table.item(rowNumb, i).text())
                  
                except:
                    row.append(None)

            self.cursor.execute(
                f"DELETE FROM timetable WHERE id = '{row[0]}' ")
            self.conn.commit()
            self._update_Friday_table()
         


        if day == 'Сб':
            for i in range(self.Saturday_table.columnCount()):
                try:
                    row.append(self.Saturday_table.item(rowNumb, i).text())
               
                except:
                    row.append(None)

            self.cursor.execute(
                f"DELETE FROM timetable WHERE id = '{row[0]}' ")
            self.conn.commit()
            self._update_Saturday_table()
           




    def _delete_teacher_from_table(self, rowNumb):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNumb, i).text())
               
            except:
                row.append(None)

        self.cursor.execute(
            f"DELETE FROM teacher WHERE id = '{row[0]}' ")
        self.conn.commit()
        self._update_teacher_table()
      


    def _update_shedule(self):
        self._update_monday_table()
        self._update_thusday_table()
        self._update_Wednesday_table()
        self._update_Thursday_table()
        self._update_Friday_table()
        self._update_Saturday_table()
        self._update_Subject_table()
        self._update_teacher_table()


if __name__ == '__main__':
    app =QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
