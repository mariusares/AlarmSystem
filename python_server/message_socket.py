#!/usr/bin/python3
import socketserver
import signal
import time
import os
import threading
from lib.sensors_data import *
class SocketMessage(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            transfer_data = self.request.recv(1024).strip()
            transfer_data = transfer_data.decode()
            print(transfer_data, time_now, trigger, alarm)
            alarm_reset()
            return_data()
            if transfer_data == "reqestData":
               self.request.sendall(str.encode(",".join([str(return_data())])))
            elif transfer_data == "updateSensor":
               get_db_data()
               get_sensors()
               setup_gpios()
               alarm_run()
               return_data()
            elif transfer_data == "requestTrigger":
               self.request.sendall(str.encode(",".join([str(trigger), str(check_temperature())])))
            elif transfer_data == "alarmUnset":
               alarm_reset()
            elif transfer_data == "alarmSet":
               alarm_reset()
            else:
               pass
        except IndexError:
            pass

class MessageServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def socketServer():
    try:
        MessageServer.allow_reuse_address = True
        server = MessageServer(("0.0.0.0", 72), SocketMessage)
        ip, port = server.server_address
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        server.serve_forever()
        server.shutdown()
        server.server_close()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("exit sistem")
        os.kill(os.getpid(), signal.SIGTERM)

alarm_run()
socketServer()
