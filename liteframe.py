from collections import OrderedDict


class DataFrameLite(object):
    def __init__(self, data=None, index=None, columns=None):
        if isinstance(data, OrderedDict):
            data = data
        elif isinstance(data, dict):
            data = OrderedDict(data)
        else:
            data = data
        self._data = data
        self.index = index
        self.columns = columns
        self.at = _AtIndexer(self)

    @classmethod
    def from_dict(cls, data):
        len_max = max([len(v) for v in data.values()])
        index = list(range(0, len_max))
        columns = data.keys()
        data = OrderedDict({k: v + ['nan']*(len_max-len(v)) for k, v in data.items()})
        return cls(data=data, index=index, columns=columns)

    def _get_value(self, row, col):
        return self._data[col][row]

    def _set_value(self, row, col, value):
        self._data[col][row] = value


class _AtIndexer(object):
    def __init__(self, frame):
        self.frame = frame

    def __getitem__(self, key):
        if isinstance(key, tuple):
            row = key[0]
            col = key[1]

            value = self.frame._get_value(row, col)
        else:
            raise ValueError('Invalid call for at access (getting)!')

        return value




if __name__ == '__main__':
    dfl = DataFrameLite.from_dict({'b': [0, 1, 2], 'a': [2, 3]})
    tmp = dfl.at[0, 'b']
    print(tmp)
