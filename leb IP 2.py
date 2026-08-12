def bagi(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("penyebut tidak boleh nol")
    return a / b