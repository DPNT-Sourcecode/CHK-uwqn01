price_list = {"A":50, "B":30,"C":20,"D":15,"E":40}
class BogoffDeal():
    def __init__(self, purchase_qty: int,free_qty: int,free_item: str):
        self.purchase_qty = purchase_qty
        self.free_qty = free_qty
        self.free_item = free_item


bogoff = {
    "E": [BogoffDeal(2, 1, "B")]
}


class Deal():
    def __init__(self, price: int, qty: int):
        self.price = price
        self.qty = qty


special_offers = {
    "A": [
        Deal(200,5),
        Deal(130,3)
    ],
    "B": [
        Deal(45,2)
    ]
}



def checkout(skus: str) -> int:
    if skus == "":
        return 0
    # if the items entered is not A,B,C,D then also want to return -1
    if "," in skus:
        list_of_items = [item.strip() for item in skus.split(",")]
    else:
        list_of_items = list(skus)
    checkout_dict = {}
    # create a dictionary where the grocery item is the key and the value is a count of each item
    for item in list_of_items:
        item = item
        if item not in checkout_dict:
            checkout_dict[item] = 1
        else:
            checkout_dict[item] += 1
    # look at the special offers and find the count of the items that exist in the special_offers dict
    total = 0
    for grocery_item in checkout_dict:
        if grocery_item not in price_list:
            return -1
        if grocery_item in bogoff and bogoff[grocery_item][0].free_item in checkout_dict: #reduce the count of B in the checkout by 1 for every 2 Es
            eligible_free_qty = checkout_dict[grocery_item]//bogoff[grocery_item][0].purchase_qty
            if checkout_dict[bogoff[grocery_item][0].free_item] >= eligible_free_qty:
                checkout_dict[bogoff[grocery_item][0].free_item] -= eligible_free_qty
            else:
                checkout_dict[bogoff[grocery_item][0].free_item] = 0

    for grocery_item in checkout_dict:
        if grocery_item in special_offers:
            offer_num = len(special_offers[grocery_item])
            for deal in special_offers[grocery_item]:
                count_grocery_item = checkout_dict[grocery_item]
                total += ((count_grocery_item // deal.qty) *
                          deal.price)
                checkout_dict[grocery_item] = (count_grocery_item % deal.qty)
        total += checkout_dict[grocery_item]*price_list[grocery_item]
    return total





