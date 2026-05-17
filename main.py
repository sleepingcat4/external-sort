import io
def external_sort(n: int, source: open, sink: open, file_opener=open)-> None:
    mergers = []
    while True:
        text = list(source.read(n))
        if not len(text):
            break
        text.sort()
        merge_me = file_opener()
        merge_me.write(''.join(text))
        mergers.append(merge_me)
        merge_me.seek(0)
        
        
    # merge into sink
    stack_tops =  [f.read(1) for f in mergers]
    while stack_tops:
        c = min(stack_tops)
        sink.write(c)
        i = stack_tops.index(c)
        t = mergers[i].read(1)
        if t:
            stack_tops[i] = t 
        else: 
            del stack_tops[i]
            mergers[i].close()
            del mergers[i]
            
def main():
    input_file = io.StringIO('679825341')
    t = list(input_file.read())
    t.sort() 
    expect = ''.join(t)
    print('expect', expect)
    for memory_size in range(1, 12):
        input_file.seek(0)
        output_file = io.StringIO()
        external_sort(memory_size, input_file, output_file, io.StringIO)
        output_file.seek(0)
        assert(output_file.read() == expect)
        print('memory size {} passed'.format(memory_size))

if __name__ == '__main__':
    example = main
    example()

