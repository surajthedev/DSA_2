# HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

# The special characters and their entities for HTML are:

# Quotation Mark: the entity is &quot; and symbol character is ".
# Single Quote Mark: the entity is &apos; and symbol character is '.
# Ampersand: the entity is &amp; and symbol character is &.
# Greater Than Sign: the entity is &gt; and symbol character is >.
# Less Than Sign: the entity is &lt; and symbol character is <.
# Slash: the entity is &frasl; and symbol character is /.
# Given the input text string to the HTML parser, you have to implement the entity parser.

# Return the text after replacing the entities by the special characters.



# Example 1:

# Input: text = "&amp; is an HTML entity but &ambassador; is not."
# Output: "& is an HTML entity but &ambassador; is not."
# Explanation: The parser will replace the &amp; entity by &
# Example 2:

# Input: text = "and I quote: &quot;...&quot;"
# Output: "and I quote: \"...\""


# Constraints:

# 1 <= text.length <= 105
# The string may contain any possible characters out of all the 256 ASCII characters.
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
#
#
#
#
#
#
# ### Brute Force

python

```python
class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        for entity, char in entities.items():
            text = text.replace(entity, char)

        return text
```

### Optimal (Single Pass)

python

```python
class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        ans = []
        i = 0

        while i < len(text):
            if text[i] == '&':
                found = False

                for entity, char in entities.items():
                    if text.startswith(entity, i):
                        ans.append(char)
                        i += len(entity)
                        found = True
                        break

                if found:
                    continue

            ans.append(text[i])
            i += 1

        return ''.join(ans)
```
