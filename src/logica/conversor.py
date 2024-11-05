class ConversorMoneda:
    tasas_cambio = {
        ('USD', 'EUR'): 0.85,
        ('USD', 'JPY'): 110,
        ('EUR', 'JPY'): 130,
        ('EUR', 'USD'): 1 / 0.85,
        ('JPY', 'USD'): 1 / 110,
        ('JPY', 'EUR'): 1 / 130,
        ('PEN', 'USD'): 0.27,
        ('PEN', 'EUR'): 0.24,
        ('PEN', 'JPY'): 40.38,
        ('USD', 'PEN'): 1/0.27,
        ('EUR', 'PEN'): 1/0.24,
        ('JPY', 'PEN'): 1/40.38
    }

    def convertir(self, monto, moneda_origen, moneda_destino):
        if monto < 0:
            raise ValueError("El monto no puede ser negativo")
        if moneda_origen == moneda_destino:
            return monto
        try:
            tasa = self.tasas_cambio[(moneda_origen, moneda_destino)]
        except KeyError:
            raise ValueError("Moneda no válida")
        return monto * tasa
