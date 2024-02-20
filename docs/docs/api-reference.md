# PyDollar-VZLA referencia

Este manual de referencia detalla las funciones, módulos y objetos incluidos en PyDollar_VZLA, describiendo qué son y qué hacen.

### DolarPrice
Esta clase se encarga de recoger todos los extractores y concatenar todos las tasas del dolar
```bash
   from pydollar_vzla.dolar_price import DolarPrice

   pydollar = DolarPrice()
```
#### get_all_extractors():
Obtiene todas las instancias de extractores o fuentes del precio del dólar.
#### add_extractor(DolarSource):
- Recibe una instancia que hereda de la clase DolarSource, que funciona como extractor del precio del dólar.
- Añade el nuevo extractor a la lista de fuentes
#### get_all_dolar_prices():
- Devuelve un diccionario con el precio del dólar de las diferentes fuentes que declaran la cotización del dólar (DolarSource).

### DolarSource

Se trata de una clase abstracta que deben implementar todas las fuentes de cotización del dólar que se agregan a la librería

```bash
   from pydollar_vzla.sources.base import DolarSource
```
#### get_name():
Retorna un string con el nombre de la fuente
#### get_dolar_price():
Comprueba si el valor obtenido por clean_data() es nulo y devuelve el valor del dólar o None si el valor es <= 0.
#### clean_data():
Obtiene una cadena con el valor en dólares de get_dolar_data() y lo formatea a float.
#### get_dolar_data():
Extrae el valor del dólar de la página web indicada y devuelve una cadena con los datos.

### Extractores que implementan la clase DolarSource

Los extractores son las clases que contienen la lógica de solicitud y extracción de los datos a la fuente del valor del dólar.

```bash
   from pydollar_vzla.sources.dolartoday import DolarTodayExtractor
   from pydollar_vzla.sources.bcv import BCVExtractor
   from pydollar_vzla.sources.monitordolar import MonitorDolarExtractor

   dolartoday = DolarTodayExtractor()
   bcv = BCVExtractor()
   monitordolar = MonitorDolarExtractor()
```
