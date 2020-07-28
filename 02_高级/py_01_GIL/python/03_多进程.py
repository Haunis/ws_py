#! /usr/bin/python3

"""
多进程无GIL锁，可充分发挥多核cpu的优势
"""
import multiprocessing 

def dead_loop():
    while True:
        pass

def main():
    p = multiprocessing.Process(target=dead_loop)
    p.start()

    while True:
        pass

if __name__ == "__main__":
    main()
