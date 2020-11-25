def common_handler_function(recommendation_dictionary: dict[int: str]) -> str:
    try:
        for temperature in recommendation_dictionary:
            if temperature <= temperature:
                return recommendation_dictionary[temperature]
            else:
                continue
    except Exception as ex:
        print(ex)
