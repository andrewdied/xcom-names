"""Generate XCOM-compatible mission names. Because the lists are from XCOM."""

from collections import namedtuple
import random
from mission_names import xcom_prefixes, xcom_suffixes, xcom2_prefixes, \
    xcom2_suffixes, xcom2_prefix_words, xcom2_suffix_words

Mission = namedtuple('Mission', 'prefix suffix')
xcom_missions = Mission(xcom_prefixes, xcom_suffixes)
xcom2_missions = Mission(xcom2_prefixes, xcom2_suffixes)
xcom2_words = Mission(xcom2_prefix_words, xcom2_suffix_words)
test_words = Mission(('first',), ('last',))

mission_groups = (xcom_missions, xcom2_missions, xcom2_words)


def operation(mission_group=random.choice(mission_groups)):
    """Return a tuple of (prefix, suffix) given a namedtuple that has tuples
    of prefixes (.prefix) and suffixes (.suffix)."""
    while True:
        (prefix, suffix) = (random.choice(mission_group.prefix),
                            random.choice(mission_group.suffix))
        if prefix != suffix: # some groups have duplicate words
            return prefix, suffix


if __name__ == '__main__':
    prefix, suffix = operation()
    print(f'Operation {prefix.upper()} {suffix.upper()}')
