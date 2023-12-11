from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._query))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._query))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._query))

    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))

    def build(self):
        return self._query
