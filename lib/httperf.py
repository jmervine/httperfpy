import cStringIO
from subprocess import Popen, PIPE, STDOUT

class Httperf(object):

    def __init__(self, path=None, **kwargs):
        self.params = {}
        self.parser = False
        if path == None:
            self.path = "httperf"
        else:
            self.path = path

        for key in kwargs:
            if not key in set(self.__params().keys()):
                raise Exception("Invalid httperf option passed:: " + key)
            self.params[key] = kwargs[key]


    def update_option(self, key, val):
        self.params[key] = val

    def run(self):
        self.results = Popen(self.__cmd(), shell=True, stdout=PIPE, stderr=STDOUT, close_fds=True).stdout.read()
        if self.parser:
            return self.results
        else:
            return self.results

    def __cmd(self):
        outstr = self.path
        for key in self.params.keys():
            outstr = outstr + " --" + key + "=\"" + self.params[key] + "\""
        return outstr

    def __params(self):
       return { 
          "add-header": None,
          "burst-length": None,
          "client": None,
          "close-with-reset": None,
          "debug": None,
          "failure-status": None,
          "hog": None,
          "http-version": None,
          "max-connections": None,
          "max-piped-calls": None,
          "method": None,
          "no-host-hdr": None,
          "num-calls": None,
          "num-conns": None,
          "period": None,
          "port": None,
          "print-reply": None,
          "print-request": None,
          "rate": None,
          "recv-buffer": None,
          "retry-on-failure": None,
          "send-buffer": None,
          "server": None,
          "server-name": None,
          "session-cookies": None,
          "ssl": None,
          "ssl-ciphers": None,
          "ssl-no-reuse": None,
          "think-timeout": None,
          "timeout": None,
          "uri": None,
          "verbose": None,
          "version": None,
          "wlog": None,
          "wsess": None,
          "wsesslog": None,
          "wset": None } 

