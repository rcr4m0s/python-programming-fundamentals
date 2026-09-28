prices = [100, 250, 400, 50, 600, 150]

expensive_prices = [p for p in prices if p > 200]

discounted_prices = [p * 0.9 for p in prices]

print(f"Expensive: {expensive_prices}")
print(f"Discounted: {discounted_prices}")