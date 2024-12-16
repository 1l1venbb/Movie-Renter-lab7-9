import math

class Sorts:

    def insertionSort(self, array, key = lambda x: x, reverse = False):
        """
        Insertion Sort.
        :param array: Array to be sorted.
        :param key: Function used as key to sort array.
        :param reverse: Reverse sort.
        """
        for i in range(1, len(array)):
            keyV = key(array[i])
            keyI = array[i]
            j = i - 1
            while j >= 0 and ((keyV < key(array[j])) if not reverse else (keyV > key(array[j]))):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = keyI

        return array

    def combSort(self, array, key = lambda x: x, reverse = False):
        """
        CombSort Sort.
        :param array: Array to be sorted.
        :param key: Function used as key to sort array.
        :param reverse: Reverse sort.
        :return: Sorted array.
        """
        n = len(array)
        gap = n
        isSorted = False

        while not isSorted:
            isSorted = True
            gap = math.floor(gap / 1.3)
            if gap < 1:
                gap = 1

            for i in range(n - gap):
                if reverse:
                    if key(array[i]) < key(array[i + gap]):
                        array[i], array[i + gap] = array[i + gap], array[i]
                        isSorted = False
                else:
                    if key(array[i]) > key(array[i + gap]):
                        array[i], array[i + gap] = array[i + gap], array[i]
                        isSorted = False

        return array