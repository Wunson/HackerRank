def is_leap(year: int) -> bool:
    if year % 4:
        return False
    if year % 100:
        return True
    if year % 400:
        return False
    return True

if __name__ == '__main__':
    for year in [2000, 2400]:
        assert(is_leap(year))
    for year in [1800, 1900, 2100, 2200, 2300, 2500]:
        assert(not is_leap(year))