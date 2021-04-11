from typing import Iterator

class Discoverable:
    """ Minimal plugin class. Allows the user to iterate over the child     
        classes.
    """
    @property
    def childClasses(self) -> Iterator[type]:
        openlist = [self.__class__]
        closedlist = set()
        while openlist:
            cur = openlist.pop()
            yield cur
            closedlist.add(cur)

            openlist += [s for s in cur.__subclasses__() if s not in closedlist]