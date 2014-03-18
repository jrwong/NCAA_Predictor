def findTie( tourneyteams ):
    """ Takes in rankings from filename(.csv) and returns list of schools
        and their ranks for the year tourneyteams(string, .csv)
        for category cat.
        this python file requires a list of tournament teams from each year 
        (surprisingly hard to find in a good format), 
        and the statistics for each year for each category 
        (found at http://www.ncaa.com/stats/basketball-men/d1)
    """
    import csv
    import sys
    import collections


    d = collections.OrderedDict()

    d["team"] = []
    with open(tourneyteams, 'rb') as g: #this creates a dictionary of the teams
        reader1 = csv.reader(g)
        for row in reader1:
            d[row[0]] = []

    catcounter = 0
    new = True
    while new:
        filename = str(raw_input("What file do you want to enter? (.csv only):"))
        cat = str(raw_input("What category is this for?"))

        
        d["team"] += [str(cat)]
        with open(filename,'rb') as f:  # This opens the csv file to take the rankings
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 3 and row[0] != 'Rank' and row[0] != 'NR' and row[1] in d:
                        if row[0] == '':
                            newrank = raw_input(("tie for", row[1], ". enter rank: "))
                            d[row[1]] += [int(newrank)]
                        else:
                            d[row[1]] += [int(row[0])]

    # this won't put out a perfect list because there are slight differences
    # (such as St. instead of State) so I will try to account for all of them
    # and then if there are still ones missing i'll eventually have a manual entry
            for x in d:
                if len(d[x]) == catcounter:
                    print x, "has a problem"
                    newstat = raw_input("enter in the rank for that team: ")
                    d[x] += [int(newstat)]

        catcounter += 1
        print d["team"]
        for x in d:
            print (x), ":", d[x]

        new = raw_input ("Do you want to enter in another stat? y/n :")

        if new == 'n':
            new = False
        elif new == 'y':
            new = True

    transfer = raw_input("Would you like to transfer to a csv file? y/n: ")
    if transfer == 'y':
        ofile = open("yearlyrankings.csv",'wb')
        writer = csv.writer(ofile)
#        writer.writerow(["team", d["team"][0], d[row][1]])
        for row in d:
            writer.writerow([row, d[row][0], d[row][1]])

        ofile.close()
        print "transfer complete. change name for csv (yearlyrankings.csv)"
        print "to preferred name"



        


