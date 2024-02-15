import setuptools

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dolar-price-vzla",
    version="0.1.0",
    author="Antonio Vila",
    author_email="vila.antoniojose@gmail.com",
    description="Obtén el precio del dólar en Venezuela desde múltiples fuentes con una sola línea de código! Nuestra biblioteca proporciona una manera sencilla y poderosa de acceder y manejar los precios del dólar desde diversas fuentes en línea, todo en un único lugar conveniente. Con funciones de webscraping integradas, recopilamos y consolidamos los datos más actualizados para que puedas tomar decisiones informadas sobre tus transacciones financieras en Venezuela. ¡Dile adiós a buscar precios dispersos y hola a una solución completa y fácil de usar con nuestra biblioteca!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntonioVilaV/dolar-price-vzla",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "beautifulsoup4>=4.12.3",
        "requests>=2.31.0",
        "selenium>=4.17.2",
    ],
)
