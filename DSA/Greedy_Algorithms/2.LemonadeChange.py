# Always return the largest possible bills first (greedy).

# 🍋 Lemonade Change Problem (LeetCode 860)
#     You are selling lemonade for $5 each.
#     Customers come in a fixed order and pay using: $5, $10, or $20 bills
#     You must determine if you can provide correct change for every customer, given no initial cash.


def lemonadeChange(bills):
    five = ten = 0

    for bill in bills:
        if bill == 5:
            five += 1

        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1

        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True


# | Payment | Change Needed | Prefer       | Backup         |
# | ------- | ------------- | ------------ | -------------- |
# | $5      | $0            | —            | —              |
# | $10     | $5            | use one $5   | no alternative |
# | $20     | $15           | **$10 + $5** | **3 × $5**     |
