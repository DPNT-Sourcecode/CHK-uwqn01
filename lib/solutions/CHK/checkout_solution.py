

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # if the items entered is not A,B,C,D then also want to return -1
    list_of_items: list = skus.split()
    checkout_dict = {}
    for item in list_of_items:
        if item not in checkout_dict:
            checkout_dict[item] = 1
        else:
            checkout_dict[item] += 1

    

