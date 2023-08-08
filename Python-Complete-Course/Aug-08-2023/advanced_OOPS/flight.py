from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        stops = [self.segments[0].departure,self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)
        return '->'.join(stops)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, value):
        self.segments[0].departure = value


flight = Flight([Segment('GLA', 'LHR')])
print(flight.departure_point)

flight.departure_point = "EDI"

print(flight.departure_point)