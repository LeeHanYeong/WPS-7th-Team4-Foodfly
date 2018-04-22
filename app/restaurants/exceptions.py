__all__ = (
    'GeocodingNotFoundException',
    'FoodflyPointNotFoundException',
    'PointNotFoundError',
)


class GeocodingNotFoundException(Exception):
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return f'Geocoding API에서 다음 주소를 찾을 수 없습니다 ({self.address})'


class FoodflyPointNotFoundException(Exception):
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def __str__(self):
        return f'FOODFLY의 음식점({info})에서 좌표를 찾을 수 없습니다'.format(
            info=f'{self.restaurant.pk}: {self.restaurant.name}'
        )


class RestaurantPointNotFoundError(Exception):
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def __str__(self):
        return f'음식점({info})에서 좌표를 찾을 수 없습니다'.format(
            info=f'{self.restaurant.pk}: {self.restaurant.name}'
        )
