# Function to find the complement (reverse) of a genome strand
def reverse_pattern(pattern:str) -> str:
    base = 'ATCG'
    base_pair = 'TAGC'
    base_length = len(base)
    
    reverse = ''
    
    # Loop to complement each char in the pattern
    for c in pattern:
        for i in range(base_length):
            if c == base[i]:
                reverse = base_pair[i] + reverse # A -> BA -> CBA
    
    return reverse

# Function to find how many times a pattern appear in a genome
def count_k_mer(genome:str, pattern:str) -> int:
    pattern_complement = reverse_pattern(pattern)
    pattern_length = len(pattern)
    
    seen = ''
    num_appear = 0

    # Loop to check if each possible pattern (same len as pattern) is identical w/ pattern
    for c in genome:
        seen += c
        if len(seen) == pattern_length:
            if seen == pattern or seen == pattern_complement:
                num_appear += 1
            seen = seen[1:pattern_length] # Delete the first char
    
    return num_appear

# Function to find the most frequent patterns in a genome
def frequent_k_mer(genome:str, k:int) -> list:
    patterns = []
    
    # Store all the appearing patterns of length k & its frequency in the genome 
    seen = ''
    for c in genome:
        seen += c
        if len(seen) == k:
            if not seen in patterns:
                patterns.append([seen, count_k_mer(genome, seen)])
            seen = seen[1:k]

    # Find the max frequency value
    max_frequency = 0
    for p in patterns:
        if p[1] > max_frequency:
            max_frequency = p[1]

    # List the patterns that has the max frequency value
    most_frequents = []
    for p in patterns:
        if p[1] == max_frequency and p[0] not in most_frequents:
            most_frequents.append(p[0])

    return most_frequents

# Main program
if __name__ == '__main__':

    # Input genome file and reject invalid file name
    while True:
        try:
            file_genome = open(input('Genome file name: '), 'r')
        except FileNotFoundError:
            print('File not found')
            continue
        break
    
    # User select which function to run
    print('Choose an option:\n'
          '[1] Compute a reverse complement of a k-mer pattern\n'
          '[2] Count a k-mer pattern\n'
          '[3] Find most frequent k-mer patterns\n')
    
    while True:
        try:
            user_selection = input('Select an operation [1/2/3]: ')
            if user_selection not in ['1', '2', '3'] or user_selection == '':
               raise
        except:
            print('Invalid input')
            continue
        break

    # Output 
    if user_selection == '1':
        while True:
            try:
                user_pattern = input('Input your pattern: ')
                if (not all(c in 'ATCG' for c in user_pattern)) or user_pattern == '':
                    raise   
            except:
                print('Invalid pattern')
                continue
            break   

        print(reverse_pattern(user_pattern))

    elif user_selection == '2':
        while True:
            try:
                user_pattern = input('Input your pattern: ')
                if (not all(c in 'ATCG' for c in user_pattern)) or user_pattern == '':
                    raise   
            except:
                print('Invalid pattern')
                continue
            break   

        print(count_k_mer(file_genome.read(), user_pattern))

    elif user_selection == '3':
        while True:
            try:
                user_k = int(input('Input value of k: '))
            except:
                print('Invalid value of k')
                continue
            break
            
        list_most_frequent = frequent_k_mer(file_genome.read(), user_k)
        for pattern in list_most_frequent:
            print(pattern)

    file_genome.close()
