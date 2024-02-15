from modules.sources.BCV import BCVExtractor


def main():
    dolar = BCVExtractor()
    price = dolar.get_dolar_price()
    print(price)


if __name__ == "__main__":
    main()
