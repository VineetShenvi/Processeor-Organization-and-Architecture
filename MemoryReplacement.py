def display(history, pages, nFrames, nHits):
    print("---------------------------------------\n")
    print("Pages ->", end="")
    for page in pages:
        print(f"     {page}", end="")
    for frame in range(nFrames):
        print(f"\nFrame {frame+1} ", end="")
        for state in history:
            print(f"     {state[frame]}", end="")
    print("\n\n---------------------------------------\n")
    print(f"Number of hits : {nHits}")
    print(f"Number of misses : {len(pages) - nHits}")
    print(f"Hit percentage : {nHits/len(pages)}")


def fifo(nFrames, pages):
    currentState = []
    queue = []
    history = []
    hIndex = 0
    index = 0
    nHits = 0
    for i in range(nFrames):
        currentState.append("-")
    for page in pages:
        if len(queue) == nFrames:
            if page not in currentState:
                queue.append(page)
                currentState[currentState.index(queue[0])] = page
                queue.remove(queue[0])
            else:
                nHits += 1
        if len(queue) != nFrames:
            if page not in currentState:
                queue.append(page)
                currentState.remove(currentState[nFrames-1])
                currentState.insert(index, page)
                index += 1
            else:
                nHits += 1
        history.append([])
        for frame in currentState:
            history[hIndex].append(frame)
        hIndex += 1
    display(history, pages, nFrames, nHits)

def lru(nFrames, pages):
    currentState = []
    queue = []
    history = []
    hIndex = 0
    index = 0
    nHits = 0
    for i in range(nFrames):
        currentState.append("-")
    for page in pages:
        if len(queue) == nFrames:
            if page not in currentState:
                queue.append(page)
                currentState[currentState.index(queue[0])] = page
                queue.remove(queue[0])
            else:
                nHits += 1
                queue.remove(page)
                queue.append(page)
        if len(queue) != nFrames:
            if page not in currentState:
                queue.append(page)
                currentState.remove(currentState[nFrames-1])
                currentState.insert(index, page)
                index += 1
            else:
                nHits += 1
                queue.remove(page)
                queue.append(page)
        history.append([])
        for frame in currentState:
            history[hIndex].append(frame)
        hIndex += 1
    display(history, pages, nFrames, nHits)

def optimal(nFrames, pages):
    currentState = []
    queue = []
    history = []
    hIndex = 0
    pIndex = 0
    index = 0
    nHits = 0
    for i in range(nFrames):
        currentState.append("-")
    for page in pages:
        if len(queue) == nFrames:
            if page not in currentState:
                checker = []
                for i in range(pIndex+1, len(pages)):
                    if pages[i] in queue and pages[i] not in checker:
                        checker.append(pages[i])
                    if len(checker) == nFrames-1:
                        break
                for removal in queue:
                    if removal not in checker:
                        currentState[currentState.index(removal)] = page
                        queue.append(page)
                        queue.remove(removal)
                        break
                        
            else:
                nHits += 1
        if len(queue) != nFrames:
            if page not in currentState:
                queue.append(page)
                currentState.remove(currentState[nFrames-1])
                currentState.insert(index, page)
                index += 1
            else:
                nHits += 1
        history.append([])
        for frame in currentState:
            history[hIndex].append(frame)
        hIndex += 1
        pIndex += 1
    display(history, pages, nFrames, nHits)


    


if __name__ == '__main__':
    print("Vineet Shenvi     60004220012")
    pages=[]
    frames = []
    stop=0

    print("Enter pages:\n(-1 to quit)")
    while 1:
        page = int(input())
        if page == -1:
            break
        else:
            pages.append(page)
    # pages=[6,7,8,9,6,7,1,6,7,8,9,1]

    nFrames = int(input("Enter number of frames: "))

    ch = int(input("Which paging technique do you want?\n1. FIFO\t2. LRU\t3. Optimal\n"))
    if ch == 1:
        print("\nFIFO")
        fifo(nFrames, pages)
    if ch == 2:
        print("\nLRU")
        lru(nFrames, pages)
    if ch == 3:
        print("\nOptimal")
        optimal(nFrames, pages)
        

    # print("\n\n####################################\n")
    # print("FIFO")
    # fifo(nFrames, pages)
    # print("\n\n####################################\n")
    # print("LRU")
    # lru(nFrames, pages)
    # print("\n\n####################################\n")
    # print("Optimal")
    # optimal(nFrames, pages)
