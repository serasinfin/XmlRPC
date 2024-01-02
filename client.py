from xmlrpc.client import ServerProxy


def main():
    s = ServerProxy('http://localhost:15000', allow_none=True)
    s.set('foo', 'bar')
    s.set('spam', [1, 2, 3])
    print(s.keys())
    print(s.get('foo'))
    s.delete('spam')
    print(s.exists('spam'))


if __name__ == '__main__':
    main()
