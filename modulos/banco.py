_saldo = 0  # "privado" por convención (no exportar ni tocar desde afuera)

def depositar(monto: int) -> None:
    """Suma al saldo interno."""
    global _saldo
    _saldo += int(monto)

def retirar(monto: int) -> bool:
    """Resta del saldo si hay fondos; devuelve True/False según éxito."""
    global _saldo
    monto = int(monto)
    if monto <= _saldo:
        _saldo -= monto
        return True
    return False

def ver_saldo() -> int:
    """Devuelve el saldo actual (solo lectura)."""
    return _saldo

def reiniciar() -> None:
    """Pone el saldo en 0."""
    global _saldo
    _saldo = 0
