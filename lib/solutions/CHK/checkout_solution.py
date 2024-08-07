price_list = {"A":50, "B":30,"C":20,"D":15}
special_offers = {"A":[3,130],"B":[2,45]}

def checkout(skus: str) -> int:
    # if the items entered is not A,B,C,D then also want to return -1
    list_of_items: list = skus.split(",")
    checkout_dict = {}
    # create a dictionary where the grocery item is the key and the value is a count of each item
    for item in list_of_items:
        if item not in checkout_dict:
            checkout_dict[item] = 1
        else:
            checkout_dict[item] += 1
    # look at the special offers and find the count of the items that exist in the special_offers dict
    for grocery_item in checkout_dict:
        if grocery_item in special_offers:
            count_grocery_item = checkout_dict[grocery_item] #5
            special_offers_price = (count_grocery_item // special_offers[grocery_item][0])*special_offers[grocery_item][1]
            checkout_dict[grocery_item] = (count_grocery_item % special_offers[grocery_item][0])


