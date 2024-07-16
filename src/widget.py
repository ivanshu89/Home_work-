def mask_account_card(card_number: str) -> str:
    """Функция обрабатывает информацию о картах и счетах и возвращает маску"""

    if "Счет" in card_number:
        return f"{card_number[:-20]}** {card_number[-4:]}"
    else:
        return f"{card_number[:-16]}{card_number[-16: -12]} {card_number[-12: -10]}** **** {card_number[-4:]}"
