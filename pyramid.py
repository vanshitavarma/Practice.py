height = int(input("Enter the height of the pyramid: "))

# Loop through each row of the pyramid
for i in range(1, height + 1):
    # Calculate spaces and stars for the current row
    spaces = height - i
    stars = 2 * i - 1
    # Print the row with spaces and stars
    print(" " * spaces + "*" * stars)


