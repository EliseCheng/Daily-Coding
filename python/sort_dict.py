n = [(u'br0', [468, 16370752, 0, 0]), (u'br1', [84331608465, 1543023710753, 2003, 1425197]), (u'br100', [769306, 1651124, 0, 1642790]), (u'eth0', [87735498809, 1543682815253, 87734729503, 1543681164129]), (u'eth1', [769774, 1651262, 0, 0]), (u'eth2', [0, 0, 0, 0]), (u'eth3', [14795620, 14329401, 14795620, 14329401]), (u'eth4', [0, 0, 0, 0]), (u'lo', [27092370869, 27092370869, 0, 0]), (u'ovs-system', [0, 0, 0, 0]), (u'vcontr-b81e13bb', [288325646927, 818460, 1424455, 0]), (u'vdata-0aec0b65', [2346900, 7992, 0, 0]), (u'vdata-3f7466a0', [2346964, 10728, 0, 0]), (u'vdata-548d07c9', [2346964, 9360, 0, 0]), (u'vdata-6931edd2', [2900948, 468, 0, 0]), (u'vdata-edb26beb', [3407771, 468, 1060807, 0]), (u'vdata-effd85cb', [2900948, 8334, 0, 7866]), (u'vgate-6931edd2', [288372063038, 2018410, 1424455, 0]), (u'vgate-edb26beb', [288413963145, 2155092, 288399167525, 0]), (u'virbr0', [0, 0, 0, 0])]

def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    a = {}
    for key, value  in items:
        a[key] = value
    return a

print sortedDictValues1(dict(n))
