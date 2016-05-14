import re;
def nor(phone):
    digits = filter(lambda c: c.isdigit() or c == '+', str(phone))
    match = re.match(r'^(0|\+?254)(?P<number>\d{9})$', digits)
    if match:
        phone_number = '0' + match.groupdict()['number']
    print phone_number


nor("+254707867162")
