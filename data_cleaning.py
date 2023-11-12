from Data_preprocessing import *

def cleaning (df=preprocessing()):

    # List of columns having more than 50% null values
    col_to_drop=df.isna().mean()[df.isna().mean()>=.50].index

    # drop the selected columns
    df = df.drop(columns=col_to_drop)

    # checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
    # change incorrect datatype from float to object
    # checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
    # change incorrect datatype from float to object

    cols_to_object=['hhcode','cadm0','cadm1','cadm2','code','farmtype','fplots','hhelectric','primary_occu',
                    'sec_occu','hhrelig','lvsown','relhead', 'water_supply', 'season2_water_supply']

    df[cols_to_object]=df[cols_to_object].astype('object')


    #drop further columns
    #tib (time interview began) column not needed
    #tie (time interview ended)
    #interviewer
    #'max_age'
    #'hhcode'
    #code

    cols_to_drop=['tib','tie','interviewer','max_age','hhcode','code']
    df.drop(columns=cols_to_drop,inplace=True)

    #clean transport column, should have only 6 valid enteries. 
    #replace 0 with nan, replace 12 and 9 with nan, convert to object

    #key for interpretation
    #1: walk
    #2: animal
    #3: cart/bicycle
    #4: truck or other motorized vehicles
    #5: Others
    #6: Combination of the above

    df['transport'].replace([0,12,9],[np.nan,np.nan,np.nan],inplace=True)

    df['transport']=df['transport'].astype('object')

    #frequent_fsystem, rename to to most common farm_system
    #only allowed values are from 1-6, replace any other value with np.nan
    #convert to object

    #key
    #1: Shifting cultivation (With long fallow period)
    #2: Continuous cropping (no fallow period)
    #3: Continuous cropping with multiple rotations (includes short fallow period)
    #4: Livestock grazing land
    #5: Other
    #6: Combination of above

    df['frequent_fsystem'].replace(0,np.nan,inplace=True)
    df['frequent_fsystem']=df['frequent_fsystem'].astype('object')
    df.rename(columns={'frequent_fsystem':'most_common_farmsystem'},inplace=True)

    #frequent_tenure, rename to to most_common_tenure_system
    #only allowed values are from 1-7, replace any other value with np.nan
    #convert to object

    #key
    #1: Own land and own use
    #2. Own land and rent to others
    #3: Sharecropped land
    #4: Communal land (traditional ownership)
    #5: Rented land
    #6: Borrowed land (Do not pay for usage)
    #7: Other (pls. specify . . . ) incl combinations of above

    df['frequent_tenure'].replace([0,15,12,16],[np.nan,np.nan,np.nan,np.nan],inplace=True)
    df['frequent_tenure']=df['frequent_tenure'].astype('object')
    df.rename(columns={'frequent_tenure':'most_common_tenuresystem'},inplace=True)

    #rename avg_yearuse to avg_use_of_plot_in_years
    df.rename(columns={'avg_yearsuse':'avg_use_of_plot_in_years'},inplace=True)

    #sum the labor for household and hired for both season1 and 2 into one column and name the column
    #number_of_laborers, 
    #convert to integer
    df['number_of_laborers']=df[['season1_count_household_labor', 'season1_sum_hired_labor',
                               'season2_count_household_labor', 'season2_count_hired_labor']].sum(axis=1).astype(int)

    #drop the columns
    df.drop(columns=['season1_count_household_labor', 'season1_sum_hired_labor',
                               'season2_count_household_labor', 'season2_count_hired_labor'],inplace=True)

    #sum the number of days for hired and household labor for both season 1 and season 2 into a column
    #days spent by laborers
    #convert to integer
    #drop the columns
    df['days_spent_by_laborers']=df[['season1_avg_household_days','season1_avg_hired_labor',
                                     'season2_avg_household_days','season2_avg_hired_labor']].sum(axis=1).astype(int)

    df.drop(columns=['season1_avg_household_days','season1_avg_hired_labor',
                                     'season2_avg_household_days','season2_avg_hired_labor'],inplace=True)

    #sum the number labor for livestock_labor for household and hired labor into one column and name the column
    #livestock_number_of_laborers
    #convert datatype to int
    #drop the columns

    df['livestock_number_of_laborers']=df[['livestock_household_labor','livestock_hired_labor']].sum(axis=1).astype(int)

    df.drop(columns=['livestock_household_labor','livestock_hired_labor'],inplace=True)

    #sum the number of days for hired and household labor livestock into one clumn named
    #days_spent_by_livestock_laborers
    #convert datatype to int
    #drop the columns
    df['days_spent_by_livestock_laborers']=df[['livestock_avg_household_days',
                                               'livestock_avg_hired_days']].sum(axis=1).astype(int)

    df.drop(columns=['livestock_avg_household_days','livestock_avg_hired_days'],inplace=True)

    #sum up the avg_household_wage and avg_hired_wage in one column and name it labor_wage
    #drop the columns

    df['labor_wage_payment']=df[['avg_household_wage','avg_hired_wage']].sum(axis=1)

    df.drop(columns=['avg_household_wage','avg_hired_wage'],inplace=True)

    #sum the kind payment for both household and hired in one column and name it kind_payment

    #drop the columns
    df['kind_payment']=df[['total_household_kind_payment','total_hired_kind_payment']].sum(axis=1)

    df.drop(columns=['total_household_kind_payment','total_hired_kind_payment'],inplace=True)

    #replace 0 with nan
    #change dtype to object

    #key for interpretation
    #1: irrigated- major scheme (public); 
    #2: irrigated minor scheme (private); 
    #3: irrigated - groundwater; 
    #4: rain-fed
    #5 : Other (pls. specify . . . )

    df['water_supply'].replace(0, np.nan,inplace=True)
    df['water_supply']=df['water_supply'].astype('object')

    #drop rows with household size greater than 39 (since maximum household according to the survey is 39)

    df.drop(df[df['hhsize']>39].index, inplace=True)
    
    numeric_cols=df.select_dtypes('number').columns

    # Define the threshold quantiles
    
    #It appears the income was collected in local currency, convert to usd, 
    
    # Create a dictionary with conversion factors
    conversion_factors = {
        'niger': 614.05,
        'ethiopia': 55.86,
        'zambia': 22.46,
        'senegal': 614.05,
        'burkinafaso': 614.05,
        'egypt': 30.90,
        'cameroon': 614.05,
        'ghana': 11.92,
        'kenya': 151.4,
        'zimbabwe': 322,
        'south africa': 18.42
    }

    # Function to perform the conversion based on country
    def convert_income(row):
        country = row['adm0'].lower()  # Convert the country name to lowercase
        if country in conversion_factors:
            return row['incfarm'] / conversion_factors[country]
        else:
            return np.nan 

    # Apply the conversion function to the DataFrame
    df['incfarm'] = df.apply(convert_income, axis=1)
    
    
    up=df.quantile(.75)
    down=df.quantile(.25)
    #handling outliers (replacing upper 75% with mean, and lower 25% with mean
    numeric_cols=['costkgfert','farmbuyv', 'farmsalev',
       'incfarm','occ1wks',
       'sickdays', 'total_plotarea', 'avg_use_of_plot_in_years',
       'total_livestocks_owned', 'total_livestocks_born',
       'total_livestocks_lost', 'total_livestocks_purchased',
       'livestocks_avg_purchase_price', 'months_grazed_communal',
       'months_grazed_own', 'month_grazed_openland', 'total_livestocks_sold',
       'livestocks_avg_sales_price', 'avg_livestocks_product_used',
       'avg_livestocks_product_sold', 'avg_product_price',
       'transport_cropcost', 'pm_cropcost', 'storage_cropcost',
       'postharvest_croploss', 'other_cropcost', 'transport_lvscost',
       'pm_lvscost', 'storage_lvscost', 'postharvest_lvsloss', 'other_lvscost',
       'edu_level', 'ave_age', 'nmale', 'nfemale', 'mem_nfarmwrk',
       'mem_farmwrk',
       'season1_mean_area', 'season1_mean_qharv', 'season2_mean_qharv',
       'season1_mean_household_consumption',
       'season2_mean_household_consumption',
       'season1_mean_livestock_consumption', 'season1_mean_loss',
       'season2_mean_loss', 'season1_mean_sold', 'season2_mean_sold',
       'season1_mean_seed_used', 'season1_mean_seed_value',
       'season2_mean_seed_value', 'no_of_crop_types',
       'avg_yield_per_crop_type', 'season1_avg_fertilizer',
       'season2_avg_fertilizer', 'season1_avg_pesticide', 'avg_price_equip',
       'avg_lifespan_equip', 'avg_no_equipment', 'total_tax_paid',
       'number_of_laborers', 'days_spent_by_laborers',
       'livestock_number_of_laborers', 'days_spent_by_livestock_laborers',
       'labor_wage_payment', 'kind_payment']
    
    for col in numeric_cols:
        # Calculate the mean of the column
        col_mean = df[col].mean()

        # Replace values outside the range with the mean
        df[col] = df[col].apply(lambda val: col_mean if (val > up[col]) or (val < down[col]) else val)

    #cleaning season1s
    df['season1s']=df['season1s'].str.extract('([a-zA-Z]{2,11})')
    df['season1s']=df['season1s'].str.replace('(dd)','')
    df['season1s']=df['season1s'].str.replace('(ww)','')
    df['season1s']=df['season1s'].str.capitalize()
    df['season1s']=df['season1s'].replace(['October','November','April','June','July','Unknown','March','Sept'],
                             ['Oct','Nov','Apr','Jun','Jul',np.nan,'Mar','Sep'])

    #cleaning season1e
    df['season1e']=df['season1e'].str.extract('([a-zA-Z]{2,11})')
    df['season1e']=df['season1e'].str.replace('(dd)','')
    df['season1e']=df['season1e'].str.replace('(ww)','')
    df['season1e']=df['season1e'].str.capitalize()
    df['season1e']=df['season1e'].replace(['October','November','April','June','July','Unknown','March','Sept'],
                             ['Oct','Nov','Apr','Jun','Jul',np.nan,'Mar','Sep'])

    #cleaning season2s
    df['season2s']=df['season2s'].str.extract('([a-zA-Z]{2,11})')
    df['season2s']=df['season2s'].str.replace('(dd)','')
    df['season2s']=df['season2s'].str.replace('(ww)','')
    df['season2s']=df['season2s'].str.capitalize()
    df['season2s']=df['season2s'].replace(['October','November','April','June','July','Unknown','March','Sept',
                                           'December','Novemvre'],
                             ['Oct','Nov','Apr','Jun','Jul',np.nan,'Mar','Sep','Dec','Nov'])


    #cleaning season2e
    df['season2e']=df['season2e'].str.extract('([a-zA-Z]{2,11})')
    df['season2e']=df['season2e'].str.replace('(dd)','')
    df['season2e']=df['season2e'].str.replace('(ww)','')
    df['season2e']=df['season2e'].str.capitalize()
    df['season2e']=df['season2e'].replace(['October','November','April','June','July','Unknown','March','Sept',
                                           'December','Novemvre','August','September'],
                             ['Oct','Nov','Apr','Jun','Jul',np.nan,'Mar','Sep','Dec','Nov','Aug','Sep'])
    return df