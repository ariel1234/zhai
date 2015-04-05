#!/usr/bin/python3
#
#=================================================================
# uwsgi.py
#
# HISTORY
#-----------------------------------------------------------------
#     DATE    |     AUTHOR     |  VERSION | COMMENT
#-------------+----------------+----------+-----------------------
#  2015-04-05 |     YAN Kai    |   V1.0   | Script Creation
#             |                |          |
#-----------------------------------------------------------------
#=================================================================
#
import os
import sys
sys.path.append('/home/kyan001/KyanToolKit_Unix')
import KyanToolKit_Py
ktk = KyanToolKit_Py.KyanToolKit_Py()

#--Pre-conditions Check-------------------------------------------
ktk.needPlatform("linux");
ktk.runCmd("sudo echo ''");
#--set params-----------------------------------------------------
uwsgi_xml="/home/kyan001/src/zhai/uwsgi.xml"
pid_file="/tmp/uwsgi_zhai.pid"
operations=["start","stop","reload"];
oprtn="";
if len(sys.argv) != 2:
    oprtn = ktk.getChoice(operations);
elif sys.argv[1] in operations:
    oprtn = sys.argv[1];
else:
    ktk.err("Wrong Params: " + sys.argv[1]);
    ktk.byeBye();
#--run commands---------------------------------------------------
if "start" == oprtn:
    ktk.runCmd("sudo uwsgi -x '" + uwsgi_xml +"' --pidfile '" + pid_file + "' &");
elif "stop" == oprtn:
    ktk.runCmd("sudo uwsgi --stop " + pid_file);
elif "reload" == oprtn:
    ktk.runCmd("sudo uwsgi --reload " + pid_file);
else:
    ktk.err("Wrong operation: " + oprtn);
    ktk.byeBye();