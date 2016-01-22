import hashlib


def chunkiter(fp, chunk_size=65536):
    """
    Return an iterator to a file-like obj which yields fixed size chunks
    :param fp: a file-like object
    :param chunk_size: maximum size of chunk
    """
    while True:
        chunk = fp.read(chunk_size)
        if chunk:
            yield chunk
        else:
            break


def chunkreadable(iter, chunk_size=65536):
    """
    Wrap a readable iterator with a reader yielding chunks of
    a preferred size, otherwise leave iterator unchanged.
    :param iter: an iter which may also be readable
    :param chunk_size: maximum size of chunk
    """
    return chunkiter(iter, chunk_size) if hasattr(iter, 'read') else iter


def test():
    checksum = hashlib.md5()
    download_file = open('/home/chengwen/Downloads/shadowsocks-nightly-2.9.4.apk', 'rb')
    for buf in chunkreadable(download_file, 4096):
        checksum.update(buf)
    print checksum.hexdigest()

if __name__ == '__main__':
    test()
