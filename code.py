def minDifference(array, k):

    # Set the result to maximum value
    result = float('inf')

    # Length of the array
    n = len(array)
    minIndex = 0
    
    # Sort the array
    array.sort()
    
    # Find the minimum difference between the first and last element
    for i in range(n - k + 1):
        if (array[i+k-1] - array[i]) < result:
            result = array[i+k-1] - array[i]
            minIndex = i
  
    return result, minIndex


if __name__ == '__main__':
    price = dict()

    # Open the input file
    with open('input3.txt', 'r') as f:

        # Number of employees
        k = int(f.readline().split(':')[1])

        # Store the price of goodies in a dictionary
        for line in f.readlines()[3:]:
            price[str(line.split(':')[0])] = int(line.split(':')[1])
    
    # Sort the dictionary
    price = dict(sorted(price.items(), key=lambda item: item[1]))
    
    # Get the result
    result, index = minDifference(list(price.values()), k)

    # Write the result to the output file
    with open("output3.txt", 'w', encoding = 'utf-8') as f:
        f.write("The goodies selected for distribution are:\n\n")

        for i in range(k):
            f.write(list(price.keys())[index+i] + ": ")
            f.write(str(price[list(price.keys())[index+i]]) + "\n")
    
        f.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is " + str(result))
