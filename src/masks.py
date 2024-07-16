from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает номер карты и возвращает маку"""

    card_number_mask = str(card_number)
    return f"{card_number_mask[0: 4]} {card_number_mask[4: 6]}** **** {card_number_mask[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает номер счета и возвращает маку"""

    account_number_mask = str(account_number)
    return f"** {account_number_mask[-4:]}"
