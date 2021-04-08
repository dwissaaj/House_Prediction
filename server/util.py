import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, bedrooms, bathrooms, sqft, floors, condition):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = sqft
    x[3] = floors
    x[4] = condition
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts..start")
    global __data_columns
    global __locations

    global __model
    with open("./artifacts\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]
    with open('./artifacts\house_model_pickle.pkl', 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts..done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
