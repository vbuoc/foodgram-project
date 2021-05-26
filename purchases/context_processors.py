from purchases.purchase import Purchase


def purchases_counter(request):
    purchase = Purchase(request)
    return {
        "purchases_counter": len(purchase)
    }
