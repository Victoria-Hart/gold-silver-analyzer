from src.visualization import plot_prices, plot_compare

gold = [1000, 2000, 3030, 4242, 6767, 6969]
silver = [22.5, 23.0, 22.8, 67.4]

r1 = plot_prices("Gold", gold)
print("Saved:", r1.file_path)

r2 = plot_prices("Silver", silver)
print("Saved:", r2.file_path)

r3 = plot_compare(gold, silver)
print("Saved:", r3.file_path)
