def common_handler_function(recommendation_dictionary: dict[int: str], temperature: int) -> str:
    try:
        return __handler_function(recommendation_dictionary, temperature)
    except Exception as ex:
        print(ex)


def __handler_function(recommendation_dictionary: dict[int: str], temperature: int) -> str:
    for temperature_dictionary in recommendation_dictionary:
        if temperature_dictionary >= temperature:
            return recommendation_dictionary[temperature_dictionary]
        else:
            continue
