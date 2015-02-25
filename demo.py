# -*- coding: utf-8 -*-
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
from extractor import Extractor

__author__ = 'Modulus'

if __name__ == '__main__':

    datum = []
    with ThreadPoolExecutor(max_workers=16) as executor:
        tasks = {executor.submit(Extractor.extract, start, start + 10): start for start in range(1, 25)}

        for index, future in enumerate(futures.as_completed(tasks)):
            task = tasks[future]
            try:
                data = future.result()
                datum.append(data)
            except Exception as exc:
                print('%r generated an exception: %s' % (future, exc))
            else:
                print('%r page is %d bytes' % (future, len(data)))

    for data in datum:
        print(data)

