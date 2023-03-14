from time import time, sleep

def ft_progress(lst):
    """
    A generator function that displays the progress of a for loop using yield.
    """
    start_time = time()
    for i,elem in enumerate(lst):
        yield elem
        progress = (i + 1) / len(lst)
        elapsed_time = time() - start_time
        eta = elapsed_time / progress - elapsed_time
        print(f"ETA: {eta:.2f}s ", end="")
        print(f"[{int(progress * 100)}%]", end="")
        print(f"[{'=' * int(progress * 20)}>{' ' * (19 - int(progress * 20))}] ", end="")
        print(f"{i + 1}/{len(lst)} ", end="")
        print(f"| elapsed time {elapsed_time:.2f}s", end="\r")
        if progress == 1:
            print("")
            print("...", end="")

if __name__ == "__main__":
	listy = range(3333) 
	ret = 0
	for elem in ft_progress(listy):
		ret += elem
		sleep(0.005)
	print()
	print(ret)
