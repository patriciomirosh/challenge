import time

import pyRofex


def iniciar(ticker2, REMARKETS_USER, REMARKET_PASS, REMARKET_ACCOUNT):
    def error_handler(message):
        print("Simbolo invalido")

    def market_data_handler(message):
        print("se ha reportado una solicutud al market data")

    def exception_handler(e):
        print("Exception Ocurred")

    def order_report_handler(message):
        print("se ha reportado una orden")
    print("~$ python challenge.py ", ticker2, " -u ",
          REMARKETS_USER, " -p ", REMARKET_PASS)
    print("Iniciando sesion en Remarket")
  # bloque try/except para autencticacion de password
    try:
        pyRofex.initialize(user=REMARKETS_USER, password=REMARKET_PASS,
                           account=REMARKET_ACCOUNT, environment=pyRofex.Environment.REMARKET)
    except:
        print("Error de autenticacion")
        print("~$")
        print("por favor vuelva a ingresar sus credenciales")
        exit()
    else:
        pyRofex.init_websocket_connection(market_data_handler=market_data_handler,
                                          error_handler=error_handler,
                                          order_report_handler=order_report_handler,
                                          exception_handler=exception_handler)

    print("Consultando simbolo")

    md = pyRofex.get_market_data(ticker=ticker2, entries=[
                                 pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.LAST])
    # capturar el key error de market data
    try:
        lp = md["marketData"]["LA"]["price"]
    except KeyError:
        print("Símbolo inválido")
    else:
        lp = md["marketData"]["LA"]["price"]
        print("Último precio operado:  $", lp)
        print("consultando BID")
        try:
            md["marketData"]["BI"][0]["price"]
        except KeyError:
         # en este caso reemplace el valor constante de 75.25 por un valor que cuando se hable del dolar septiembre el valor sea de 75.25 en el bid ofertado. 
         # Pero que si hablamos de otro activo (otro instrumento) este se mantenga en un valor competitivo para la oferta/demanda.
            pyRofex.send_order(ticker=ticker2, side=pyRofex.Side.BUY, size=1,
                               price=lp - 0.91, order_type=pyRofex.OrderType.LIMIT)
            print("No hay Bids Activos")
            bido = lp - 0.91
            print("ingresando orden :$", bido)

        else:
            pyRofex.send_order(ticker=ticker2, side=pyRofex.Side.BUY, size=1,
                               price=md["marketData"]["BI"][0]["price"]-0.01, order_type=pyRofex.OrderType.LIMIT)
            bid = md["marketData"]["BI"][0]["price"]
            bido = bid-0.01
            print("Precio de BID: $", bid)
            print("ingresando orden :$", bido)
    print("cerrando sesion en Remarket")
    time.sleep(5)
    pyRofex.close_websocket_connection()
    print("~$")


# Datos nescesarios para el ingreso
ticker2 = input("ingrese el simbolo a operar: ")
REMARKETS_USER = input("ingrese el usuario:pato16pp5012: ")
REMARKET_PASS = input("ingrese el password: ")
iniciar(ticker2, REMARKETS_USER, REMARKET_PASS, "REM5012")
