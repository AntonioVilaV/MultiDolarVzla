from modules.sources.DolarToday import DolarTodayExtractor


def main():
    driver_type = "Chrome"
    dolar = DolarTodayExtractor(driver_type)
    price = dolar.get_dolar_price()
    print(price)


if __name__ == "__main__":
    main()
