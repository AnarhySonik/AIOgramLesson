from typing import Any
from typing import Optional
from typing import Union
from typing import Literal


def any_func(arg: Any) -> None:
    pass


def optional_func(var_1: Optional[int]):
    pass


def union_func(var_1: Union[int, float], var_2: Union[list, tuple, set]):
    pass


def literal_func(user: dict[Literal['name'] | Literal['second_name'] | Literal['username'], str]):
    pass


user_var: dict[Literal['name'] | Literal['second_name'] | Literal['username'], str] = {}

user_var['gender'] = 'male'
