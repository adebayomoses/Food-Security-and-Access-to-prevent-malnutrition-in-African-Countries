
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns',40)

def preprocessing():
    
    df=pd.read_csv('data.csv')
    #dropping the unnamed column
    df.drop('Unnamed: 0',axis=1,inplace=True)

    #issues to resolve (Issue 3)

    #sum up all the plotareas for each household
    cols_fplot=df.columns[df.columns.str.contains('fplotarea')]
    df['total_plotarea']=df[cols_fplot].sum(axis=1)

    #drop fplotarea1, fplotarea2 and fplotarea3
    df.drop(columns=cols_fplot, inplace=True)

    #reduce fsystem to one column which returns the most common farmsystem used by each household,
    #for those with more than one common farm system, return the values that are common
    cols_fsystem=df.columns[df.columns.str.contains('fsystem')]
    fsystem_mode=df[cols_fsystem].mode(axis=1)[0]
    df['frequent_fsystem']=fsystem_mode

    #drop cols with fsystem
    df.drop(columns=cols_fsystem,inplace=True)

    #reduce the tenure to one column which returns the most common tenure system used by each household, 
    #for those with more than one common tenure system, return the values that are common
    cols_tenure=df.columns[df.columns.str.contains('tenure')]
    tenure_mode=df[cols_tenure].mode(axis=1)[0]
    df['frequent_tenure']=tenure_mode

    #drop cols with tenure
    df.drop(columns=cols_tenure,inplace=True)

    #reduce yearuse1 to one colum which returns the average number of years of use of each farmland
    cols_year=df.columns[df.columns.str.contains('yearsuse')]
    avg_yearsuse=df[cols_year].mean(axis=1)
    df['avg_yearsuse']=avg_yearsuse

    #drop cols with yearsuse
    df.drop(columns=cols_year,inplace=True)

    #reduce rentplot to one column which returns the average years each land is rented for each household
    cols_rent=df.columns[df.columns.str.contains('rentplot')]
    avg_rentplot=df[cols_rent].mean(axis=1)
    df['avg_rentplot']=avg_rentplot

    #drop cols with rentplot
    df.drop(columns=cols_rent,inplace=True)

    #drop season3 (since there are only 2 seasons in Africa)
    df.drop(columns=['season3s','season3e','seas3nam'],inplace=True)

    #drop all activites that have to do with season3
    #dropping the values in the first column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hm3')],inplace=True)

    #dropping the values in the second column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hmd3')],inplace=True)

    #dropping the values in the third column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hhf3')],inplace=True)

    #dropping the values in the fourth column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hfd3')],inplace=True)

    #dropping the values in the fifth column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hhc3')],inplace=True)

    #dropping the values in the sixth column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hcd3')],inplace=True)

    #dropping the values in the seven column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hrm3')],inplace=True)

    #dropping the values in the eight column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('rmd3')],inplace=True)

    #dropping the values in the ninth column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hrf3')],inplace=True)

    #dropping the values in the tenth column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hrfd3')],inplace=True)

    #dropping the values in the eleventh column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('hrc3')],inplace=True)

    #dropping the values in the twelfth column in the survey table
    df.drop(columns=df.columns[df.columns.str.contains('rcd3')],inplace=True)

    #reduce the household columns to calculate:

    #number of household labor

    #average number of days for household labor

    #reduce hired labor columns to calculate:

    #number of hired labor

    #average number of days for hired labor

    #columns for all household laborers (male, female, children)
    cols_labor=(df.columns[df.columns.str.contains('hhf1')].
          append(df.columns[df.columns.str.contains('hhm1')]).
          append(df.columns[df.columns.str.contains('hhc1')]))

    household_labor=df[cols_labor].count(axis=1)
    df['season1_count_household_labor']=household_labor

    #drop the columns
    df.drop(columns=cols_labor, inplace=True)

    #columns for household number of days
    cols_days=(df.columns[df.columns.str.contains('hhmd1')].
          append(df.columns[df.columns.str.contains('hhfd1')]).
          append(df.columns[df.columns.str.contains('hhcd1')]))

    household_labor=df[cols_days].mean(axis=1)
    df['season1_avg_household_days']=household_labor

    #drop the columns
    df.drop(columns=cols_days, inplace=True)

    #columns for all hired laborers (male, female, children)
    cols_hire=(df.columns[df.columns.str.contains('hrf1')].
          append(df.columns[df.columns.str.contains('hrm1')]).
          append(df.columns[df.columns.str.contains('hrc1')]))

    hired_labor=df[cols_hire].sum(axis=1)
    df['season1_sum_hired_labor']=hired_labor

    #drop the columns
    df.drop(columns=cols_hire, inplace=True)

    #columns for all hired number of days
    cols_hiredays=(df.columns[df.columns.str.contains('hrfd1')].
          append(df.columns[df.columns.str.contains('hrmd1')]).
          append(df.columns[df.columns.str.contains('hrcd1')]))

    hired_labor=df[cols_hiredays].mean(axis=1)
    df['season1_avg_hired_labor']=hired_labor

    #drop the columns
    df.drop(columns=cols_hiredays, inplace=True)

    ##Do similar for SEASON2
    #columns for all household laborers (male, female, children)
    cols_house=(df.columns[df.columns.str.contains('hhf2')].
          append(df.columns[df.columns.str.contains('hhm2')]).
          append(df.columns[df.columns.str.contains('hhc2')]))

    household_labor=df[cols_house].sum(axis=1)
    df['season2_count_household_labor']=household_labor

    #drop the columns
    df.drop(columns=cols_house, inplace=True)

    #columns for household number of days
    cols_days=(df.columns[df.columns.str.contains('hhmd2')].
          append(df.columns[df.columns.str.contains('hhfd2')]).
          append(df.columns[df.columns.str.contains('hhcd2')]))

    household_labor=df[cols_days].mean(axis=1)
    df['season2_avg_household_days']=household_labor

    #drop the columns
    df.drop(columns=cols_days, inplace=True)

    #columns for all hired laborers (male, female, children)
    cols=(df.columns[df.columns.str.contains('hrf2')].
          append(df.columns[df.columns.str.contains('hrm2')]).
          append(df.columns[df.columns.str.contains('hrc2')]))

    hired_labor=df[cols].sum(axis=1)
    df['season2_count_hired_labor']=hired_labor

    #drop the columns
    df.drop(columns=cols, inplace=True)

    #columns for all hired number of days
    cols=(df.columns[df.columns.str.contains('hrfd2')].
          append(df.columns[df.columns.str.contains('hrmd2')]).
          append(df.columns[df.columns.str.contains('hrcd2')]))

    hired_labor=df[cols].mean(axis=1)
    df['season2_avg_hired_labor']=hired_labor

    #drop the columns
    df.drop(columns=cols, inplace=True)

    #do the same for livestock, calculate the sum of household labor for livestock in each household
    df['livestock_household_labor']=df['livshhm']+df['livshhf']+df['livshhc']

    #drop the columns
    df.drop(columns=['livshhm','livshhf','livshhc'],inplace=True)

    #do the same for number of days
    df['livestock_avg_household_days']=df[['livshhmd','livshhfd','livshhcd']].mean(axis=1)

    #drop the columns
    df.drop(columns=['livshhmd','livshhfd','livshhcd'],inplace=True)

    #do same for hired labor
    df['livestock_hired_labor']=df['livshrm']+df['livshrf']+df['livshrc']
    #drop the columns
    df.drop(columns=['livshrm','livshrf','livshrc'],inplace=True)

    df['livestock_avg_hired_days']=df[['livshrmd','livshrfd','livshrcd']].mean(axis=1)
    #drop the columns
    df.drop(columns=['livshrmd','livshrfd','livshrcd'],inplace=True)

    #do the same thing for average wage
    df['avg_household_wage']=df[['wagehhm','wagehhf','wagehhc']].mean(axis=1)

    #drop the columns
    df.drop(columns=['wagehhm','wagehhf','wagehhc'],inplace=True)

    #do the same thing for average wage
    df['avg_hired_wage']=df[['wagehrm','wagehrf','wagehrc']].mean(axis=1)

    #drop the columns
    df.drop(columns=['wagehrm','wagehrf','wagehrc'],inplace=True)

    #do the same for inkind payment
    df['total_household_kind_payment']=df[['inkindhhm','inkindhhf','inkindhhc']].sum(axis=1)

    #drop the columns
    df.drop(columns=['inkindhhm','inkindhhf','inkindhhc'],inplace=True)

    df['total_hired_kind_payment']=df[['inkindhrm','inkindhrf','inkindhrc']].sum(axis=1)

    #drop the columns
    df.drop(columns=['inkindhrm','inkindhrf','inkindhrc'],inplace=True)

    # Section 4b resolved by Victor
    # Create column for total number of livestocks owned
    df["total_livestocks_owned"]=df[["lvs1num","lvs2num","lvs3num","lvs4num","lvs5num","lvs6num",
        "lvs7num","lvs8num","lvs9num","lvs10num","lvs11num","lvs12num"]].sum(axis=1)

    #drop the number of each type of livestocks owned
    df.drop(columns=["lvs1num","lvs2num","lvs3num","lvs4num","lvs5num","lvs6num",
        "lvs7num","lvs8num","lvs9num","lvs10num","lvs11num","lvs12num"], inplace=True)

    # Create column for total nummber of livestocks born over the last 12 months
    df["total_livestocks_born"]=df[["lvs1born","lvs2born","lvs3born","lvs4born","lvs5born","lvs6born",
        "lvs7born","lvs8born","lvs9born","lvs10born","lvs11born","lvs12born"]].sum(axis=1)

    # drop the number of each type of livestocks born
    df.drop(columns=["lvs1born","lvs2born","lvs3born","lvs4born","lvs5born","lvs6born",
        "lvs7born","lvs8born","lvs9born","lvs10born","lvs11born","lvs12born"], inplace=True)

    # Create columns for the total number of livestock lost in the past 12 years
    df["total_livestocks_lost"]=df[["lvs1lost","lvs2lost","lvs3lost","lvs4lost","lvs5lost","lvs6lost",
        "lvs7lost","lvs8lost","lvs9lost","lvs10lost","lvs11lost","lvs12lost"]].sum(axis=1)

    # Drop Columns for each type of livestock lost 
    df.drop(columns=["lvs1lost","lvs2lost","lvs3lost","lvs4lost","lvs5lost","lvs6lost",
        "lvs7lost","lvs8lost","lvs9lost","lvs10lost","lvs11lost","lvs12lost"], inplace=True)

    # Create columns for the total number of livestock purchased in the past 12 years
    df["total_livestocks_purchased"]=df[["lvs1purch","lvs2purch","lvs3purch","lvs4purch","lvs5purch","lvs6purch",
        "lvs7purch","lvs8purch","lvs9purch","lvs10purch","lvs11purch","lvs12purch"]].sum(axis=1)

    # Drop Columns for each type of livestock purchased
    df.drop(columns=["lvs1purch","lvs2purch","lvs3purch","lvs4purch","lvs5purch","lvs6purch",
        "lvs7purch","lvs8purch","lvs9purch","lvs10purch","lvs11purch","lvs12purch"], inplace=True)

    # Create columns for the average purchase price per animal
    df["livestocks_avg_purchase_price"] = df[["lvs1pprice","lvs2pprice","lvs3pprice","lvs4pprice","lvs5pprice","lvs6pprice",
        "lvs7pprice","lvs8pprice","lvs9pprice","lvs10pprice","lvs11pprice","lvs12pprice"]].mean(axis=1)

    #Drop columns for purchase price per animals 
    df.drop(columns=["lvs1pprice","lvs2pprice","lvs3pprice","lvs4pprice","lvs5pprice","lvs6pprice",
        "lvs7pprice","lvs8pprice","lvs9pprice","lvs10pprice","lvs11pprice","lvs12pprice"], inplace=True)

    # Create columns for the average number of months than animals graze on Communalland 
    df["months_grazed_communal"]=df[["lvs1graze1","lvs2graze1","lvs3graze1","lvs4graze1","lvs5graze1","lvs6graze1",
        "lvs7graze1","lvs8graze1","lvs9graze1","lvs10graze1","lvs11graze1","lvs12graze1"]].mean(axis=1)

    # Drop columns with number of months each type of animals graze communal land
    df.drop(columns=["lvs1graze1","lvs2graze1","lvs3graze1","lvs4graze1","lvs5graze1","lvs6graze1",
        "lvs7graze1","lvs8graze1","lvs9graze1","lvs10graze1","lvs11graze1","lvs12graze1"], inplace=True)

    # Create columns for the average number of months than animals graze on 'Own land' 
    df["months_grazed_own"]=df[["lvs1graze2","lvs2graze2","lvs3graze2","lvs4graze2","lvs5graze2","lvs6graze2",
        "lvs7graze2","lvs8graze2","lvs9graze2","lvs10graze2","lvs11graze2","lvs12graze2"]].mean(axis=1)

    # Drop columns with number of months each type of animals graze Own land
    df.drop(columns=["lvs1graze2","lvs2graze2","lvs3graze2","lvs4graze2","lvs5graze2","lvs6graze2",
        "lvs7graze2","lvs8graze2","lvs9graze2","lvs10graze2","lvs11graze2","lvs12graze2"], inplace=True)

    # Create columns for the average number of months than animals graze on 'Open land' 
    df["month_grazed_openland"]=df[["lvs1graze3","lvs2graze3","lvs3graze3","lvs4graze3","lvs5graze3","lvs6graze3",
        "lvs7graze3","lvs8graze3","lvs9graze3","lvs10graze3","lvs11graze3","lvs12graze3"]].mean(axis=1)

    # Drop columns with number of months each type of animals graze open land
    df.drop(columns=["lvs1graze3","lvs2graze3","lvs3graze3","lvs4graze3","lvs5graze3","lvs6graze3",
        "lvs7graze3","lvs8graze3","lvs9graze3","lvs10graze3","lvs11graze3","lvs12graze3"], inplace=True)

    # Create columns for the total number of livestock sold in the past 12 years
    df["total_livestocks_sold"]=df[["lvs1sold","lvs2sold","lvs3sold","lvs4sold","lvs5sold","lvs6sold",
        "lvs7sold","lvs8sold","lvs9sold","lvs10sold","lvs11sold","lvs12sold"]].sum(axis=1)

    # Drop Columns for each type of livestock sold
    df.drop(columns=["lvs1sold","lvs2sold","lvs3sold","lvs4sold","lvs5sold","lvs6sold",
        "lvs7sold","lvs8sold","lvs9sold","lvs10sold","lvs11sold","lvs12sold"], inplace=True)

    # Create columns for the average sales price per animal
    df["livestocks_avg_sales_price"] = df[["lvs1sprice","lvs2sprice","lvs3sprice","lvs4sprice","lvs5sprice","lvs6sprice",
        "lvs7sprice","lvs8sprice","lvs9sprice","lvs10sprice","lvs11sprice","lvs12sprice"]].mean(axis=1)

    # Drop columns used for creating average sales price per animal
    df.drop(columns=["lvs1sprice","lvs2sprice","lvs3sprice","lvs4sprice","lvs5sprice","lvs6sprice",
        "lvs7sprice","lvs8sprice","lvs9sprice","lvs10sprice","lvs11sprice","lvs12sprice"], inplace=True)

    # Create columns for the average Quanity of livestock product used per year
    df["avg_livestocks_product_used"] = df[["lvsp1use","lvsp2use","lvsp3use","lvsp4use","lvsp5use","lvsp6use",
        "lvsp7use","lvsp8use","lvsp9use"]].mean(axis=1)

    # Drop columns used for creating average Quantity of liverstocks product used per year
    df.drop(columns=["lvsp1use","lvsp2use","lvsp3use","lvsp4use","lvsp5use","lvsp6use",
        "lvsp7use","lvsp8use","lvsp9use"], inplace=True)

    # Create columns for the average Quanity of livestock product used per year
    df["avg_livestocks_product_sold"] = df[["lvsp1sell","lvsp2sell","lvsp3sell","lvsp4sell","lvsp5sell","lvsp6sell",
        "lvsp7sell","lvsp8sell","lvsp9sell"]].mean(axis=1)

    # Drop columns used for creating average Quantity of liverstocks product sold per year
    df.drop(columns=["lvsp1sell","lvsp2sell","lvsp3sell","lvsp4sell","lvsp5sell","lvsp6sell",
        "lvsp7sell","lvsp8sell","lvsp9sell"], inplace=True)

    # Create columns for the Average Price of Livestock product sold per unit 
    df["avg_product_price"] = df[["lvsp1price","lvsp2price","lvsp3price","lvsp4price","lvsp5price","lvsp6price",
        "lvsp7price","lvsp8price","lvsp9price"]].mean(axis=1)

    # Drop columns used for creating average Price of Livestock product sold per unit 
    df.drop(columns=["lvsp1price","lvsp2price","lvsp3price","lvsp4price","lvsp5price","lvsp6price",
        "lvsp7price","lvsp8price","lvsp9price"], inplace=True)

    #Rename Columns 
    df["transport_cropcost"] = df["cost1crop"] # cost of transportion of food and tree crops harvested
    df["pm_cropcost"] = df["cost2crop"] # Cost of Packing/marketing of food and tree crops harvested
    df["storage_cropcost"] = df["cost3crop"] # cost of storage of food and tree crops harvested
    df["postharvest_croploss"] = df["cost4crop"] # Post harvest loss on food and tree crops harvested
    df["other_cropcost"] = df["cost5crop"] # Other cost on food and tree crops harvested
    df["transport_lvscost"]=df['cost1lvs'] # cost of transportion of livestocks
    df["pm_lvscost"] = df["cost2lvs"]  #cost of Packing/marketing on livestocks
    df["storage_lvscost"] = df["cost3lvs"] # cost of storage on livestock
    df["postharvest_lvsloss"] = df["cost4lvs"] # Post harvest loss on livestock
    df["other_lvscost"] = df["cost5lvs"] # Other cost on livestocks

    # Drops columns on cost1crop,...,cost5lvs
    df.drop(columns=["cost1crop","cost2crop","cost3crop","cost4crop","cost5crop","cost1lvs",
                     "cost2lvs","cost3lvs","cost4lvs","cost5lvs"], inplace=True)

    #Section 7
    def new_df (df,col_name,pattern):
        ''' 
        df: dataframe,
        col_name: the name of the column to create
        pattern: the pattern to match.

        Returns the new dataframe with the new column created
        '''
        data=df[df.columns[df.columns.str.contains(pattern)]]
        new_df=[]
        for x,y in data.iterrows():
            new_df.append(y[y==1].index.to_list())

        new_list=[', '.join(item) for item in new_df]
        new_list=pd.Series(new_list)
        df[col_name]=new_list

        #replace empty space with nan values
        df[col_name]=df[col_name].replace('',np.nan)

        #drop the columns
        df.drop(columns=data.columns,inplace=True)

        return df

    #create a new column for response to ad71 questions
    df=new_df(df,'adaptation_to_climate','ad71')

    #create a new column for responses to ad72 questions
    df=new_df(df,'constraints_to_adjustment','ad72')

    #create a new column for responses to ad73 questions
    df=new_df(df,'shift_mean_temperature','ad73')

    #create a new column for responses to ad74 questions
    df=new_df(df,'shift_mean_rainfall','ad74')

    #create a new column for responses to ad75 questions
    df=new_df(df, 'adaptation_temperature_change','ad75')

    #create a new column for responses to ad76 questions
    df=new_df(df, 'adaptation_precipitation_change','ad76')

    #for Zimbabwe, since their coding is clmadaptstrategy1, clmadaptstrategy2, clmadaptstrategy3
    df['adaptation_to_climate']=(df['adaptation_to_climate'].
                                 fillna(df['clmadaptstrategy1']).
                                 fillna( df['clmadaptstrategy2']).
                                 fillna( df['clmadaptstrategy3'])
                                )
    #drop the columns
    df.drop(columns=['clmadaptstrategy1','clmadaptstrategy2','clmadaptstrategy3'],inplace=True)

    #do the same for constraint1-3
    df['constraints_to_adjustment']=(df['constraints_to_adjustment'].
                                 fillna(df['constraint1']).
                                 fillna( df['constraint2']).
                                 fillna( df['constraint3'])
                                )

    #drop the columns
    df.drop(columns=['constraint1','constraint2','constraint3'],inplace=True)


    #do the same for longtermtempshifts1-3
    df['shift_mean_temperature']=(df['shift_mean_temperature'].
                                 fillna(df['longtermtempshifts1']).
                                 fillna( df['longtermtempshifts2']).
                                 fillna( df['longtermtempshifts3'])
                                )

    #drop the columns
    df.drop(columns=['longtermtempshifts1','longtermtempshifts2','longtermtempshifts3'],inplace=True)

    #do the same for longtermrainfallshifts1-3
    df['shift_mean_rainfall']=(df['shift_mean_rainfall'].
                                 fillna(df['longtermrainfallshifts1']).
                                 fillna( df['longtermrainfallshifts2']).
                                 fillna( df['longtermrainfallshifts3'])
                                )

    #drop the columns
    df.drop(columns=['longtermrainfallshifts1','longtermrainfallshifts2','longtermrainfallshifts3'],inplace=True)

    #do the same for adjtempshifts1-3
    df['adaptation_temperature_change']=(df['adaptation_temperature_change'].
                                 fillna(df['adjtempshifts1']).
                                 fillna( df['adjtempshifts2']).
                                 fillna( df['adjtempshifts3']).
                                fillna(df['adjtempshifts1_1']).
                                fillna(df['adjtempshifts2_1']).
                                fillna(df['adjtempshifts3_1'])
                                )
    #drop the columns
    df.drop(columns=['adjtempshifts1','adjtempshifts2','adjtempshifts3',
                    'adjtempshifts1_1','adjtempshifts2_1','adjtempshifts3_1'],inplace=True)

    #do the same for adjrainfallshifts1-3
    df['adaptation_precipitation_change']=(df['adaptation_precipitation_change'].
                                 fillna(df['adjrainfallshifts1']).
                                 fillna( df['adjrainfallshifts2']).
                                 fillna( df['adjrainfallshifts3']).
                                fillna( df['adjrainfallshifts1_1']).
                                fillna( df['adjrainfallshifts2_1']).
                                fillna(df['adjrainfallshifts3_1']))

    #drop the columns
    df.drop(columns=['adjrainfallshifts1','adjrainfallshifts2',
                     'adjrainfallshifts3','adjrainfallshifts1_1','adjrainfallshifts2_1',
                    'adjrainfallshifts3_1'],inplace=True)                            

    #Issue 1 Resolved

    #Find the mean eduation level of the members of each household to determine the level education in each.
    df['edu_level'] = df[df.columns[df.columns.str.contains('educ')]].mean(axis = 1)

    df['edu_level'].head(5)

    #drop educ1 - educ38
    df.drop(df.columns[df.columns.str.contains('educ')], axis = 1, inplace = True)

    #aggregate the ages of each household to determine the strength and level of experience

    #average age of each household
    df['ave_age'] = df[df.columns[df.columns.str.contains('age')]].mean(axis = 1)

    #maximum age
    df['max_age'] = df[df.columns[df.columns.str.contains('age')]].max(axis = 1)

    #drop age1 - age38
    #df.drop(df.columns[df.columns.str.contains('age')], axis = 1, inplace = True)

    df.drop(['age1','age2', 'age3', 'age4', 'age5', 'age6', 'age7', 'age8', 'age9', 
             'age10','age11', 'age12', 'age13', 'age14', 'age15','age16', 'age17', 
             'age18', 'age19', 'age20', 'age21', 'age22', 'age23', 'age24', 'age25', 
             'age26', 'age27', 'age28','age29', 'age30', 'age31', 'age32', 'age33', 
             'age34', 'age35', 'age36', 'age37', 'age38'], axis = 1, inplace = True)

    #to determine the number of female and male in each household
    df['nmale'] = df[df.columns[df.columns.str.contains('gender')]].apply(lambda x: (x == 1).sum(), axis = 1)

    df['nfemale'] = df[df.columns[df.columns.str.contains('gender')]].apply(lambda x: (x == 2).sum(), axis = 1)

    #drop gender1 - gender38
    df.drop(df.columns[df.columns.str.contains('gender')], axis = 1, inplace = True)

    #frequency of members involve in non farmwork
    df['mem_nfarmwrk'] = df[df.columns[df.columns.str.contains('nfarmwork')]].apply(lambda x : (x == 1).sum(), axis = 1)

    #drop nfarmwork1 - 38
    df.drop(df.columns[df.columns.str.contains('nfarmwork')], axis = 1, inplace = True)

    #frequency of member involve in farmwork
    df['mem_farmwrk'] = df[df.columns[df.columns.str.contains('farmwork')]].apply(lambda x : (x == 1).sum(), axis = 1)

    #drop farmwork1 - 38
    df.drop(df.columns[df.columns.str.contains('farmwork')], axis = 1, inplace = True)

    #married

    #number of married people
    df['n_maried'] = df[df.columns[df.columns.str.contains('married')]].apply(lambda x : (x== 1).sum(), axis =1)

    #number of singles
    df['n_singles'] = df[df.columns[df.columns.str.contains('married')]].apply(lambda x : (x== 2).sum(), axis =1)

    #number of divorceds
    df['n_divorced'] = df[df.columns[df.columns.str.contains('married')]].apply(lambda x : (x== 3).sum(), axis =1)

    #number of teengers
    df['n_teengers'] = df[df.columns[df.columns.str.contains('married')]].apply(lambda x : (x== 4).sum(), axis =1)

    #drop married1 - 38
    df.drop(df.columns[df.columns.str.contains('married')], axis = 1, inplace = True)


    #rename primary occupation and secondary occupation
    df.rename({'hhhdocc1' : 'primary_occu', 'hhhdocc2' : 'sec_occu'}, axis = 1,inplace=True)


    #issue 4a resolved
    cols=df.columns[df.columns.str.startswith('s3')]
    df.drop(columns=cols, inplace=True)

    crop_type=df[['s1p1c1','s1p1c2','s1p1c3','s1p1c4','s1p1c5','s1p1c6',
                  's1p2c1','s1p2c2','s1p2c3','s1p2c4','s1p2c5','s1p2c6',
                 's1p3c1','s1p3c2','s1p3c3','s1p3c4','s1p3c5','s1p3c6']]
    df_crop=[]
    for a,b in crop_type.iterrows():
        df_crop.append(b[b>=1].values)

    result = [', '.join(map(str, row)) for row in df_crop]
    series=pd.Series(result)
    df['season1_crop_type']=series

    #drop the columns
    df.drop(columns=crop_type.columns, inplace=True)

    crop_type=df[['s2p1c1','s2p1c2','s2p1c3','s2p1c4','s2p1c5','s2p1c6',
                  's2p2c1','s2p2c2','s2p2c3','s2p2c4','s2p2c5','s2p2c6',]]

    df_crop=[]
    for a,b in crop_type.iterrows():
        df_crop.append(b[b>=1].values)

    result = [', '.join(map(str, row)) for row in df_crop]
    series=pd.Series(result)
    df['season2_crop_type']=series

    #drop the columns
    df.drop(columns=crop_type.columns, inplace=True)


    #harvest and planting date not needed, so drop them
    cols_plant=df.columns[df.columns.str.contains('s1\w+plant')]
    cols_harvest=df.columns[df.columns.str.contains('s1\w{4}harv')]
    cols_2plant=df.columns[df.columns.str.contains('s2\w+plant')]
    cols_2harv=df.columns[df.columns.str.contains('s2\w{4}harv')]

    df.drop(columns=cols_plant,inplace=True)
    df.drop(columns=cols_harvest,inplace=True)
    df.drop(columns=cols_2plant,inplace=True)
    df.drop(columns=cols_2harv,inplace=True)

    #what is the mean proportion of area used for planting in season_1 and season_2
    cols=df.columns[df.columns.str.contains('s1\w+area')]
    df_season1_area=df[cols].mean(axis=1)
    df['season1_mean_area']=df_season1_area

    #drop the columns
    df.drop(columns=cols, inplace=True)

    #do same for season 2
    cols=df.columns[df.columns.str.contains('s2\w+area')]
    df_season2_area=df[cols].mean(axis=1)
    df['season2_mean_area']=df_season2_area

    #drop the columns
    df.drop(columns=cols, inplace=True)

    #what is the mean quantity of harvest for season 1 and season 2
    cols=df.columns[df.columns.str.contains('s1\w+qharv')]
    df_season1_qharv=df[cols].mean(axis=1)
    df['season1_mean_qharv']=df_season1_qharv

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #do same for season 2
    cols=df.columns[df.columns.str.contains('s2\w+qharv')]
    df_season2_qharv=df[cols].mean(axis=1)
    df['season2_mean_qharv']=df_season2_qharv

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #what is the mean amount consumed by household from season 1 and 2
    cols=df.columns[df.columns.str.contains('s1\w+cons')]
    df_season1_cons=df[cols].mean(axis=1)
    df['season1_mean_household_consumption']=df_season1_cons

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #do same for season 2
    cols=df.columns[df.columns.str.contains('s2\w+cons')]
    df_season2_cons=df[cols].mean(axis=1)
    df['season2_mean_household_consumption']=df_season2_cons

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #what is the mean amount consumed by livestock from season 1 and 2
    cols=df.columns[df.columns.str.contains('s1\w+lives')]
    df_season1_lives=df[cols].mean(axis=1)
    df['season1_mean_livestock_consumption']=df_season1_lives

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #do same for season 2
    cols=df.columns[df.columns.str.contains('s2\w+lives')]
    df_season2_lives=df[cols].mean(axis=1)
    df['season2_mean_livestock_consumption']=df_season2_lives

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #what is the mean amount lost due to livestock and pest in season 1 and 2?
    cols=df.columns[df.columns.str.contains('s1\w+lost')]
    df_season1_lost=df[cols].mean(axis=1)
    df['season1_mean_loss']=df_season1_lost

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #do same for season 2
    cols=df.columns[df.columns.str.contains('s2\w+lost')]
    df_season2_lost=df[cols].mean(axis=1)
    df['season2_mean_loss']=df_season2_lost

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #what is the mean quantity sold in season 1 and 2
    cols=df.columns[df.columns.str.contains('s1\w+sold')]
    df_season1_sold=df[cols].mean(axis=1)
    df['season1_mean_sold']=df_season1_sold

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #do same for season 2
    cols=df.columns[df.columns.str.contains('s2\w+sold')]
    df_season2_sold=df[cols].mean(axis=1)
    df['season2_mean_sold']=df_season2_sold

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #drop columns for mkt
    cols=df.columns[df.columns.str.contains('s1\w+mkt')]
    df.drop(columns=cols, inplace=True)

    #what is the average amount of seed used in season 1 and 2
    df['s1p1c1seed'] =  df['s1p1c1seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c2seed'] =  df['s1p1c2seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c3seed'] =  df['s1p1c3seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c4seed'] =  df['s1p1c4seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c5seed'] =  df['s1p1c5seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c6seed'] =  df['s1p1c6seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p2c1seed'] =  df['s1p2c1seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p2c2seed'] =  df['s1p2c2seed'].str.extract("(\d+\.?\d+)").astype(float)

    cols=df.columns[df.columns.str.contains('s1\w+seed')]
    df_season1_seed=df[cols].mean(axis=1)
    df['season1_mean_seed_used']=df_season1_seed

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #do same for season 2
    df['s2p1c1seed'] =  df['s2p1c1seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p1c2seed'] =  df['s2p1c2seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p1c3seed'] =  df['s2p1c3seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p1c4seed'] =  df['s2p1c4seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p2c1seed'] =  df['s2p2c1seed'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p2c2seed'] =  df['s2p2c2seed'].str.extract("(\d+\.?\d+)").astype(float)

    cols=df.columns[df.columns.str.contains('s2\w+seed')]
    df_season2_seed=df[cols].mean(axis=1)
    df['season2_mean_seed_used']=df_season2_seed

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #what is the average cost per seed used
    df['s1p1c1sval'] =  df['s1p1c1sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c2sval'] =  df['s1p1c2sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c3sval'] =  df['s1p1c3sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c4sval'] =  df['s1p1c4sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c5sval'] =  df['s1p1c5sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p1c6sval'] =  df['s1p1c6sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p2c1sval'] =  df['s1p2c1sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s1p2c2sval'] =  df['s1p2c2sval'].str.extract("(\d+\.?\d+)").astype(float)

    cols=df.columns[df.columns.str.contains('s1\w+sval')]
    df_season1_sval=df[cols].mean(axis=1)
    df['season1_mean_seed_value']=df_season1_sval

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #do same for season 2
    df['s2p1c1sval'] =  df['s2p1c1sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p1c2sval'] =  df['s2p1c2sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p1c3sval'] =  df['s2p1c3sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p1c4sval'] =  df['s2p1c4sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p2c1sval'] =  df['s2p2c1sval'].str.extract("(\d+\.?\d+)").astype(float)

    df['s2p2c2sval'] =  df['s2p2c2sval'].str.extract("(\d+\.?\d+)").astype(float)
    cols=df.columns[df.columns.str.contains('s2\w+sval')]
    df_season2_sval=df[cols].mean(axis=1)
    df['season2_mean_seed_value']=df_season2_sval

    #drop the cols
    df.drop(columns=cols, inplace=True)

    #create a columnn for the count of the crop type for each household per year, and another column for the 
    cols=df.columns[df.columns.str.startswith('pc')]
    crop_type=df[cols].count(axis=1)
    df['no_of_crop_types']=crop_type

    #drop the columns
    df.drop(columns=cols, inplace=True)

    #do the same for yield, but find the average
    cols=df.columns[df.columns.str.startswith('nyieldc')]
    avg_yield_per_crop=df[cols].mean(axis=1)
    df['avg_yield_per_crop_type']=avg_yield_per_crop

    #drop the columns
    df.drop(columns=cols, inplace=True)

    df['water_supply']= (df['s1p1wat1'].fillna(df['s1p1wat2']).
                         fillna(df['s1p1wat3']).fillna(df['s1p1wat4']).
                         fillna(df['s1p1wat5']))
    #drop the columns
    df.drop(columns=['s1p1wat1','s1p1wat2','s1p1wat3','s1p1wat4','s1p1wat5'],inplace=True)


    #find the means of water supply for season 1 for each household
    cols=df.columns[df.columns.str.contains('s1p\d+wat\d+')]
    #merge the columns into one

    df['season1_water_supply']=None
    for col in cols:
        df['season1_water_supply'].fillna(df[col],inplace=True)

    #drop the columns
    df.drop(columns=cols,inplace=True)

    #do the same for season 2
    cols=df.columns[df.columns.str.contains('s2p\d+wat\d+')]
    #merge the columns into one

    df['season2_water_supply']=None
    for col in cols:
        df['season2_water_supply'].fillna(df[col],inplace=True)

    #drop the columns
    df.drop(columns=cols,inplace=True)


    #find the irrigation system used by each household
    cols=df.columns[df.columns.str.contains('s1\w+irrig')]
    #merge the columns into one

    df['season1_irrigation_type']=None
    for col in cols:
        df['season1_irrigation_type'].fillna(df[col],inplace=True)

    #drop the columns
    df.drop(columns=cols,inplace=True)

    cols=df.columns[df.columns.str.contains('s2\w+irrig')]
    #merge the columns into one

    df['season2_irrigation_type']=None
    for col in cols:
        df['season2_irrigation_type'].fillna(df[col],inplace=True)

    #drop the columns
    df.drop(columns=cols,inplace=True)

    #find the average fertilizer use per household for season 1 and 2
    cols=df.columns[df.columns.str.contains('s1\w+fert')]
    season1_fert=df[cols].mean(axis=1)
    df['season1_avg_fertilizer']=season1_fert

    #drop the columns
    df.drop(columns=cols,inplace=True)

    #do the same for season2
    cols=df.columns[df.columns.str.contains('s2\w+fert')]
    season2_fert=df[cols].mean(axis=1)
    df['season2_avg_fertilizer']=season2_fert

    #drop the columns
    df.drop(columns=cols,inplace=True)

    #find the average pesticide use per family for season 1 and 2
    cols=df.columns[df.columns.str.contains('s1\w+pest')]
    season1_pest=df[cols].mean(axis=1)
    df['season1_avg_pesticide']=season1_pest

    #drop the columns
    df.drop(columns=cols,inplace=True)

    #do the same for season 2
    cols=df.columns[df.columns.str.contains('s2\w+pest')]
    season2_pest=df[cols].mean(axis=1)
    df['season2_avg_pesticide']=season2_pest

    #drop the columns
    df.drop(columns=cols,inplace=True)

    #we don't need the column for the owner of the machinery, so drop it
    cols=df.columns[df.columns.str.contains('owner')]
    df.drop(columns=cols,inplace=True)

    #calculate the average price per machinery for each household
    cols=df.columns[df.columns.str.contains('\w{2}\d+price')]
    avg_price_equipment=df[cols].mean(axis=1)
    df['avg_price_equip']=avg_price_equipment

    #drop the columns
    df.drop(columns=cols, inplace=True)

    #calculate the average lifespan of each equipment for each household
    cols=df.columns[df.columns.str.contains('\w{2}\d+life')]
    avg_lifespan=df[cols].mean(axis=1)
    df['avg_lifespan_equip']=avg_lifespan

    #drop the columns
    df.drop(columns=cols,inplace=True)

    #calculate the average number of equipment used/owned by each family
    cols=df.columns[df.columns.str.contains('[lha]m\d+')]
    avg_no_equip=df[cols].mean(axis=1)
    df['avg_no_equipment']=avg_no_equip

    #drop the columns
    df.drop(columns=cols, inplace=True)

    #drop the columns for builduse
    cols=df.columns[df.columns.str.contains('build\w+')]
    df.drop(columns=cols,inplace=True)

    # Section 5 Issue resolved 


    # Drop the whole section 5 columns 
    df.drop(columns=df.columns[df.columns.str.startswith('ext')], inplace=True)
    #section 6
    #sum of all taxes to be paid
    total_tax_paid= df[df.columns[df.columns.str.contains('tax')]].sum(axis=1)
    #equivalent columns for total tax
    #drop irrelevant columns of tax
    df.drop(['taxincome', 'taxprop','taxsales','taxother'], axis= 1, inplace= True)
    #include the equivalent tax column to the dataframe
    df['total_tax_paid']= total_tax_paid
    #For the income section
    #Total income from farm activities per household will be the average of the average income yearly and the income for the last     12 monts
    #inc_farm= df[['incfarm', 'incfarm_n']].mean(axis=1)
    #Drop the irrelevant columns
    df.drop(['incfarm_n'], axis=1, inplace= True)
    #include the relevant column
    #df['inc_farm']= inc_farm
    #Do the same for income from non farm activities
    #inc_nfarm= df[['incnfarm', 'incnfarm_n']].mean(axis=1)
    df.drop(['incnfarm', 'incnfarm_n'], axis=1, inplace= True)
    #df['inc_nfarm']= inc_nfarm
    #The subsidy section
    df[df.columns[df.columns.str.contains('subs')]]
    df.drop(['subs1from', 'subs1get', 'subs1tot', 
             'subs2from','subs2get', 'subs2tot', 'subs3from', 
             'subs3get', 'subs3tot','subs4from', 'subs4get', 
             'subs4tot'], axis=1, inplace= True)
    #The borrowed money section
   
    #since there are very few numbers that borrowed from relatives
    #we drop the column
    df.drop(['inc1', 'inc1tot', 'inc1r', 'inc1years'], axis= 1, inplace= True)
    
    #Do same for inc2
    df.drop(['inc2', 'inc2r', 'inc2tot', 'inc2years'], axis= 1, inplace= True)
    
    #Do same for inc3
    df.drop(['inc3', 'inc3r', 'inc3tot', 'inc3years'], axis= 1, inplace= True)
    
    #Do same for inc4
    df.drop(['inc4', 'inc4r', 'inc4tot', 'inc4years'], axis= 1, inplace= True)
    
    #Do same for inc5
    df.drop(['inc5', 'inc5r', 'inc5tot', 'inc5years'], axis= 1, inplace= True)

    return df

    # Section 6 Resolved
