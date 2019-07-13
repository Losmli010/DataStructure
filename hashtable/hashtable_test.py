import time
from hashtable.hashtable import HashTable


def test_func():
    with open('Lorem_ipsum.txt', 'r') as fp:
        words = fp.read().split(' ')

    start = time.time()
    ht = HashTable(100)
    word_count = 0
    for word in words:
        ht.add(str(word_count) + word, word_count)
        word_count += 1
    end = time.time()
    print("HashTable(100) add time:%f\n" % (end - start))
    print(ht.get_distribution())
    print('\n')

    start = time.time()
    ht1 = HashTable(1000)
    word_count = 0
    for word in words:
        ht1.add(str(word_count) + word, word_count)
        word_count += 1
    end = time.time()
    print("HashTable(1000) add time:%f\n" % (end - start))
    print(ht1.get_distribution())
    print('\n')

    start = time.time()
    ht2 = HashTable(150000)
    word_count = 0
    for word in words:
        ht2.add(str(word_count) + word, word_count)
        word_count += 1
    end = time.time()
    print("HashTable(150000) add time:%f\n" % (end - start))
    print(ht2.get_distribution())
    print('\n')

    start = time.time()
    for item in ht2:
        ht2.remove(item.key)
    end = time.time()
    print("remove entry cost time:%f\n" % (end - start))


if __name__ == '__main__':
    test_func()
