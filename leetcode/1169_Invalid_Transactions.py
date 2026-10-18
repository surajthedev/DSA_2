# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

# Return a list of transactions that are possibly invalid. You may return the answer in any order.



# Example 1:

# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
# Example 2:

# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
# Example 3:

# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]


# Constraints:

# transactions.length <= 1000
# Each transactions[i] takes the form "{name},{time},{amount},{city}"
# Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
# Each {time} consist of digits, and represent an integer between 0 and 1000.
# Each {amount} consist of digits, and represent an integer between 0 and 2000.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ### 1. Brute Force — O(n²)

python
```
class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        n = len(transactions)
        parsed = [t.split(",") for t in transactions]
        invalid = [False] * n

        for i in range(n):
            name1, time1, amount1, city1 = parsed[i]
            time1, amount1 = int(time1), int(amount1)

            if amount1 > 1000:
                invalid[i] = True

            for j in range(i + 1, n):
                name2, time2, amount2, city2 = parsed[j]
                time2 = int(time2)

                if (
                    name1 == name2
                    and city1 != city2
                    and abs(time1 - time2) <= 60
                ):
                    invalid[i] = True
                    invalid[j] = True

        return [
            transactions[i]
            for i in range(n)
            if invalid[i]
        ]
```

### 2. Optimal Solution — O(n²)

python
```
class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        parsed = [t.split(",") for t in transactions]
        n = len(transactions)
        invalid = [False] * n

        for i, (name1, time1, amount1, city1) in enumerate(parsed):
            if int(amount1) > 1000:
                invalid[i] = True

            for j, (name2, time2, amount2, city2) in enumerate(parsed):
                if i == j:
                    continue

                if (
                    name1 == name2
                    and city1 != city2
                    and abs(int(time1) - int(time2)) <= 60
                ):
                    invalid[i] = True
                    break

        return [
            transactions[i]
            for i in range(n)
            if invalid[i]
        ]
```
