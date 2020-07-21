
import csv
import os
import seaborn as sb
import matplotlib.pyplot as plt

plotX = []
plotY = []

def validationStepPositivesPer100000():
    os.chdir("C:////Users////moose_f8sa3n2////Google Drive////Data Analysis for Project Management////Course Project////Positives Per 100,000")
    with open('CountyCovidDataAll9_scorePositives.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for rows in reader:
            BF1 = max(0, float(rows["WITH_A_DISABILITY_WHITE_PERCENT"]) - 17.79)
            BF2 = max(0, 17.79 - float(rows["WITH_A_DISABILITY_WHITE_PERCENT"]))
            BF3 = max(0, float(rows["RENT_PER_MONTH"]) - 1910)
            BF4 = max(0, 1910 - float(rows["RENT_PER_MONTH"]))
            BF6 = max(0, 6.12 - float(rows["TWO_OR_MORE_RACES_MALE_PERCENT"]))
            BF7 = max(0, float(rows["PEOPLE_PER_UNIT"]) - 11.5)
            BF9 = max(0, float(rows["AFRICAN_AMERICAN_MALES_PERCENT"]) - 8.53)
            BF10 = max(0, 8.53 - float(rows["AFRICAN_AMERICAN_MALES_PERCENT"]))
            BF11 = max(0, float(rows["PCT_OVERHOUSED"]) - 0.93)
            BF12 = max(0, 0.93 - float(rows["PCT_OVERHOUSED"]))
            BF14 = max(0, 253 - float(rows["TPCT_OWNSFD"]))
            BF15 = max(0, float(rows["ARTS_ENTERTAINMENT_AND_RECREATION_AND_ACCOMMODATION_PERCENT"]) - 3.6)

            ValCalc = 88.7757 + 251.681 * BF1 + 16.6504 * BF2 + 0.935702 * BF3\
                 - 0.176406 * BF4 + 64.4226 * BF6 - 142.258 * BF7\
                 + 4.12785 * BF9 - 40.4765 * BF10 + 824.754 * BF11\
                 + 370.482 * BF12 + 2.5115 * BF14 - 19.7121 * BF15

            yield round(float(rows["RESPONSE"]),3),round(ValCalc,3)

def validationStepDeathsPer100000():
    os.chdir("C:////Users////moose_f8sa3n2////Google Drive////Data Analysis for Project Management////Course Project////Deaths Per 100,000")
    with open('CountyCovidDataAll9_scoreDeaths.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for rows in reader:
            BF1 = max(0, float(rows["WITH_A_DISABILITY_WHITE_PERCENT"]) - 17.79)
            BF2 = max(0, 17.79 - float(rows["WITH_A_DISABILITY_WHITE_PERCENT"]))
            BF3 = max(0, float(rows["RENT_PER_MONTH"]) - 1774)
            BF5 = max(0, float(rows["PEOPLE_PER_UNIT"]) - 9.8)
            BF6 = max(0, 9.8 - float(rows["PEOPLE_PER_UNIT"]))
            BF7 = max(0, float(rows["AMERICAN_INDIAN_FEMALE_PERCENT"]) - 2.07)
            BF8 = max(0, 2.07 - float(rows["AMERICAN_INDIAN_FEMALE_PERCENT"]))
            BF9 = max(0, float(rows["PCT_OVERHOUSED"]) - 1.02)
            BF10 = max(0, 1.02 - float(rows["PCT_OVERHOUSED"]))
            BF11 = max(0, float(rows["FEMALE_TOTAL_POPULATION_85_YEARS_AND_OVER_PERCENT"]) - 4.4)
            BF12 = max(0, 4.4 - float(rows["FEMALE_TOTAL_POPULATION_85_YEARS_AND_OVER_PERCENT"]))
            BF13 = max(0, float(rows["TWO_OR_MORE_RACES_MALE_PERCENT"]) - 4.67)
            BF14 = max(0, 4.67 - float(rows["TWO_OR_MORE_RACES_MALE_PERCENT"]))
            BF15 = max(0, float(rows["NCHS_CODE"]) - 1)

            ValCalc = 9.42304 + 8.27823 * BF1 + 0.586005 * BF2 + 0.062297 * BF3\
                 - 7.31681 * BF5 + 0.572955 * BF6 + 0.483703 * BF7\
                 - 7.05329 * BF8 + 82.0343 * BF9 + 25.6931 * BF10\
                 - 19.0854 * BF11 - 7.66592 * BF12 - 0.729053 * BF13\
                 + 4.05636 * BF14 - 3.16135 * BF15
            
            yield round(float(rows["RESPONSE"]),3),round(ValCalc,3)


def validationStepDeaths():
    os.chdir("C:////Users////moose_f8sa3n2////Google Drive////Data Analysis for Project Management////Week 6")
    with open('scored_Deaths2.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for rows in reader:
             BF1 = max( 0, float(rows["TOTALUNITS"]) - 68184)
             BF3 = max( 0, float(rows["HH_INCOME"]) - 86315)
             BF4 = max( 0, 86315 - float(rows["HH_INCOME"]))
             BF5 = max( 0, float(rows["PEOPLE_PER_UNIT"]) - 10.4)
             BF6 = max( 0, 10.4 - float(rows["PEOPLE_PER_UNIT"]))
             BF7 = max( 0, float(rows["ASIAN_MALE_PERCENT"]) - 16.75)
             BF8 = max( 0, 16.75 - float(rows["ASIAN_MALE_PERCENT"]))
             BF9 = max( 0, float(rows["TMINORITY"]) - 405)
             BF10 = max( 0, 405 - float(rows["TMINORITY"]))
             BF11 = max( 0, float(rows["TOTALUNITS"]) - 25040)
             BF13 = max( 0, float(rows["TOTALUNITS"]) - 7372)

             ValCalc = 152.318 + 0.015104 * BF1 + 0.0145447 * BF3 - 0.000159989 * BF4\
                      - 90.2748 * BF5 + 1.63934 * BF6 - 33.8793 * BF7\
                      - 7.02735 * BF8 + 0.92076 * BF9 - 0.124537 * BF10\
                      - 0.0126089 * BF11 + 0.0159557 * BF13
            
             yield round(float(rows["RESPONSE"]),3),round(ValCalc,3)


def validationStepPositives():
    os.chdir("C:////Users////moose_f8sa3n2////Google Drive////Data Analysis for Project Management////Week 6")
    with open('scored_Positives.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for rows in reader:
             BF1 = max( 0, float(rows["RESIDENTS_TOTAL_ALL_DEATHS"]) - 928)
             BF6 = max( 0, 7.34046e+07 - float(rows["GDP_2018_THOUSANDS_DOLLARS"]))
             BF7 = max( 0, float(rows["HH_INCOME"]) - 94206)
             BF11 = max( 0, float(rows["PEOPLE_TOTAL"]) - 108445)

             ValCalc = 7636.38 + 9.48817 * BF1 - 0.000106908 * BF6 + 0.199672 * BF7 + 0.104197 * BF11

             yield round(float(rows["RESPONSE"]),3),round(ValCalc,3)



def dataPlotter():
    
    for line in validationStepPositivesPer100000():
    #for line in validationStepDeathsPer100000()
    #for line in validationStepPositives()
    #for line in validationStepDeaths()
        if line[1] > 0:
            plotX.append(line[1])
            plotY.append(line[0])

    fig = plt.figure(figsize=(10,7))
    plt.grid(True)
    plt.title('Predicted vs Actual Data')
    plt.xlabel('Predicted Values from data')
    plt.ylabel('Actual Values from data')
    sb.regplot(plotX,plotY,color='orange',marker="+")
    plt.scatter(plotX,plotY,color='green',marker="+")
    plt.show()
    
dataPlotter()
    

        
