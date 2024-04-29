allocation=[]

def display(memory, processes):
    print("|-------------------------------------------|")
    print(f"|Memory Block      |      Process Allocated |")
    print("|-------------------------------------------|")
    for i in range(len(memory)):
        if allocation[i] != 0:
            print(f"|{memory[i]}K              |         P{processes.index(allocation[i])}")
        if allocation[i] == 0:
            print(f"|{memory[i]}K              |         Not allocated")
        print("|-------------------------------------------|")
    not_allocated = []
    for i in range(len(processes)):
        if processes[i] not in allocation:
            not_allocated.append(processes[i])
    if len(not_allocated) == 0:
        print("\nAll processes are allocatd a memory block.")
    else:
        print("\nThe following processes weren't allocated a memory block:")
        for na in not_allocated:
            print(f"=>P{processes.index(na)} ({na}K)")
    utilization = sum(allocation)/sum(memory)
    print(f"\nMemory utilization: {utilization}%")

def first_fit(memory, processes):   
    visited=[]
    print("\nFirstFit:")
    for process in processes:
        index = 0
        for block in memory:
            if process<=block and index not in visited:
                allocation[index] = process
                visited.append(index)
                break
            else:
                index += 1
    display(memory, processes)

def worst_fit(memory, processes):
    visited=[]
    for process in processes:
        index = 0
        insert_point = -1
        max_diff = 0
        for block in memory:
            if process<=block and index not in visited:
                diff = block - process
                if diff>max_diff:
                    max_diff = diff
                    insert_point = index
            index += 1
        if insert_point != -1:
            allocation[insert_point] = process
            visited.append(insert_point)
    display(memory, processes)

def best_fit(memory, processes):
    visited=[]
    for process in processes:
        index = 0
        insert_point = -1
        min_diff =99999999
        for block in memory:
            if process<=block and index not in visited:
                diff = block - process
                if diff<min_diff:
                    min_diff = diff
                    insert_point = index
            index += 1
        if insert_point != -1:
            allocation[insert_point] = process
            visited.append(insert_point)
    display(memory, processes)

if __name__ == '__main__':
    print("Vineet Shenvi     60004220012")
    memory=[]
    processes=[]
    stop=0

    print("Enter memory blocks\n(-1 to quit)")
    while stop!=1:
        mem = int(input())
        if mem == -1:
            stop = 1
        else:
            memory.append(mem)
    print(memory)

    stop=0
    print("Enter processes:\n(-1 to quit)")
    while stop!=1:
        proc = int(input())
        if proc == -1:
            stop = 1
        else:
            processes.append(proc)

    ch=0
    while ch!=4:
        for block in memory:
            allocation.append(0)

        ch = int(input("Which fit do you want?\n1. First Fit\t2. Worst Fit\t3. Best Fit\t4.Exit\n"))
        if ch == 1:
            first_fit(memory, processes)
        if ch == 2:
            worst_fit(memory, processes)
        if ch == 3:
            best_fit(memory, processes)
        if ch == 4:
            print("Program has ended.")

    



    