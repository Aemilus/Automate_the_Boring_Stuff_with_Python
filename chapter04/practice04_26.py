def add_to_shopping_cart(_cart, product):
    # _cart will reference the object passed as argument, not a copy of the object
    print('_cart id:', id(_cart))
    _cart.append(product)
    # no need to return _cart because we worked on a mutable object via it's reference


if __name__ == '__main__':
    cart = ['eggs', 'tomatoes']
    print(id(cart), cart)

    add_to_shopping_cart(cart, 'onion')
    add_to_shopping_cart(cart, 'milk')
    add_to_shopping_cart(cart, 'salt')
    add_to_shopping_cart(cart, 'ice cream')
    print(id(cart), cart)
