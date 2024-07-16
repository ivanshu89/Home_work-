def mask_account_card(card_number: str) -> str:
    """Функция обрабатывает информацию о картах и счетах и возвращает маску"""

    if "Счет" in card_number:
        return f"{card_number[:-20]}** {card_number[-4:]}"
    else:
        return f"{card_number[:-16]}{card_number[-16: -12]} {card_number[-12: -10]}** **** {card_number[-4:]}"


def get_date(long_date: str) -> str:
    return f"{long_date[8:10]}.{long_date[5:7]}.{long_date[:4]}"
