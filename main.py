# -*- coding: utf-8 -*- 

from module_teste import imprimindo_algo 

print(imprimindo_algo())

def print_my_name_and_age(name: str, age: int) -> str:
    """[summary]

    Args:
        name (str): [description]
        age (int): [description]

    Returns:
        str: [description]
    """
    return f'Hi! My name is {name} and my age is {age} years'

print(print_my_name_and_age(
                            name='will',
                            age='50'
                            ))