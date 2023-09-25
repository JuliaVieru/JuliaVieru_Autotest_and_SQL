import pytest
import senter_stand_request
import data

# Получить номер трека
def to_get_track_number():
    resp_new_body = senter_stand_request.create_new_order()
    return resp_new_body.json()["track"]

# Передать номер трека в параметры
params = data.params.copy()
params["t"] = to_get_track_number()

# Позитивная проверка статус кода
def positive_assert(params):
    request = senter_stand_request.to_get_order_under_truck_number(params)
    assert request.status_code == 200


#Тест на проверку статус кода
def test_track_status():
    positive_assert(params)

# Юлия Виеру когорта 8а Финальный проект

