import csv
import os
import sys
import seaborn as sb
import matplotlib.pyplot as plt

plotX = []
plotY = []

def validationStepDeathsPer100000():
    os.chdir(os.getcwd())
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
            
            yield round(float(rows["DEATHS_PER_100_000"]),3),round(ValCalc,3),rows["FIPS"],rows["COUNTY"],rows["STATE"]


def dataPlotter():
    while True:
        inputed = []
        inputs = input("Enter a county FIPS number (enter 'done' when finished): ")
        for line in validationStepDeathsPer100000():
            if line[1] > 0:
                plotX.append(line[1])
                plotY.append(line[0])
                try:
                    if inputs == line[2]:
                        inputed.append([inputs,line[3],line[4],line[1],line[0]])
                except NameError: pass
        try:
            if len(inputed) > 0:
                fig = plt.figure(figsize=(10,7))
                plt.grid(True)
                plt.title('Predicted vs Actual Deaths Per 100,000')
                plt.xlabel('Predicted Values from data')
                plt.ylabel('Actual Values from data')
                sb.regplot(plotX,plotY,color='orange',marker="+",scatter_kws={'alpha':0.2})
                plt.scatter(plotX,plotY,color='green',marker="+",alpha=.2)
                plt.scatter(inputed[0][4],inputed[0][3],color='red',
                            label = ('Fips: {}'.format(int(inputed[0][0])),
                                     'State: {}'.format(inputed[0][1]),
                                     'County: {}'.format(inputed[0][2]),
                                     'Actual Value: {}'.format(round(inputed[0][3],3)),
                                     'Predicted Value: {}'.format(round(inputed[0][4],3)),
                                     'Residual: {}'.format(round(inputed[0][4]-inputed[0][3],3))),
                            s=45)
                #print(inputed[0])
                fig.legend()
            plt.show()
            plt.close()
        except IndexError:
            pass
        if inputs.lower() == 'done': sys.exit(0)
    
dataPlotter()
