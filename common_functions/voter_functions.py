from typing import Tuple, List

def confidential_voter(fields: List[str]) -> Tuple[str]:
    """
    Determines if a voter is marked as confidential.

    Args:
    fields (List[str]): List containing voter data, where fields[0] is expected to be the confidentiality flag.

    Returns:
    Tuple[str]: A tuple containing 'YES' if the voter is confidential, otherwise 'NO'.
    """
    if not fields or len(fields) < 1:
        return ('NO',)

    confidential = ('YES',) if 'XX' in fields[0] else ('NO',)
    return confidential

from typing import List

def confidential_address(fields: List[str]) -> str:
    """
    Returns 'YES' if the voter's address is confidential, otherwise 'NO'.

    Args:
    fields (List[str]): List containing voter data, where fields[0] is the confidentiality flag.

    Returns:
    str: 'YES' if the address is confidential, otherwise 'NO'.
    """
    if not fields or len(fields) < 1:
        return 'NO'

    return 'YES' if 'XX' in fields[0] else 'NO'
