class DataFrameLite:
    def __init__(self, data=None, index=None, columns=None):
        self.data = data
        self.index = index
        self.columns = columns
        self.at = _AtIndexer(self)

    @classmethod
    def from_dict(cls, data):
        columns = data.keys()
        return cls(data=data, columns=columns)


class _AtIndexer:
    def __init__(self, frame):
        self.frame = frame

    def __getitem__(self, key):
        if isinstance(key, tuple):
            row = key[0]
            col = key[1]

            value = self.frame.data[col][row]
        else:
            raise ValueError('Invalid call for at access (getting)!')

        return value


if __name__ == '__main__':
    dfl = DataFrameLite.from_dict({'a': [0, 1], 'b': [2, 3]})
    tmp = dfl.at[0, 'b']
    print(tmp)
