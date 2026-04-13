BASE_PRICE = 50
PRICE_PER_KM = 12


def calculateDistance(start_km, end_km):
    distance = abs(end_km - start_km)
    return distance


def calculateRidePrice(distance):
    price = BASE_PRICE + distance * PRICE_PER_KM
    return price


def createRide(client_name, start_km, end_km):
    distance = calculateDistance(start_km, end_km)
    price = calculateRidePrice(distance)

    print("----- Ride info -----")
    print("Client:", client_name)
    print("Distance:", distance, "km")
    print("Price:", price, "UAH")


if __name__ == "__main__":
    createRide("Ivan", 5, 20)
