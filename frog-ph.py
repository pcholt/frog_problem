# Paul Holt
# pcholt@gmail.com
# hereby committed to the PUBLIC DOMAIN
    
def _crossing_hop_count(hops_remaining):
    count = 0
    while hops_remaining > 0:
        hops_remaining -= random.randrange(1,hops_remaining+1)
        count += 1
    return count

def crossing_histogram(pond_size, samples):
    hist = [0 for i in xrange(pond_size+1)]
    for i in xrange(samples):
        hist[_crossing_hop_count(pond_size)] += 1
    return hist

def average(samples=10**5, pond_size=3):
    histogram = crossing_histogram(pond_size,samples)
    total = 0
    for hop_count, occurrences in enumerate(histogram):
        total += hop_count * occurrences
    return (total/float(samples), histogram)

def main():
    for pond_size in xrange(200):
        print pond_size, average(pond_size=pond_size)

if __name__ == '__main__':
    main()