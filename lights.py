import wemo
import time
import sys
from threading import Thread

victor_ip = '10.0.0.167'
eric_ip = '10.0.0.58'


class Switcher:
    def __init__(self, ip, name='Wemo Switch'):
        self.run_thread = False
        self.name = name
        self.ip = ip
        self.switch = wemo.switch(ip)
        self.switch_thread = None
        self.strobe_on = False

    def start_strobe(self):
        if not self.run_thread:
            self.switch_thread = Thread(target=self.run, daemon=False)
            self.switch_thread.start()
            self.strobe_on = True

    def stop_strobe(self):
        self.run_thread = False
        self.strobe_on = False

    def lights_on(self):
        self.stop_strobe()
        self.switch.enable()

    def lights_off(self):
        self.stop_strobe()
        self.switch.disable()

    def run(self):
        self.run_thread = True
        while self.run_thread:
            self.switch.local_toggle()
            time.sleep(.45)

    def strobe_is_on(self):
        return self.strobe_on

    def get_status(self):
        return self.switch.getStatus()


sys.stdout.write('Initializing light switches.')
victor_switcher = Switcher(victor_ip, name='House Generator')
# eric_switcher = Switcher(eric_ip, name='Eric\'s Room')
sys.stdout.write('\rLights Ready.\n')
