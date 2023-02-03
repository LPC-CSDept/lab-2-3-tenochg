def main():
    ##################################################
    # Comlete your code here
    ##################################################
    val1 = int(input('First Integer value:'))
    val2 = int(input('Second Integer value:'))
    val3 = int(input('Third Integer value:'))
    sum = val1 + + val2 + val3
    avg = sum/3

    print(f'Values: {val1} {val2} {val3}')
    print(f'Total: {sum}')
    print(f'Average: {avg:.2f}')

    pass


if __name__ == '__main__':
    main()
