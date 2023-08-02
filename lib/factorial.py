def factorial(n):
    product = 1
    print(f"at the start product is {product}")
    while n > 0:
        product *= n
        print(f"we multiply {product} by {n}")
        n -= 1
        print(f"we get {product}")
      
    return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")