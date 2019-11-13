# Hammurabi, by Al Sweigart al@inventwithpython.com
# The classic BASIC game Hamurabi.bas by Doug Dyment, popularized by David Ahl.

import random

def main():
    print('HAMMURABI by Doug Dyment and others')
    print('Try your hand at governing ancient Sumeria for a ten-year term of office.')
    print()
    print("""Game mechanics:
- The game is played over 10 years, each turn is one year.
- You start with 100 people, 1000 acres, and 3000 bushels of grain.
- Each year has 3 phases: buy/sell land, feed population, and plant grain.
- Land trades between 17 and 26 bushels per acre. The price changes each year.
- 20 bushels feeds 1 person.
- 2 bushels are used to plant 1 acre, 1 person can plant 10 acres.
- Next years' harvest is (acres plantd * random number 1 to 5)
- Each year has a 15%% chance of plague that kills half the population.
- If more 45%% of the people starve in a single year, you instantly lose.

Best ending:     <=3%% population died and >10 acres per person.
Mediocre ending: >3% to 10%% population died or >9 to 10 acres per person.
Bad ending:      >10% to 33%% population died or >7 to 9 acres per person.
Worst ending:    >33%% population died or <7 acres per person.""")
    print()



    year = 1
    deaths = 0
    births = 5
    population = 95
    acresOwned = 1000
    acresToPlant = 1000
    bushelsStored = 2800
    bushelsHarvestedPerAcre = 3
    ratsAte = 200
    totalDeaths = 0
    totalPopulation = population
    percentageDiedEachYear = []

    while True:
        print()
        print(f'Hammurabi, I beg to report to you, in the year {year}:')
        print(f'- {deaths} people starved')
        print(f'- {births} came to the city')
        print()
        population += births
        totalPopulation += births

        if random.randint(0, 99) <= 15:
            print('*** A HORRIBLE PLAGUE STRUCK! HALF THE PEOPLE DIED. ***')
            print()
            population //= 2 # Halve the population.

        print(f'  Population: {population} people')
        print(f'        Land: {acresOwned} acres ({acresOwned // population} per person)')
        print(f'     Harvest: {bushelsHarvestedPerAcre} bushels per acres, {bushelsHarvestedPerAcre * acresToPlant} total')
        print(f'    Rats ate: {ratsAte} bushels')
        print(f'Grain stored: {bushelsStored} bushels in store.')
        print()

        if year > 10: # End game after year 10.
             break

        print('Phases: BUY/SELL LAND => FEED POPULATION => PLANT CROPS')
        print()

        # Buying and selling land:
        landPricePerAcre = random.randint(17, 26)
        print(f'Land trades between 17 & 26 bushels per acre. Current price: {landPricePerAcre}')

        while True:
            print(f'How many acres do you wish to buy? (0-{bushelsStored // landPricePerAcre})')
            try:
                acresToBuy = int(input())
            except:
                continue # Player didn't enter a number, ask again.
            if acresToBuy > (bushelsStored // landPricePerAcre) or acresToBuy < 0:
                continue # Ask again.

            bushelsStored -= acresToBuy * landPricePerAcre
            acresOwned += acresToBuy
            print(f'Spent {acresToBuy * landPricePerAcre} bushels to buy {acresToBuy} acres. Current bushels: {bushelsStored} Current land: {acresOwned}')
            break

        if acresToBuy == 0: # Only ask to sell land if they didn't buy land.
            while True:
                print(f'How many acres do you wish to sell? (0-{acresOwned})')
                try:
                    acresToSell = int(input())
                except:
                    continue # Player didn't enter a number, ask again.
                if acresToSell < 0 or acresToSell > acresOwned:
                    continue # Ask again.

                bushelsStored += acresToSell * landPricePerAcre
                acresOwned -= acresToSell
                print(f'Sold {acresToSell} acres for {acresToSell * landPricePerAcre} bushels. Current bushels: {bushelsStored} Current land: {acresOwned}')
                break

        # Feed population.
        while True:
            maxToFeed = min(bushelsStored, population * 20)
            print(f'20 bushels feeds 1 person: How many bushels do you wish to feed your people? (0-{maxToFeed})')
            try:
                bushelsToFeed = int(input())
            except:
                continue # Player didn't enter a number, ask again.
            if bushelsToFeed > maxToFeed or bushelsToFeed < 0:
                continue # Ask again.

            bushelsStored -= bushelsToFeed
            print(f'Fed {bushelsToFeed // 20} people with {bushelsToFeed} bushels. Current bushels: {bushelsStored}')
            break

        # Plant seeds.
        while True:
            maxCanPlant = min(acresOwned, bushelsStored // 2, population * 10)
            print(f'2 bushels to plant 1 acre, 1 person can plant 10 acres: How many acres do you wish to plant with seed? (0-{maxCanPlant})')
            try:
                acresToPlant = int(input())
            except:
                continue # Player didn't enter a number, ask again.
            if acresToPlant > maxCanPlant or acresToPlant < 0:
                continue # Ask again.

            bushelsStored -= acresToPlant * 2
            print(f'Planted {acresToPlant} acres using {acresToPlant * 2} bushels. Current bushels: {bushelsStored}')
            break

        # Calculate harvest:
        bushelsHarvestedPerAcre = random.randint(1, 5)
        bushelsHarvested = acresToPlant * bushelsHarvestedPerAcre


        # Chance for rats running wild:
        if random.randint(0, 99) <= 40:
            ratsAte = int(bushelsStored / random.randint(1, 5))
        else:
            ratsAte = 0

        bushelsStored += bushelsHarvested - ratsAte

        # Calculate births:
        births = int(random.randint(1, 5) * (20 * acresOwned + bushelsStored) / population / 100 + 1)

        # Calculate how many people starved:
        deaths = population - (bushelsToFeed // 20)
        percentageDiedEachYear.append(int(deaths / population * 100))
        totalDeaths += deaths

        if deaths > (0.45 * population):
            print(f'You starved {deaths} people in one year!!!')
            print('Due to this extreme mismanagement you have not only')
            print('been impeached and thrown out of office but you have')
            print('also been declared a national fink!!!!')
            return # Game over.


        population -= deaths # Update population.
        year += 1

    # Tell the player how they did:
    percentageDiedPerYear = sum(percentageDiedEachYear) // 10 # TODO This is wrong and needs to be corrected. Get the percentage deaths each year, and find the average of that. See original source.
    acresPerPerson = acresOwned // population
    print(f'In your 10-year term of office, {percentageDiedPerYear} percent of the')
    print('population starved per year on the average, i.e. a total of')
    print(f'{totalDeaths} out of {totalPopulation} people died!!')
    print('You started with 10 acres per person and ended with')
    print(f'{acresPerPerson} acres per person.')
    print()



    if percentageDiedPerYear > 33 or acresPerPerson < 7:
        print('Due to this extreme mismanagement you have not only')
        print('been impeached and thrown out of office but you have')
        print('also been declared a national fink!!!!')
        return

    elif percentageDiedPerYear > 10 or acresPerPerson < 9:
        print('Your heavy-handed performance smacks of Nero and Ivan IV.')
        print('The people (remaining) find you an unpleasant ruler, and,')
        print('frankly, hate your guts!!')
        return

    elif percentageDiedPerYear > 3 or acresPerPerson < 10:
        print('Your performance could have been somewhat better, but')
        print(f'really wasn\'t too bad at all. {random.randint(0, int(population * 0.8))} people')
        print('would dearly like to see you assassinated but we all have our')
        print('trivial problems.')

    else:
        print('A fantastic performance!!! Mandela, Elizabeth II, and')
        print('Annan combined could not have done better!')


    print()
    print('So long for now.')

if __name__ == '__main__':
    main()
