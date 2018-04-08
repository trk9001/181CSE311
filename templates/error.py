# Use ''.format() to fill in the blanks.

from templates.master import *

_errors = [head.format('Error'), header.format(nav_0), '{}', footer]
error = '\n\n'.join(_errors)

if __name__ == '__main__':
    print(error)
