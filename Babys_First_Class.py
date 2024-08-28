'''
Make a class AgendaItem for which each instance exists of:
1. A string (description) of the AgendaItem
2. A starting time.
3. A duration

To this end create a:
Constructor that sets the above attributes
A method to updates/sets the attributes
Asserts so that duration > 0
A version with attribute of duration (_duur) and seperately an ending time (_eindtijd)
'''
class AgendaItem:
    def __init__(self, beschr="Een les.", start_t=(9, 0), eind_t=(9, 50)):
        self._beschrijving = beschr
        self.starttijd = start_t
        if isinstance(eind_t, tuple):
            assert start_t[0] <= eind_t[0]
            if start_t[0] == eind_t[0]:
                assert start_t[1] < eind_t[1]
            self._eindtijd = eind_t
        else:
            assert start_t[0] >= 0 and eind_t >= 0
            self._starttijd = start_t
            self._duur = eind_t

    # Simply updates the 'descriptors' of the agenda item (Checks for tuple or int to distinguish between time/duration)
    def update(self, values):
        self._beschrijving = values[0]
        self._starttijd = values[1]
        if isinstance(values[2], tuple):
            self._eindtijd = values[2]
            self._duur = None
        else:
            self._duur = values[2]
            self._eindtijd = None

    def __str__(self):
        if self._duur:  # returns false if duur = None
            return "Beschrijving:\n" + str(self._beschrijving) + "\nDe les start op " + str(
                self._starttijd) + " en duurt " + str(self._duur) + " minuten."
        else:
            return "Beschrijving:\n" + str(self._beschrijving) + "\nDe les start om " + str(
                self._starttijd) + " en eindigt om " + str(self._eindtijd) + "."
            # Return duration or end-time depending on case. Could pretty up the times by adding in a : between.

    def __repr__(self):
        return str(self)


wiskunde = AgendaItem("Een wiskunde les", (10, 30), 45)   # check the case in which I send 'duration"

wiskunde.update(["De wiskunde les", (11, 45), (12, 50)])  # Check case in which I send 'end time'

print(wiskunde) # will call wiskunde.__repr__, which in turn calls wiskunde.__str__
                # Should return description, starting time and either duration or end time
