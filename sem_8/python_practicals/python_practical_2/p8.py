''' Please write a program to print the running time of execution of "1+1" for 100
times.'''
import timeit

def main():
    start_time = timeit.default_timer()
    for i in range(0,100):
        1 + 1
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("start_time :", start_time)
    print("end_time: ", end_time)
    print(execution_time)

if __name__ == "__main__" :
    main()
