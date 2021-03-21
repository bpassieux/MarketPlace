import logging
logging.basicConfig(level=logging.DEBUG)
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, Float
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class HelloWorldService(ServiceBase):
    @rpc(Float, Float, Float, Integer, _returns=Float)
    def fdp(self, prix, distance, poids, nombre) :
        # Retourne le prix final (ajout des fdp)
        return (nombre * prix) + min((distance * poids / 5 ), poids * 5)

application = Application([HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

app = WsgiApplication(application)