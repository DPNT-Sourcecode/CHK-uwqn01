price_list = {"A":50, "B":30,"C":20,"D":15}
special_offers = {"A":[3,130],"B":[2,45]}


def checkout(skus: str) -> int:
    if skus == "":
        return 0
    # if the items entered is not A,B,C,D then also want to return -1
    list_of_items: list = skus.split(",")
    checkout_dict = {}
    # create a dictionary where the grocery item is the key and the value is a count of each item
    for item in list_of_items:
        item = item.strip().upper()
        if item not in checkout_dict:
            checkout_dict[item] = 1
        else:
            checkout_dict[item] += 1
    # look at the special offers and find the count of the items that exist in the special_offers dict
    total = 0
    for grocery_item in checkout_dict:
        if grocery_item not in price_list:
            return -1
        if grocery_item in special_offers:
            count_grocery_item = checkout_dict[grocery_item]
            total += (count_grocery_item // special_offers[grocery_item][0])*special_offers[grocery_item][1]
            checkout_dict[grocery_item] = (count_grocery_item % special_offers[grocery_item][0])
        total += checkout_dict[grocery_item]*price_list[grocery_item]
    return total

