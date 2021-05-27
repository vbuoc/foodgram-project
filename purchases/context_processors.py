from purchases.purchase import Purchase


def purchases_counter(request):
    purchase_counter = len(Purchase(request))
    return {
        "purchases_counter": purchase_counter if purchase_counter > 0 else None
    }
