# (shebang line)
# I created a script that will add a space after a comma with Regex.
# The parsed information from my resume on an application tracking system removed all white spaces. Rather than
# adding a space after each comma manually, I created a script that did so from parsed information that is copied to
# the clipboard and returns an aesthetically pleasing result back to the clipboard.

import re
import sys
import pyperclip

if len(sys.argv) < 1:
    sys.exit()

make_space = pyperclip.paste()  # Grabs text from clipboard
print(make_space)
make_space = re.sub(r'(?<=[.,])(?=[^\s])', r' ', make_space)
pyperclip.copy(make_space)
print(make_space)
