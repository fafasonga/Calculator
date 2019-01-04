

orig_amount = float(input("\nPlease Enter Original Price: "))
disc_perc = float(input("Please Enter Discount Percentage: "))
# orig_amount = 12000
# disc_perc = 70


conv = float(disc_perc / 100)
disc_rate = float(orig_amount * conv)

disc_value = orig_amount - disc_rate

print("\nThe Original Price is = ", orig_amount, "\nThe Percentage rate Discount is = ", disc_perc, "%",
      "\nSales Price after Discount = ", disc_value, "\nYou Saved = ", disc_rate)


orig_amount = float(input("\nPlease Enter Original Price: "))
disc_rate = float(input("Please Enter Discount Price: "))
# orig_amount = 12000
# disc_rate = 3600
#
result = float((1 - float(disc_rate/orig_amount)) * 100)
print("\nThe Original Price is = ", orig_amount, "\nThe Discount Price is = ", disc_rate,
      "\nThe Discount Percentage is = ", result, "%")
