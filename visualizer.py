from modules.sources.MonitorDolar import MonitorDolarExtractor


def main():
    driver_type = "Chrome"
    dolar = MonitorDolarExtractor(driver_type)
    price = dolar.get_dolar_price()
    print(price)


if __name__ == "__main__":
    main()
