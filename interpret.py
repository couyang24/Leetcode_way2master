from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union

commands1 = "G()(al)"
commands2 = "G()()()()(al)"
commands3 = "(al)G(al)()()G"
commands_lst = [commands1, commands2, commands3]


class Solution:
    def interpret(self, command: str) -> str:
        clst = command.split("()")
        tcommand = "o".join(clst)
        clst2 = tcommand.split("(al)")
        return "al".join(clst2)

rprint(Solution().interpret, commands_lst)
