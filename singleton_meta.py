from __future__ import annotations

from typing import Dict


class SingletonMeta(type):
    __instances: Dict = {}

    def __call__(cls, *args, **kwargs) -> SingletonMeta:  # type: ignore
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]
