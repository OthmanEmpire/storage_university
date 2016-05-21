# Some simple examples of formatted output - compare with
# the equivalent Java code in Formatting.java
# (NDE, 2011-08-12)

from math import pi

print("Default: {:f}".format(pi))
print("8 dp: {:.8f}".format(pi))
print("4 dp: {:.4f}".format(pi))
print("2 dp, six-char field: |{:6.2f}|".format(pi))
print("5 dp, ten-char field: |{:10.5f}|".format(pi))
