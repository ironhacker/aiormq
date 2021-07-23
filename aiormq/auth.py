import abc
from enum import Enum


class AuthBase:
    def __init__(self, connector):
        self.connector = connector
        self.value = None

    @abc.abstractmethod
    def encode(self) -> bytes:
        raise NotImplementedError

    def marshal(self) -> bytes:
        if self.value is None:
            self.value = self.encode()
        return self.value


class PlainAuth(AuthBase):
    def encode(self) -> bytes:
        return (
            b"\x00"
            + (self.connector.url.user or "guest").encode()
            + b"\x00"
            + (self.connector.url.password or "guest").encode()
        )

class ExternalAuth(AuthBase):
    def encode(self) -> bytes:
        return (
            b''
        )

class AuthMechanism(Enum):
    PLAIN = PlainAuth
