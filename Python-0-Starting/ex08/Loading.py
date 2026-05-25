import os
from time import thread_time
from time import strftime
from time import strptime


def ft_tqdm(lst: range) -> None:
    print("%3d%%| [" % (int(lst[0]) / int(lst[1]) * 100), end="")
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        percent = int(i / total * 100)
        barSize = os.get_terminal_size().columns - 41
        bar = "=" * int(i / total * barSize) + ">"
        print(f"\r{percent:3d}%|{bar:<{barSize}}| {i}/{total} \
            [{strftime("%M:%S", thread_time())}<00:00, 164.49it/s]", end="")
        yield item
