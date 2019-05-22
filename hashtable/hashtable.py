class Entry(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, bucket_num):
        if not isinstance(bucket_num, int) or bucket_num < 0:
            raise ValueError("Invaild value of bucket num")

        self.bucket_num = bucket_num
        self.buckets = [None for _ in range(self.bucket_num)]

    def __str__(self):
        string = '{'
        for bucket in self.buckets:
            if bucket is not None:
                for entry in bucket:
                    if isinstance(entry.key, str):
                        string += ("'%s': " % entry.key)
                    else:
                        string += ("%s: " % entry.key)
                    if isinstance(entry.value, str):
                        string += ("'%s', " % entry.value)
                    else:
                        string += ("%s, " % entry.value)
        return string.rstrip(', ') + "}"

    def hash(self, key):
        if not key:
            return -1
        power = 0
        hashing = 0
        for char in key:
            hashing += (ord(char) - 32) * pow(95, power)
            power += 1
        index = hashing % self.bucket_num
        return index

    def add(self, key, value):
        index = self.hash(str(key))
        if index < 0 or index > self.bucket_num:
            return False
        if self.buckets[index] is None:
            self.buckets[index] = [Entry(key, value)]
            return True
        else:
            for entry in self.buckets[index]:
                if entry.key == key:
                    entry.value = value
                    return True
            self.buckets[index].append(Entry(key, value))
            return True

    def update_value(self, key, value):
        index = self.hash(str(key))
        if index is None or self.buckets[index] is None:
            # print("Key Not Found!")
            return False
        else:
            for entry in self.buckets[index]:
                if entry.key == key:
                    entry.value = value
                    return True
            # print("Key Not Found!")
            return False

    def delete(self, key):
        index = self.hash(str(key))
        if index is None or self.buckets[index] is None:
            # print("Key Not Found!")
            return False
        else:
            for entry in self.buckets[index]:
                if entry.key == key:
                    self.buckets[index].remove(entry)
                    return True
            # print("Key Not Found!")
            return False

    def look_up(self, key):
        index = self.hash(str(key))
        if index is None or self.buckets[index] is None:
            # print("Key Not Found!")
            return False
        else:
            for entry in self.buckets[index]:
                if entry.key == key:
                    return entry.value
            # print("Key Not Found!")
            return False

    def print_distribution(self):
        string = ''
        bucket_num = 0
        mins = None
        maxs = 0
        total = 0
        for bucket in self.buckets:
            if bucket is not None:
                # string += ("Bucket Number %d has: "%bucketNum)
                counts = 0
                for entry in bucket:
                    counts += 1
                # string += ("%d entries\n"%count)
                total += counts
                if counts > maxs:
                    maxs = counts
                if mins is None or counts < mins:
                    mins = counts
            else:
                pass
                # string += ("Bucket Number %d has 0 entries\n"%(bucketNum))
            bucket_num += 1
        string += ("Largest Bucket has %d entries\n" \
                   "Smallest Bucket has %d entries\nTotal entries: %d\n" \
                   "Avg bucket size is %f" % (maxs, mins, total, (total / self.bucket_num)))
        return string


if __name__ == '__main__':
    ht = HashTable(100)
    print(ht)

    ht.add('bob', 2)
    ht.add(11, 3)
    ht.add('11', 4)
    ht.add(' ', 5)
    print(ht)
    print(ht.look_up(11))
    print(ht.print_distribution())
