# Sebastian Raschka 2014-2016
# mlxtend Machine Learning Library Extensions
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: BSD 3 clause

import numpy as np

def autompg_data():
    """Auto MPG dataset.

    Source: https://archive.ics.uci.edu/ml/datasets/Auto+MPG
    Number of samples: 392
    Continuous target variable: mpg

    Attributes:
    1) cylinders: multi-valued discrete
    2) displacement: continuous
    3) horsepower: continuous
    4) weight: continuous
    5) acceleration: continuous
    6) model year: multi-valued discrete
    7) origin: multi-valued discrete
    8) car name: string (unique for each instance)

    Returns
    --------
    X, y : [n_samples, n_features], [n_targets]
      X is the feature matrix with 392 auto samples as rows
      and 8 feature columns (6 rows with NaNs removed).
      y is a 1-dimensional array of the target MPG values.

    """
    X = np.array([
        [ 8,307.0,130.0,3504.0,12.0,70,1,"chevrolet chevelle malibu"],
        [ 8,350.0,165.0,3693.0,11.5,70,1,"buick skylark 320"],
        [ 8,318.0,150.0,3436.0,11.0,70,1,"plymouth satellite"],
        [ 8,304.0,150.0,3433.0,12.0,70,1,"amc rebel sst"],
        [ 8,302.0,140.0,3449.0,10.5,70,1,"ford torino"],
        [ 8,429.0,198.0,4341.0,10.0,70,1,"ford galaxie 500"],
        [ 8,454.0,220.0,4354.0,9.0,70,1,"chevrolet impala"],
        [ 8,440.0,215.0,4312.0,8.5,70,1,"plymouth fury iii"],
        [ 8,455.0,225.0,4425.0,10.0,70,1,"pontiac catalina"],
        [ 8,390.0,190.0,3850.0,8.5,70,1,"amc ambassador dpl"],
        [ 8,383.0,170.0,3563.0,10.0,70,1,"dodge challenger se"],
        [ 8,340.0,160.0,3609.0,8.0,70,1,"plymouth 'cuda 340"],
        [ 8,400.0,150.0,3761.0,9.5,70,1,"chevrolet monte carlo"],
        [ 8,455.0,225.0,3086.0,10.0,70,1,"buick estate wagon (sw)"],
        [ 4,113.0,95.0,2372.0,15.0,70,3,"toyota corona mark ii"],
        [ 6,198.0,95.0,2833.0,15.5,70,1,"plymouth duster"],
        [ 6,199.0,97.0,2774.0,15.5,70,1,"amc hornet"],
        [ 6,200.0,85.0,2587.0,16.0,70,1,"ford maverick"],
        [ 4,97.0,88.0,2130.0,14.5,70,3,"datsun pl510"],
        [ 4,97.0,46.0,1835.0,20.5,70,2,"volkswagen 1131 deluxe sedan"],
        [ 4,110.0,87.0,2672.0,17.5,70,2,"peugeot 504"],
        [ 4,107.0,90.0,2430.0,14.5,70,2,"audi 100 ls"],
        [ 4,104.0,95.0,2375.0,17.5,70,2,"saab 99e"],
        [ 4,121.0,113.0,2234.0,12.5,70,2,"bmw 2002"],
        [ 6,199.0,90.0,2648.0,15.0,70,1,"amc gremlin"],
        [ 8,360.0,215.0,4615.0,14.0,70,1,"ford f250"],
        [ 8,307.0,200.0,4376.0,15.0,70,1,"chevy c20"],
        [ 8,318.0,210.0,4382.0,13.5,70,1,"dodge d200"],
        [ 8,304.0,193.0,4732.0,18.5,70,1,"hi 1200d"],
        [ 4,97.0,88.0,2130.0,14.5,71,3,"datsun pl510"],
        [ 4,140.0,90.0,2264.0,15.5,71,1,"chevrolet vega 2300"],
        [ 4,113.0,95.0,2228.0,14.0,71,3,"toyota corona"],
        [ 6,232.0,100.0,2634.0,13.0,71,1,"amc gremlin"],
        [ 6,225.0,105.0,3439.0,15.5,71,1,"plymouth satellite custom"],
        [ 6,250.0,100.0,3329.0,15.5,71,1,"chevrolet chevelle malibu"],
        [ 6,250.0,88.0,3302.0,15.5,71,1,"ford torino 500"],
        [ 6,232.0,100.0,3288.0,15.5,71,1,"amc matador"],
        [ 8,350.0,165.0,4209.0,12.0,71,1,"chevrolet impala"],
        [ 8,400.0,175.0,4464.0,11.5,71,1,"pontiac catalina brougham"],
        [ 8,351.0,153.0,4154.0,13.5,71,1,"ford galaxie 500"],
        [ 8,318.0,150.0,4096.0,13.0,71,1,"plymouth fury iii"],
        [ 8,383.0,180.0,4955.0,11.5,71,1,"dodge monaco (sw)"],
        [ 8,400.0,170.0,4746.0,12.0,71,1,"ford country squire (sw)"],
        [ 8,400.0,175.0,5140.0,12.0,71,1,"pontiac safari (sw)"],
        [ 6,258.0,110.0,2962.0,13.5,71,1,"amc hornet sportabout (sw)"],
        [ 4,140.0,72.0,2408.0,19.0,71,1,"chevrolet vega (sw)"],
        [ 6,250.0,100.0,3282.0,15.0,71,1,"pontiac firebird"],
        [ 6,250.0,88.0,3139.0,14.5,71,1,"ford mustang"],
        [ 4,122.0,86.0,2220.0,14.0,71,1,"mercury capri 2000"],
        [ 4,116.0,90.0,2123.0,14.0,71,2,"opel 1900"],
        [ 4,79.0,70.0,2074.0,19.5,71,2,"peugeot 304"],
        [ 4,88.0,76.0,2065.0,14.5,71,2,"fiat 124b"],
        [ 4,71.0,65.0,1773.0,19.0,71,3,"toyota corolla 1200"],
        [ 4,72.0,69.0,1613.0,18.0,71,3,"datsun 1200"],
        [ 4,97.0,60.0,1834.0,19.0,71,2,"volkswagen model 111"],
        [ 4,91.0,70.0,1955.0,20.5,71,1,"plymouth cricket"],
        [ 4,113.0,95.0,2278.0,15.5,72,3,"toyota corona hardtop"],
        [ 4,97.5,80.0,2126.0,17.0,72,1,"dodge colt hardtop"],
        [ 4,97.0,54.0,2254.0,23.5,72,2,"volkswagen type 3"],
        [ 4,140.0,90.0,2408.0,19.5,72,1,"chevrolet vega"],
        [ 4,122.0,86.0,2226.0,16.5,72,1,"ford pinto runabout"],
        [ 8,350.0,165.0,4274.0,12.0,72,1,"chevrolet impala"],
        [ 8,400.0,175.0,4385.0,12.0,72,1,"pontiac catalina"],
        [ 8,318.0,150.0,4135.0,13.5,72,1,"plymouth fury iii"],
        [ 8,351.0,153.0,4129.0,13.0,72,1,"ford galaxie 500"],
        [ 8,304.0,150.0,3672.0,11.5,72,1,"amc ambassador sst"],
        [ 8,429.0,208.0,4633.0,11.0,72,1,"mercury marquis"],
        [ 8,350.0,155.0,4502.0,13.5,72,1,"buick lesabre custom"],
        [ 8,350.0,160.0,4456.0,13.5,72,1,"oldsmobile delta 88 royale"],
        [ 8,400.0,190.0,4422.0,12.5,72,1,"chrysler newport royal"],
        [ 3,70.0,97.0,2330.0,13.5,72,3,"mazda rx2 coupe"],
        [ 8,304.0,150.0,3892.0,12.5,72,1,"amc matador (sw)"],
        [ 8,307.0,130.0,4098.0,14.0,72,1,"chevrolet chevelle concours (sw)"],
        [ 8,302.0,140.0,4294.0,16.0,72,1,"ford gran torino (sw)"],
        [ 8,318.0,150.0,4077.0,14.0,72,1,"plymouth satellite custom (sw)"],
        [ 4,121.0,112.0,2933.0,14.5,72,2,"volvo 145e (sw)"],
        [ 4,121.0,76.0,2511.0,18.0,72,2,"volkswagen 411 (sw)"],
        [ 4,120.0,87.0,2979.0,19.5,72,2,"peugeot 504 (sw)"],
        [ 4,96.0,69.0,2189.0,18.0,72,2,"renault 12 (sw)"],
        [ 4,122.0,86.0,2395.0,16.0,72,1,"ford pinto (sw)"],
        [ 4,97.0,92.0,2288.0,17.0,72,3,"datsun 510 (sw)"],
        [ 4,120.0,97.0,2506.0,14.5,72,3,"toyouta corona mark ii (sw)"],
        [ 4,98.0,80.0,2164.0,15.0,72,1,"dodge colt (sw)"],
        [ 4,97.0,88.0,2100.0,16.5,72,3,"toyota corolla 1600 (sw)"],
        [ 8,350.0,175.0,4100.0,13.0,73,1,"buick century 350"],
        [ 8,304.0,150.0,3672.0,11.5,73,1,"amc matador"],
        [ 8,350.0,145.0,3988.0,13.0,73,1,"chevrolet malibu"],
        [ 8,302.0,137.0,4042.0,14.5,73,1,"ford gran torino"],
        [ 8,318.0,150.0,3777.0,12.5,73,1,"dodge coronet custom"],
        [ 8,429.0,198.0,4952.0,11.5,73,1,"mercury marquis brougham"],
        [ 8,400.0,150.0,4464.0,12.0,73,1,"chevrolet caprice classic"],
        [ 8,351.0,158.0,4363.0,13.0,73,1,"ford ltd"],
        [ 8,318.0,150.0,4237.0,14.5,73,1,"plymouth fury gran sedan"],
        [ 8,440.0,215.0,4735.0,11.0,73,1,"chrysler new yorker brougham"],
        [ 8,455.0,225.0,4951.0,11.0,73,1,"buick electra 225 custom"],
        [ 8,360.0,175.0,3821.0,11.0,73,1,"amc ambassador brougham"],
        [ 6,225.0,105.0,3121.0,16.5,73,1,"plymouth valiant"],
        [ 6,250.0,100.0,3278.0,18.0,73,1,"chevrolet nova custom"],
        [ 6,232.0,100.0,2945.0,16.0,73,1,"amc hornet"],
        [ 6,250.0,88.0,3021.0,16.5,73,1,"ford maverick"],
        [ 6,198.0,95.0,2904.0,16.0,73,1,"plymouth duster"],
        [ 4,97.0,46.0,1950.0,21.0,73,2,"volkswagen super beetle"],
        [ 8,400.0,150.0,4997.0,14.0,73,1,"chevrolet impala"],
        [ 8,400.0,167.0,4906.0,12.5,73,1,"ford country"],
        [ 8,360.0,170.0,4654.0,13.0,73,1,"plymouth custom suburb"],
        [ 8,350.0,180.0,4499.0,12.5,73,1,"oldsmobile vista cruiser"],
        [ 6,232.0,100.0,2789.0,15.0,73,1,"amc gremlin"],
        [ 4,97.0,88.0,2279.0,19.0,73,3,"toyota carina"],
        [ 4,140.0,72.0,2401.0,19.5,73,1,"chevrolet vega"],
        [ 4,108.0,94.0,2379.0,16.5,73,3,"datsun 610"],
        [ 3,70.0,90.0,2124.0,13.5,73,3,"maxda rx3"],
        [ 4,122.0,85.0,2310.0,18.5,73,1,"ford pinto"],
        [ 6,155.0,107.0,2472.0,14.0,73,1,"mercury capri v6"],
        [ 4,98.0,90.0,2265.0,15.5,73,2,"fiat 124 sport coupe"],
        [ 8,350.0,145.0,4082.0,13.0,73,1,"chevrolet monte carlo s"],
        [ 8,400.0,230.0,4278.0,9.5,73,1,"pontiac grand prix"],
        [ 4,68.0,49.0,1867.0,19.5,73,2,"fiat 128"],
        [ 4,116.0,75.0,2158.0,15.5,73,2,"opel manta"],
        [ 4,114.0,91.0,2582.0,14.0,73,2,"audi 100ls"],
        [ 4,121.0,112.0,2868.0,15.5,73,2,"volvo 144ea"],
        [ 8,318.0,150.0,3399.0,11.0,73,1,"dodge dart custom"],
        [ 4,121.0,110.0,2660.0,14.0,73,2,"saab 99le"],
        [ 6,156.0,122.0,2807.0,13.5,73,3,"toyota mark ii"],
        [ 8,350.0,180.0,3664.0,11.0,73,1,"oldsmobile omega"],
        [ 6,198.0,95.0,3102.0,16.5,74,1,"plymouth duster"],
        [ 6,232.0,100.0,2901.0,16.0,74,1,"amc hornet"],
        [ 6,250.0,100.0,3336.0,17.0,74,1,"chevrolet nova"],
        [ 4,79.0,67.0,1950.0,19.0,74,3,"datsun b210"],
        [ 4,122.0,80.0,2451.0,16.5,74,1,"ford pinto"],
        [ 4,71.0,65.0,1836.0,21.0,74,3,"toyota corolla 1200"],
        [ 4,140.0,75.0,2542.0,17.0,74,1,"chevrolet vega"],
        [ 6,250.0,100.0,3781.0,17.0,74,1,"chevrolet chevelle malibu classic"],
        [ 6,258.0,110.0,3632.0,18.0,74,1,"amc matador"],
        [ 6,225.0,105.0,3613.0,16.5,74,1,"plymouth satellite sebring"],
        [ 8,302.0,140.0,4141.0,14.0,74,1,"ford gran torino"],
        [ 8,350.0,150.0,4699.0,14.5,74,1,"buick century luxus (sw)"],
        [ 8,318.0,150.0,4457.0,13.5,74,1,"dodge coronet custom (sw)"],
        [ 8,302.0,140.0,4638.0,16.0,74,1,"ford gran torino (sw)"],
        [ 8,304.0,150.0,4257.0,15.5,74,1,"amc matador (sw)"],
        [ 4,98.0,83.0,2219.0,16.5,74,2,"audi fox"],
        [ 4,79.0,67.0,1963.0,15.5,74,2,"volkswagen dasher"],
        [ 4,97.0,78.0,2300.0,14.5,74,2,"opel manta"],
        [ 4,76.0,52.0,1649.0,16.5,74,3,"toyota corona"],
        [ 4,83.0,61.0,2003.0,19.0,74,3,"datsun 710"],
        [ 4,90.0,75.0,2125.0,14.5,74,1,"dodge colt"],
        [ 4,90.0,75.0,2108.0,15.5,74,2,"fiat 128"],
        [ 4,116.0,75.0,2246.0,14.0,74,2,"fiat 124 tc"],
        [ 4,120.0,97.0,2489.0,15.0,74,3,"honda civic"],
        [ 4,108.0,93.0,2391.0,15.5,74,3,"subaru"],
        [ 4,79.0,67.0,2000.0,16.0,74,2,"fiat x1.9"],
        [ 6,225.0,95.0,3264.0,16.0,75,1,"plymouth valiant custom"],
        [ 6,250.0,105.0,3459.0,16.0,75,1,"chevrolet nova"],
        [ 6,250.0,72.0,3432.0,21.0,75,1,"mercury monarch"],
        [ 6,250.0,72.0,3158.0,19.5,75,1,"ford maverick"],
        [ 8,400.0,170.0,4668.0,11.5,75,1,"pontiac catalina"],
        [ 8,350.0,145.0,4440.0,14.0,75,1,"chevrolet bel air"],
        [ 8,318.0,150.0,4498.0,14.5,75,1,"plymouth grand fury"],
        [ 8,351.0,148.0,4657.0,13.5,75,1,"ford ltd"],
        [ 6,231.0,110.0,3907.0,21.0,75,1,"buick century"],
        [ 6,250.0,105.0,3897.0,18.5,75,1,"chevroelt chevelle malibu"],
        [ 6,258.0,110.0,3730.0,19.0,75,1,"amc matador"],
        [ 6,225.0,95.0,3785.0,19.0,75,1,"plymouth fury"],
        [ 6,231.0,110.0,3039.0,15.0,75,1,"buick skyhawk"],
        [ 8,262.0,110.0,3221.0,13.5,75,1,"chevrolet monza 2+2"],
        [ 8,302.0,129.0,3169.0,12.0,75,1,"ford mustang ii"],
        [ 4,97.0,75.0,2171.0,16.0,75,3,"toyota corolla"],
        [ 4,140.0,83.0,2639.0,17.0,75,1,"ford pinto"],
        [ 6,232.0,100.0,2914.0,16.0,75,1,"amc gremlin"],
        [ 4,140.0,78.0,2592.0,18.5,75,1,"pontiac astro"],
        [ 4,134.0,96.0,2702.0,13.5,75,3,"toyota corona"],
        [ 4,90.0,71.0,2223.0,16.5,75,2,"volkswagen dasher"],
        [ 4,119.0,97.0,2545.0,17.0,75,3,"datsun 710"],
        [ 6,171.0,97.0,2984.0,14.5,75,1,"ford pinto"],
        [ 4,90.0,70.0,1937.0,14.0,75,2,"volkswagen rabbit"],
        [ 6,232.0,90.0,3211.0,17.0,75,1,"amc pacer"],
        [ 4,115.0,95.0,2694.0,15.0,75,2,"audi 100ls"],
        [ 4,120.0,88.0,2957.0,17.0,75,2,"peugeot 504"],
        [ 4,121.0,98.0,2945.0,14.5,75,2,"volvo 244dl"],
        [ 4,121.0,115.0,2671.0,13.5,75,2,"saab 99le"],
        [ 4,91.0,53.0,1795.0,17.5,75,3,"honda civic cvcc"],
        [ 4,107.0,86.0,2464.0,15.5,76,2,"fiat 131"],
        [ 4,116.0,81.0,2220.0,16.9,76,2,"opel 1900"],
        [ 4,140.0,92.0,2572.0,14.9,76,1,"capri ii"],
        [ 4,98.0,79.0,2255.0,17.7,76,1,"dodge colt"],
        [ 4,101.0,83.0,2202.0,15.3,76,2,"renault 12tl"],
        [ 8,305.0,140.0,4215.0,13.0,76,1,"chevrolet chevelle malibu classic"],
        [ 8,318.0,150.0,4190.0,13.0,76,1,"dodge coronet brougham"],
        [ 8,304.0,120.0,3962.0,13.9,76,1,"amc matador"],
        [ 8,351.0,152.0,4215.0,12.8,76,1,"ford gran torino"],
        [ 6,225.0,100.0,3233.0,15.4,76,1,"plymouth valiant"],
        [ 6,250.0,105.0,3353.0,14.5,76,1,"chevrolet nova"],
        [ 6,200.0,81.0,3012.0,17.6,76,1,"ford maverick"],
        [ 6,232.0,90.0,3085.0,17.6,76,1,"amc hornet"],
        [ 4,85.0,52.0,2035.0,22.2,76,1,"chevrolet chevette"],
        [ 4,98.0,60.0,2164.0,22.1,76,1,"chevrolet woody"],
        [ 4,90.0,70.0,1937.0,14.2,76,2,"vw rabbit"],
        [ 4,91.0,53.0,1795.0,17.4,76,3,"honda civic"],
        [ 6,225.0,100.0,3651.0,17.7,76,1,"dodge aspen se"],
        [ 6,250.0,78.0,3574.0,21.0,76,1,"ford granada ghia"],
        [ 6,250.0,110.0,3645.0,16.2,76,1,"pontiac ventura sj"],
        [ 6,258.0,95.0,3193.0,17.8,76,1,"amc pacer d/l"],
        [ 4,97.0,71.0,1825.0,12.2,76,2,"volkswagen rabbit"],
        [ 4,85.0,70.0,1990.0,17.0,76,3,"datsun b-210"],
        [ 4,97.0,75.0,2155.0,16.4,76,3,"toyota corolla"],
        [ 4,140.0,72.0,2565.0,13.6,76,1,"ford pinto"],
        [ 4,130.0,102.0,3150.0,15.7,76,2,"volvo 245"],
        [ 8,318.0,150.0,3940.0,13.2,76,1,"plymouth volare premier v8"],
        [ 4,120.0,88.0,3270.0,21.9,76,2,"peugeot 504"],
        [ 6,156.0,108.0,2930.0,15.5,76,3,"toyota mark ii"],
        [ 6,168.0,120.0,3820.0,16.7,76,2,"mercedes-benz 280s"],
        [ 8,350.0,180.0,4380.0,12.1,76,1,"cadillac seville"],
        [ 8,350.0,145.0,4055.0,12.0,76,1,"chevy c10"],
        [ 8,302.0,130.0,3870.0,15.0,76,1,"ford f108"],
        [ 8,318.0,150.0,3755.0,14.0,76,1,"dodge d100"],
        [ 4,98.0,68.0,2045.0,18.5,77,3,"honda accord cvcc"],
        [ 4,111.0,80.0,2155.0,14.8,77,1,"buick opel isuzu deluxe"],
        [ 4,79.0,58.0,1825.0,18.6,77,2,"renault 5 gtl"],
        [ 4,122.0,96.0,2300.0,15.5,77,1,"plymouth arrow gs"],
        [ 4,85.0,70.0,1945.0,16.8,77,3,"datsun f-10 hatchback"],
        [ 8,305.0,145.0,3880.0,12.5,77,1,"chevrolet caprice classic"],
        [ 8,260.0,110.0,4060.0,19.0,77,1,"oldsmobile cutlass supreme"],
        [ 8,318.0,145.0,4140.0,13.7,77,1,"dodge monaco brougham"],
        [ 8,302.0,130.0,4295.0,14.9,77,1,"mercury cougar brougham"],
        [ 6,250.0,110.0,3520.0,16.4,77,1,"chevrolet concours"],
        [ 6,231.0,105.0,3425.0,16.9,77,1,"buick skylark"],
        [ 6,225.0,100.0,3630.0,17.7,77,1,"plymouth volare custom"],
        [ 6,250.0,98.0,3525.0,19.0,77,1,"ford granada"],
        [ 8,400.0,180.0,4220.0,11.1,77,1,"pontiac grand prix lj"],
        [ 8,350.0,170.0,4165.0,11.4,77,1,"chevrolet monte carlo landau"],
        [ 8,400.0,190.0,4325.0,12.2,77,1,"chrysler cordoba"],
        [ 8,351.0,149.0,4335.0,14.5,77,1,"ford thunderbird"],
        [ 4,97.0,78.0,1940.0,14.5,77,2,"volkswagen rabbit custom"],
        [ 4,151.0,88.0,2740.0,16.0,77,1,"pontiac sunbird coupe"],
        [ 4,97.0,75.0,2265.0,18.2,77,3,"toyota corolla liftback"],
        [ 4,140.0,89.0,2755.0,15.8,77,1,"ford mustang ii 2+2"],
        [ 4,98.0,63.0,2051.0,17.0,77,1,"chevrolet chevette"],
        [ 4,98.0,83.0,2075.0,15.9,77,1,"dodge colt m/m"],
        [ 4,97.0,67.0,1985.0,16.4,77,3,"subaru dl"],
        [ 4,97.0,78.0,2190.0,14.1,77,2,"volkswagen dasher"],
        [ 6,146.0,97.0,2815.0,14.5,77,3,"datsun 810"],
        [ 4,121.0,110.0,2600.0,12.8,77,2,"bmw 320i"],
        [ 3,80.0,110.0,2720.0,13.5,77,3,"mazda rx-4"],
        [ 4,90.0,48.0,1985.0,21.5,78,2,"volkswagen rabbit custom diesel"],
        [ 4,98.0,66.0,1800.0,14.4,78,1,"ford fiesta"],
        [ 4,78.0,52.0,1985.0,19.4,78,3,"mazda glc deluxe"],
        [ 4,85.0,70.0,2070.0,18.6,78,3,"datsun b210 gx"],
        [ 4,91.0,60.0,1800.0,16.4,78,3,"honda civic cvcc"],
        [ 8,260.0,110.0,3365.0,15.5,78,1,"oldsmobile cutlass salon brougham"],
        [ 8,318.0,140.0,3735.0,13.2,78,1,"dodge diplomat"],
        [ 8,302.0,139.0,3570.0,12.8,78,1,"mercury monarch ghia"],
        [ 6,231.0,105.0,3535.0,19.2,78,1,"pontiac phoenix lj"],
        [ 6,200.0,95.0,3155.0,18.2,78,1,"chevrolet malibu"],
        [ 6,200.0,85.0,2965.0,15.8,78,1,"ford fairmont (auto)"],
        [ 4,140.0,88.0,2720.0,15.4,78,1,"ford fairmont (man)"],
        [ 6,225.0,100.0,3430.0,17.2,78,1,"plymouth volare"],
        [ 6,232.0,90.0,3210.0,17.2,78,1,"amc concord"],
        [ 6,231.0,105.0,3380.0,15.8,78,1,"buick century special"],
        [ 6,200.0,85.0,3070.0,16.7,78,1,"mercury zephyr"],
        [ 6,225.0,110.0,3620.0,18.7,78,1,"dodge aspen"],
        [ 6,258.0,120.0,3410.0,15.1,78,1,"amc concord d/l"],
        [ 8,305.0,145.0,3425.0,13.2,78,1,"chevrolet monte carlo landau"],
        [ 6,231.0,165.0,3445.0,13.4,78,1,"buick regal sport coupe (turbo)"],
        [ 8,302.0,139.0,3205.0,11.2,78,1,"ford futura"],
        [ 8,318.0,140.0,4080.0,13.7,78,1,"dodge magnum xe"],
        [ 4,98.0,68.0,2155.0,16.5,78,1,"chevrolet chevette"],
        [ 4,134.0,95.0,2560.0,14.2,78,3,"toyota corona"],
        [ 4,119.0,97.0,2300.0,14.7,78,3,"datsun 510"],
        [ 4,105.0,75.0,2230.0,14.5,78,1,"dodge omni"],
        [ 4,134.0,95.0,2515.0,14.8,78,3,"toyota celica gt liftback"],
        [ 4,156.0,105.0,2745.0,16.7,78,1,"plymouth sapporo"],
        [ 4,151.0,85.0,2855.0,17.6,78,1,"oldsmobile starfire sx"],
        [ 4,119.0,97.0,2405.0,14.9,78,3,"datsun 200-sx"],
        [ 5,131.0,103.0,2830.0,15.9,78,2,"audi 5000"],
        [ 6,163.0,125.0,3140.0,13.6,78,2,"volvo 264gl"],
        [ 4,121.0,115.0,2795.0,15.7,78,2,"saab 99gle"],
        [ 6,163.0,133.0,3410.0,15.8,78,2,"peugeot 604sl"],
        [ 4,89.0,71.0,1990.0,14.9,78,2,"volkswagen scirocco"],
        [ 4,98.0,68.0,2135.0,16.6,78,3,"honda accord lx"],
        [ 6,231.0,115.0,3245.0,15.4,79,1,"pontiac lemans v6"],
        [ 6,200.0,85.0,2990.0,18.2,79,1,"mercury zephyr 6"],
        [ 4,140.0,88.0,2890.0,17.3,79,1,"ford fairmont 4"],
        [ 6,232.0,90.0,3265.0,18.2,79,1,"amc concord dl 6"],
        [ 6,225.0,110.0,3360.0,16.6,79,1,"dodge aspen 6"],
        [ 8,305.0,130.0,3840.0,15.4,79,1,"chevrolet caprice classic"],
        [ 8,302.0,129.0,3725.0,13.4,79,1,"ford ltd landau"],
        [ 8,351.0,138.0,3955.0,13.2,79,1,"mercury grand marquis"],
        [ 8,318.0,135.0,3830.0,15.2,79,1,"dodge st. regis"],
        [ 8,350.0,155.0,4360.0,14.9,79,1,"buick estate wagon (sw)"],
        [ 8,351.0,142.0,4054.0,14.3,79,1,"ford country squire (sw)"],
        [ 8,267.0,125.0,3605.0,15.0,79,1,"chevrolet malibu classic (sw)"],
        [ 8,360.0,150.0,3940.0,13.0,79,1,"chrysler lebaron town @ country (sw)"],
        [ 4,89.0,71.0,1925.0,14.0,79,2,"vw rabbit custom"],
        [ 4,86.0,65.0,1975.0,15.2,79,3,"maxda glc deluxe"],
        [ 4,98.0,80.0,1915.0,14.4,79,1,"dodge colt hatchback custom"],
        [ 4,121.0,80.0,2670.0,15.0,79,1,"amc spirit dl"],
        [ 5,183.0,77.0,3530.0,20.1,79,2,"mercedes benz 300d"],
        [ 8,350.0,125.0,3900.0,17.4,79,1,"cadillac eldorado"],
        [ 4,141.0,71.0,3190.0,24.8,79,2,"peugeot 504"],
        [ 8,260.0,90.0,3420.0,22.2,79,1,"oldsmobile cutlass salon brougham"],
        [ 4,105.0,70.0,2200.0,13.2,79,1,"plymouth horizon"],
        [ 4,105.0,70.0,2150.0,14.9,79,1,"plymouth horizon tc3"],
        [ 4,85.0,65.0,2020.0,19.2,79,3,"datsun 210"],
        [ 4,91.0,69.0,2130.0,14.7,79,2,"fiat strada custom"],
        [ 4,151.0,90.0,2670.0,16.0,79,1,"buick skylark limited"],
        [ 6,173.0,115.0,2595.0,11.3,79,1,"chevrolet citation"],
        [ 6,173.0,115.0,2700.0,12.9,79,1,"oldsmobile omega brougham"],
        [ 4,151.0,90.0,2556.0,13.2,79,1,"pontiac phoenix"],
        [ 4,98.0,76.0,2144.0,14.7,80,2,"vw rabbit"],
        [ 4,89.0,60.0,1968.0,18.8,80,3,"toyota corolla tercel"],
        [ 4,98.0,70.0,2120.0,15.5,80,1,"chevrolet chevette"],
        [ 4,86.0,65.0,2019.0,16.4,80,3,"datsun 310"],
        [ 4,151.0,90.0,2678.0,16.5,80,1,"chevrolet citation"],
        [ 4,140.0,88.0,2870.0,18.1,80,1,"ford fairmont"],
        [ 4,151.0,90.0,3003.0,20.1,80,1,"amc concord"],
        [ 6,225.0,90.0,3381.0,18.7,80,1,"dodge aspen"],
        [ 4,97.0,78.0,2188.0,15.8,80,2,"audi 4000"],
        [ 4,134.0,90.0,2711.0,15.5,80,3,"toyota corona liftback"],
        [ 4,120.0,75.0,2542.0,17.5,80,3,"mazda 626"],
        [ 4,119.0,92.0,2434.0,15.0,80,3,"datsun 510 hatchback"],
        [ 4,108.0,75.0,2265.0,15.2,80,3,"toyota corolla"],
        [ 4,86.0,65.0,2110.0,17.9,80,3,"mazda glc"],
        [ 4,156.0,105.0,2800.0,14.4,80,1,"dodge colt"],
        [ 4,85.0,65.0,2110.0,19.2,80,3,"datsun 210"],
        [ 4,90.0,48.0,2085.0,21.7,80,2,"vw rabbit c (diesel)"],
        [ 4,90.0,48.0,2335.0,23.7,80,2,"vw dasher (diesel)"],
        [ 5,121.0,67.0,2950.0,19.9,80,2,"audi 5000s (diesel)"],
        [ 4,146.0,67.0,3250.0,21.8,80,2,"mercedes-benz 240d"],
        [ 4,91.0,67.0,1850.0,13.8,80,3,"honda civic 1500 gl"],
        [ 4,97.0,67.0,2145.0,18.0,80,3,"subaru dl"],
        [ 4,89.0,62.0,1845.0,15.3,80,2,"vokswagen rabbit"],
        [ 6,168.0,132.0,2910.0,11.4,80,3,"datsun 280-zx"],
        [ 3,70.0,100.0,2420.0,12.5,80,3,"mazda rx-7 gs"],
        [ 4,122.0,88.0,2500.0,15.1,80,2,"triumph tr7 coupe"],
        [ 4,107.0,72.0,2290.0,17.0,80,3,"honda accord"],
        [ 4,135.0,84.0,2490.0,15.7,81,1,"plymouth reliant"],
        [ 4,151.0,84.0,2635.0,16.4,81,1,"buick skylark"],
        [ 4,156.0,92.0,2620.0,14.4,81,1,"dodge aries wagon (sw)"],
        [ 6,173.0,110.0,2725.0,12.6,81,1,"chevrolet citation"],
        [ 4,135.0,84.0,2385.0,12.9,81,1,"plymouth reliant"],
        [ 4,79.0,58.0,1755.0,16.9,81,3,"toyota starlet"],
        [ 4,86.0,64.0,1875.0,16.4,81,1,"plymouth champ"],
        [ 4,81.0,60.0,1760.0,16.1,81,3,"honda civic 1300"],
        [ 4,97.0,67.0,2065.0,17.8,81,3,"subaru"],
        [ 4,85.0,65.0,1975.0,19.4,81,3,"datsun 210 mpg"],
        [ 4,89.0,62.0,2050.0,17.3,81,3,"toyota tercel"],
        [ 4,91.0,68.0,1985.0,16.0,81,3,"mazda glc 4"],
        [ 4,105.0,63.0,2215.0,14.9,81,1,"plymouth horizon 4"],
        [ 4,98.0,65.0,2045.0,16.2,81,1,"ford escort 4w"],
        [ 4,98.0,65.0,2380.0,20.7,81,1,"ford escort 2h"],
        [ 4,105.0,74.0,2190.0,14.2,81,2,"volkswagen jetta"],
        [ 4,107.0,75.0,2210.0,14.4,81,3,"honda prelude"],
        [ 4,108.0,75.0,2350.0,16.8,81,3,"toyota corolla"],
        [ 4,119.0,100.0,2615.0,14.8,81,3,"datsun 200sx"],
        [ 4,120.0,74.0,2635.0,18.3,81,3,"mazda 626"],
        [ 4,141.0,80.0,3230.0,20.4,81,2,"peugeot 505s turbo diesel"],
        [ 6,145.0,76.0,3160.0,19.6,81,2,"volvo diesel"],
        [ 6,168.0,116.0,2900.0,12.6,81,3,"toyota cressida"],
        [ 6,146.0,120.0,2930.0,13.8,81,3,"datsun 810 maxima"],
        [ 6,231.0,110.0,3415.0,15.8,81,1,"buick century"],
        [ 8,350.0,105.0,3725.0,19.0,81,1,"oldsmobile cutlass ls"],
        [ 6,200.0,88.0,3060.0,17.1,81,1,"ford granada gl"],
        [ 6,225.0,85.0,3465.0,16.6,81,1,"chrysler lebaron salon"],
        [ 4,112.0,88.0,2605.0,19.6,82,1,"chevrolet cavalier"],
        [ 4,112.0,88.0,2640.0,18.6,82,1,"chevrolet cavalier wagon"],
        [ 4,112.0,88.0,2395.0,18.0,82,1,"chevrolet cavalier 2-door"],
        [ 4,112.0,85.0,2575.0,16.2,82,1,"pontiac j2000 se hatchback"],
        [ 4,135.0,84.0,2525.0,16.0,82,1,"dodge aries se"],
        [ 4,151.0,90.0,2735.0,18.0,82,1,"pontiac phoenix"],
        [ 4,140.0,92.0,2865.0,16.4,82,1,"ford fairmont futura"],
        [ 4,105.0,74.0,1980.0,15.3,82,2,"volkswagen rabbit l"],
        [ 4,91.0,68.0,2025.0,18.2,82,3,"mazda glc custom l"],
        [ 4,91.0,68.0,1970.0,17.6,82,3,"mazda glc custom"],
        [ 4,105.0,63.0,2125.0,14.7,82,1,"plymouth horizon miser"],
        [ 4,98.0,70.0,2125.0,17.3,82,1,"mercury lynx l"],
        [ 4,120.0,88.0,2160.0,14.5,82,3,"nissan stanza xe"],
        [ 4,107.0,75.0,2205.0,14.5,82,3,"honda accord"],
        [ 4,108.0,70.0,2245.0,16.9,82,3,"toyota corolla"],
        [ 4,91.0,67.0,1965.0,15.0,82,3,"honda civic"],
        [ 4,91.0,67.0,1965.0,15.7,82,3,"honda civic (auto)"],
        [ 4,91.0,67.0,1995.0,16.2,82,3,"datsun 310 gx"],
        [ 6,181.0,110.0,2945.0,16.4,82,1,"buick century limited"],
        [ 6,262.0,85.0,3015.0,17.0,82,1,"oldsmobile cutlass ciera (diesel)"],
        [ 4,156.0,92.0,2585.0,14.5,82,1,"chrysler lebaron medallion"],
        [ 6,232.0,112.0,2835.0,14.7,82,1,"ford granada l"],
        [ 4,144.0,96.0,2665.0,13.9,82,3,"toyota celica gt"],
        [ 4,135.0,84.0,2370.0,13.0,82,1,"dodge charger 2.2"],
        [ 4,151.0,90.0,2950.0,17.3,82,1,"chevrolet camaro"],
        [ 4,140.0,86.0,2790.0,15.6,82,1,"ford mustang gl"],
        [ 4,97.0,52.0,2130.0,24.6,82,2,"vw pickup"],
        [ 4,135.0,84.0,2295.0,11.6,82,1,"dodge rampage"],
        [ 4,120.0,79.0,2625.0,18.6,82,1,"ford ranger"],
        [ 4,119.0,82.0,2720.0,19.4,82,1,"chevy s-10"]])

    y = np.array([
        18.0,15.0,18.0,16.0,17.0,15.0,14.0,14.0,14.0,15.0,
        15.0,14.0,15.0,14.0,24.0,22.0,18.0,21.0,27.0,26.0,
        25.0,24.0,25.0,26.0,21.0,10.0,10.0,11.0,9.0,27.0,
        28.0,25.0,19.0,16.0,17.0,19.0,18.0,14.0,14.0,14.0,
        14.0,12.0,13.0,13.0,18.0,22.0,19.0,18.0,23.0,28.0,
        30.0,30.0,31.0,35.0,27.0,26.0,24.0,25.0,23.0,20.0,
        21.0,13.0,14.0,15.0,14.0,17.0,11.0,13.0,12.0,13.0,
        19.0,15.0,13.0,13.0,14.0,18.0,22.0,21.0,26.0,22.0,
        28.0,23.0,28.0,27.0,13.0,14.0,13.0,14.0,15.0,12.0,
        13.0,13.0,14.0,13.0,12.0,13.0,18.0,16.0,18.0,18.0,
        23.0,26.0,11.0,12.0,13.0,12.0,18.0,20.0,21.0,22.0,
        18.0,19.0,21.0,26.0,15.0,16.0,29.0,24.0,20.0,19.0,
        15.0,24.0,20.0,11.0,20.0,19.0,15.0,31.0,26.0,32.0,
        25.0,16.0,16.0,18.0,16.0,13.0,14.0,14.0,14.0,29.0,
        26.0,26.0,31.0,32.0,28.0,24.0,26.0,24.0,26.0,31.0,
        19.0,18.0,15.0,15.0,16.0,15.0,16.0,14.0,17.0,16.0,
        15.0,18.0,21.0,20.0,13.0,29.0,23.0,20.0,23.0,24.0,
        25.0,24.0,18.0,29.0,19.0,23.0,23.0,22.0,25.0,33.0,
        28.0,25.0,25.0,26.0,27.0,17.5,16.0,15.5,14.5,22.0,
        22.0,24.0,22.5,29.0,24.5,29.0,33.0,20.0,18.0,18.5,
        17.5,29.5,32.0,28.0,26.5,20.0,13.0,19.0,19.0,16.5,
        16.5,13.0,13.0,13.0,31.5,30.0,36.0,25.5,33.5,17.5,
        17.0,15.5,15.0,17.5,20.5,19.0,18.5,16.0,15.5,15.5,
        16.0,29.0,24.5,26.0,25.5,30.5,33.5,30.0,30.5,22.0,
        21.5,21.5,43.1,36.1,32.8,39.4,36.1,19.9,19.4,20.2,
        19.2,20.5,20.2,25.1,20.5,19.4,20.6,20.8,18.6,18.1,
        19.2,17.7,18.1,17.5,30.0,27.5,27.2,30.9,21.1,23.2,
        23.8,23.9,20.3,17.0,21.6,16.2,31.5,29.5,21.5,19.8,
        22.3,20.2,20.6,17.0,17.6,16.5,18.2,16.9,15.5,19.2,
        18.5,31.9,34.1,35.7,27.4,25.4,23.0,27.2,23.9,34.2,
        34.5,31.8,37.3,28.4,28.8,26.8,33.5,41.5,38.1,32.1,
        37.2,28.0,26.4,24.3,19.1,34.3,29.8,31.3,37.0,32.2,
        46.6,27.9,40.8,44.3,43.4,36.4,30.0,44.6,33.8,29.8,
        32.7,23.7,35.0,32.4,27.2,26.6,25.8,23.5,30.0,39.1,
        39.0,35.1,32.3,37.0,37.7,34.1,34.7,34.4,29.9,33.0,
        33.7,32.4,32.9,31.6,28.1,30.7,25.4,24.2,22.4,26.6,
        20.2,17.6,28.0,27.0,34.0,31.0,29.0,27.0,24.0,36.0,
        37.0,31.0,38.0,36.0,36.0,36.0,34.0,38.0,32.0,38.0,
        25.0,38.0,26.0,22.0,32.0,36.0,27.0,27.0,44.0,32.0,
        28.0,31.0 ])

    return X, y