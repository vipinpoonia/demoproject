from os import environ


class Secrets(object):
    def value(self, key):
        return environ[key]

