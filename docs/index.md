# PyDollar-VZLA Documentation

Esta es una librería Python diseñada para obtener de manera eficiente y confiable el precio del dólar en Venezuela a partir de múltiples fuentes. Desarrollada con el propósito de ofrecer una herramienta versátil y fácil de usar, la librería tiene la capacidad de extraer información de diversas páginas web utilizando técnicas de web scraping, combinando las poderosas capacidades de Playwright, BeautifulSoup y Requests para asegurar la exactitud de los datos obtenidos.

## Características Principales

- **Obtención de Datos desde Múltiples Fuentes:** Actualmente, la librería ofrece la capacidad de obtener el precio del dólar en Venezuela desde tres fuentes diferentes, lo que asegura una mayor robustez y fiabilidad en los datos recolectados.
- **Modularidad y Escalabilidad:** Diseñada con un enfoque modular, esta librería está preparada para la incorporación de nuevas fuentes de información en el futuro, lo que garantiza su escalabilidad y adaptabilidad a medida que evolucionan las necesidades del usuario.
- **Fácil Integración:** Gracias a su interfaz intuitiva y sencilla, la librería puede ser fácilmente integrada en proyectos existentes con un mínimo esfuerzo de desarrollo, lo que la convierte en una solución atractiva y práctica para desarrolladores de todos los niveles de experiencia.

## Fuentes Soportadas

- BCV (Banco Central de Venezuela)
- MonitorDolar
- DolarToday

## Instalación

Para instalar PyDollar-VZLA abre una shell interactiva y ejecuta:

I. Instalación de librería 

```bash
    pip install pydollar_vzla
```

II. Instalación de dependencias (Navegadores)

```bash
    playwright install
```

## Uso

```bash
   from pydollar_vzla.dolar_price import DolarPrice

   # Create a PyDollar instance
   pydollar = DolarPrice()

   # Obtain dollar prices
   dollar_prices = pydollar.get_all_dolar_prices()
   print("Dollar prices:", dollar_prices)

```

## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir a PyDollar, por favor sigue estos pasos:

1. Haz un fork del [repositorio](https://github.com/AntonioVilaV/pydollar_vzla).
2. Crea una nueva rama `git checkout -b feature/feature_name`.
3. Realiza tus cambios y documenta tus adiciones.
4. Haz commit de tus cambios `git commit -am 'Añadir nueva característica'`.
5. Haz push a la rama `git push origin feature/feature_name`.
6. Abre un Pull Request