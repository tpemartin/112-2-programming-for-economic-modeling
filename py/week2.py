def cobb_douglas(K, L):

    # Create alpha and z
    z = 1
    alpha = 0.33

    return z * K**alpha * L**(1 - alpha)

def marginal_products(K, L, epsilon):

    mpl = (cobb_douglas(K, L + epsilon) - cobb_douglas(K, L)) / epsilon
    mpk = (cobb_douglas(K + epsilon, L) - cobb_douglas(K, L)) / epsilon

    return mpl, mpk

tup = marginal_products(1.0, 0.5,  1e-4)
print(tup)

