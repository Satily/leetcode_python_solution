class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def flatten_interval(interval):
    if isinstance(interval, Interval):
        return "Interval(start = %d, end = %d)" % (interval.start, interval.end)
    if interval is None:
        return None
    raise RuntimeError("Unsupported type. %s." % interval)
