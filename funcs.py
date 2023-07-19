import re
from aiohttp import ClientSession
from datetime import date


def calculate_luhn(cc):
    numMap = map(int, str(cc))
    num = list(numMap)
    check_digit = (
        10 - sum(num[-2::-2] + [sum(divmod(d * 2, 10)) for d in num[::-2]]) % 10
    )
    return 0 if check_digit == 10 else check_digit


def get_cc(text) -> bool | list:
    text = text.strip()
    finds = re.findall(r"\d+", text)
    finds = finds[:4]

    if len(finds) < 4:
        return False

    cc = finds[0]
    mes = finds[1]
    ano = finds[2]
    cvv = finds[3]
    if not cc or cc[0] not in ["3", "4", "5", "6"]:
        return False

    elif (
        (cc[0] == "3" and len(cc) != 15) or (cc[0] != "3" and len(cc) != 16)
    ) or not calculate_luhn(cc):
        return False
    elif (
        len(ano) == 4
        and ano == str(date.today().year)
        and int(mes) not in range(date.today().month, 13)
    ) or (
        len(ano) == 2
        and ano == str(date.today().year)[2:]
        and int(mes) not in range(date.today().month, 13)
    ):
        return False
    elif (
        len(ano) not in [2, 4]
        or (len(ano) == 4 and int(ano) not in range(date.today().year, 2050))
        or (len(ano) == 2 and int(ano) not in range(date.today().year % 100, 30))
    ):
        return False
    elif (cc[0] == "3" and len(cvv) != 4) or (cc[0] != "3" and len(cvv) != 3):
        return False
    else:
        return [cc.strip(), mes.strip(), ano.strip(), cvv.strip()]


async def get_bin(bin: str) -> bool | dict:
    if not isinstance(bin, str) or not bin.isdigit() or len(bin) != 6:
        return False

    async with ClientSession() as session:
        async with session.get(f"https://bins.antipublic.cc/bins/{bin}") as resp:
            if resp.status != 200:
                return False
            data = await resp.json()
            brand = data["brand"]
            country = data["country_name"]
            country_flag = data["country_flag"]
            bank = data["bank"]
            level = data["level"]
            type = data["type"]
            return {
                "bin": bin,
                "brand": brand,
                "country": country,
                "country_flag": country_flag,
                "bank": bank,
                "level": level,
                "type": type,
            }
