class Mailing:

    def __init__(self, track, from_address, to_address, cost):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.from_address} "
                f"в {self.to_address}. Стоимость: {self.cost} рублей.")
