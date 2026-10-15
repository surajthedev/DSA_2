# A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

# 't' that evaluates to true.
# 'f' that evaluates to false.
# '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
# '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# Given a string expression that represents a boolean expression, return the evaluation of that expression.

# It is guaranteed that the given expression is valid and follows the given rules.



# Example 1:

# Input: expression = "&(|(f))"
# Output: false
# Explanation:
# First, evaluate |(f) --> f. The expression is now "&(f)".
# Then, evaluate &(f) --> f. The expression is now "f".
# Finally, return false.
# Example 2:

# Input: expression = "|(f,f,f,t)"
# Output: true
# Explanation: The evaluation of (false OR false OR false OR true) is true.
# Example 3:

# Input: expression = "!(&(f,t))"
# Output: true
# Explanation:
# First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
# Then, evaluate !(f) --> NOT false --> true. We return true.


# Constraints:

# 1 <= expression.length <= 2 * 104
# expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
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
### Brute Force

python
```
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        while len(expression) > 1:
            i = expression.rfind(')')

            j = i - 1
            while expression[j] != '(':
                j -= 1

            op = expression[j - 1]
            sub = expression[j + 1:i]

            if op == '!':
                result = sub == 'f'
            elif op == '&':
                result = 'f' not in sub
            else:
                result = 't' in sub

            expression = expression[:j - 1] + ('t' if result else 'f') + expression[i + 1:]

        return expression == 't'
```

### Optimal — Stack

python
```
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch == ',':
                continue

            if ch != ')':
                stack.append(ch)
            else:
                has_true = False
                has_false = False

                while stack[-1] != '(':
                    val = stack.pop()
                    if val == 't':
                        has_true = True
                    elif val == 'f':
                        has_false = True

                stack.pop()
                op = stack.pop()

                if op == '!':
                    result = not has_true
                elif op == '&':
                    result = not has_false
                else:
                    result = has_true

                stack.append('t' if result else 'f')

        return stack[-1] == 't'
```
