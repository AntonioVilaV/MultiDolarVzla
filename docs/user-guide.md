# PyDollar-VZLA guía de usuario

Esta guía es una visión general y explica las características importantes y los detalles se encuentran en PyDollar-VZLA.

## Obtener el precio del dólar de las diferentes fuentes soportadas

```bash
   from pydollar_vzla.dolar_price import DolarPrice

   pydollar = DolarPrice()
   dollar_prices = pydollar.get_all_dolar_prices()
   print("Dollar prices:", dollar_prices)

```

## Obtener todos los extractores soportados
```bash
   from pydollar_vzla.dolar_price import DolarPrice

   pydollar = DolarPrice()
   extractors = pydollar.get_all_extractors()
   print("extractors:", extractors)

```

## Agregar nuevo extractor
```bash
   from pydollar_vzla.dolar_price import DolarPrice
   new_extractor = NewExtractor() # Must inherit from class DolarSource
   pydollar = DolarPrice()
   extractors = pydollar.add_extractor(new_extractor)
   print("extractors:", extractors)

```

## Obtener el precio del dolar de una sola fuente
```bash
   from pydollar_vzla.sources.dolartoday import DolarTodayExtractor
   from pydollar_vzla.sources.bcv import BCVExtractor
   from pydollar_vzla.sources.monitordolar import MonitorDolarExtractor

   dolartoday = DolarTodayExtractor()
   dolartoday_price = dolartoday.get_dolar_price()
   print(dolartoday_price)

   bcv = BCVExtractor()
   bcv_price = bcv.get_dolar_price()
   print(bcv_price)

   monitordolar = MonitorDolarExtractor()
   monitordolar_price = monitordolar.get_dolar_price()
   print(monitordolar_price)   

```

