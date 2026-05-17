import io
import heapq

def external_sort(n: int, source, sink, file_opener=io.StringIO):
    runs = []

    while True:
        chunk = source.read(n)
        if not chunk:
            break

        f = file_opener()
        f.write(''.join(sorted(chunk)))
        f.seek(0)
        runs.append(f)

    heap = []

    for i, f in enumerate(runs):
        c = f.read(1)
        if c:
            heap.append((c, i))

    heapq.heapify(heap)

    while heap:
        c, i = heapq.heappop(heap)
        sink.write(c)

        nxt = runs[i].read(1)
        if nxt:
            heapq.heappush(heap, (nxt, i))
        else:
            runs[i].close()
