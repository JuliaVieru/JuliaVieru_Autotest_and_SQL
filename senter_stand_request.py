import data
import configuration
import requests

# Функция для создания заказа
def create_new_order():
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_NEW_ORDER_PATH, json=data.order_body,
                         headers=data.headers)

# Функция для получения заказ по номеру трека
def to_get_order_under_truck_number(params):
    response_order = requests.get(configuration.URL_SERVICE+configuration.GET_TRACK_NUMBER_PATH, params=params)
    return response_order


