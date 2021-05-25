from purchases.purchase import Purchase


def purchases_counter(request):
    purchase = Purchase(request)
    counter = len(purchase)
    return {
        "purchases_counter": counter
    }
