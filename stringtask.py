def picincitemsprint(itemsdic, lw, rw):
    print('PICNIC ITEMS'.center(lw + rw, '-'))
    for k, v in itemsdic.items():
        print(k.ljust(lw, '.') + str(v).rjust(rw))


picnicitems = {'sandwiches': '2', 'laddu': '4', 'cake': '1'}
picincitemsprint(picnicitems, 12, 8)
picincitemsprint(picnicitems, 20, 16)
