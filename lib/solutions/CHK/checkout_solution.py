price_list = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35, "J": 60,
              "K": 70, "L": 90, "M":15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50, "S": 20, "T": 20, "U": 40,
              "V": 50, "W": 20, "X": 17, "Y": 20, "Z": 21}
class BogoffDeal():
    def __init__(self, purchase_qty: int,free_qty: int,free_item: str):
        self.purchase_qty = purchase_qty
        self.free_qty = free_qty
        self.free_item = free_item


bogoff = {
    "E": [BogoffDeal(2, 1, "B")],
    "F": [BogoffDeal(3, 1, "F")],
    "N": [BogoffDeal(3, 1, "M")],
    "R": [BogoffDeal(3, 1, "Q")],
    "U": [BogoffDeal(4, 1, "U")],
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
    ],
    "H": [
        Deal(80,10),
        Deal(45,5)
    ],
    "K": [
        Deal(150,2),
    ],
    "P": [
        Deal(200,5)
    ] ,
    "Q": [
        Deal(80,3)
    ],
    "V": [
        Deal(130,3),
        Deal(90,2)
    ]
}


class GroupOffer():
    def __init__(self, grp_items: list, qty_req: int, price: int):
        self.grp_items = grp_items
        self.qty_req = qty_req
        self.price = price


group_offer = GroupOffer(["Z","S", "T", "Y", "X"], 3, 45)


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
    # checking for the group offers
    sum_eligible_qnt = 0
    for offer_item in group_offer.grp_items:
        if offer_item in checkout_dict:
            sum_eligible_qnt += checkout_dict[offer_item]

    group_off_num = (sum_eligible_qnt//group_offer.qty_req)
    qty_eligible_grp_deal = group_off_num * group_offer.qty_req
    total = group_off_num * group_offer.price
    for group_offer_item in group_offer.grp_items:
        if group_offer_item in checkout_dict:
            if checkout_dict[group_offer_item] <= qty_eligible_grp_deal:
                qty_eligible_grp_deal -= checkout_dict[group_offer_item]
                checkout_dict[group_offer_item] = 0
            else:
                checkout_dict[group_offer_item] -= qty_eligible_grp_deal
                qty_eligible_grp_deal = 0

        # checking for bogoff offers
    for grocery_item in checkout_dict:
        if grocery_item not in price_list:
            return -1
        if grocery_item in bogoff and bogoff[grocery_item][0].free_item in checkout_dict: #reduce the count of B in the checkout by 1 for every 2 Es
            eligible_free_qty = checkout_dict[grocery_item]//bogoff[grocery_item][0].purchase_qty
            if checkout_dict[bogoff[grocery_item][0].free_item] >= eligible_free_qty:
                checkout_dict[bogoff[grocery_item][0].free_item] -= eligible_free_qty
            else:
                checkout_dict[bogoff[grocery_item][0].free_item] = 0
    # checking for special qty price offers
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



