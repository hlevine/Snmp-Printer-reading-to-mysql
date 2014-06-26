Snmp-Printer-reading-to-mysql
=============================

A python application to upload page counts, serial numbers, model and the level of consumables to a mysql database

Required software to install.<br>
Python 2.7<br>
MySQL-python-1.2.3.win32-py2.7<br>
pycrypto-2.6.win32-py2.7<br>
ez_tools<br>
pysnmp to be installed via ez_tools<br>
To schedule a task with windows task scheduler<br>
schedule the tak with the full path to python and the full path to script.  Also to prevent popups in windows use teh pythonw.exe not the python.exe.<br>
To Install <br>
Create database, create database user, import table script, update reader.py and run. If any one manages to get this to compile with py2exe, please lt me know.
