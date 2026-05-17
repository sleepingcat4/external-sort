import heapq
import tempfile
import os

def external_sort(n: int, source_path: str, sink_path: str):
    runs = []

    with open(source_path, "r", encoding="utf-8") as source:
        while True:
            chunk = source.read(n)
            if not chunk:
                break

            tmp = tempfile.NamedTemporaryFile(delete=False, mode="w+", encoding="utf-8")
            tmp.write("".join(sorted(chunk)))
            tmp.flush()
            tmp.seek(0)
            runs.append(tmp)

    heap = []

    for i, f in enumerate(runs):
        c = f.read(1)
        if c:
            heap.append((c, i))

    heapq.heapify(heap)

    with open(sink_path, "w", encoding="utf-8") as sink:
        while heap:
            c, i = heapq.heappop(heap)
            sink.write(c)

            nxt = runs[i].read(1)
            if nxt:
                heapq.heappush(heap, (nxt, i))
            else:
                runs[i].close()
                os.unlink(runs[i].name)

    for f in runs:
        if not f.closed:
            f.close()
            os.unlink(f.name)
