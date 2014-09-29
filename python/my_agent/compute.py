url = '192.168.5.120:9292'
path = '/var/lib/libvirt/images'

vm_type = {'controller': 0, 'gateway': 1, 'slice_vm': 2}

class Image(object):

    def __init__(self, uuid):
        self.uuid = uuid
        print 'fetch %s from %s, place it on %s' % (uuid, url, path)

    def __repr__(self):
        return self.uuid
        



class VirtualMachine(object):
    def __init__(self, name, image_uuid, vm_type):
        self.name = name
        self.image = Image(image_uuid)
        self.vm_type = vm_type
    
    def create(self):
        print '-----------create---------------'
        print 'based on image %s' % self.image
        print 'name %s' % self.name
        self.config_network()

    def config_network(self):
        print 'do proper network config'
        if self.vm_type == 0:
            pass
        elif self.vm_type == 1:
            pass
        else:
            pass


def create_slicevm(name, uuid):
    vm = VirtualMachine(name, uuid, vm_type('slice_vm'))
    vm.create()

def create_controller(name, uuid):
    vm = VirtualMachine(name, uuid, vm_type('controller'))
    vm.create()
    
if __name__ == '__main__':
    create_slicevm('slice_vm', 'uuid_123')
    create_controller('ctrl1', 'uuid_234')
