import pandas as pd
avg_bmi = {'male': 25.0,'female':24.0}
food_df1 = pd.read_csv("data/nndb_flat.csv")
food_df2 = food_df1.iloc[:,0:13]
food_df2 =food_df2.dropna(axis = 'columns', how ='any')
food_df3 =food_df2.drop(['FoodGroup','ShortDescrip'], axis =1)

print(food_df3)

def recommend_Energy_kcal(food_df3,avg_bmi,input_height,input_weight,input_gender):
    bmi = input_weight/input_height **2
    if bmi > avg_bmi[input_gender]:
        #person is above BMI, RECOMMEND LOWEST ENERGY ITEM
        return food_df3.sort_values(by = 'Energy_kcal',ascending =True).iloc[0]['Descrip']
    else:
        #person is below average bmi, recommend highest energy item
        return food_df3.sort_values(by="Energy_kcal",ascending=False).iloc[0]['Descrip']

    print(recommend_Energy_kcal(food_df3, avg_bmi, 1.99,50,'male'))#skinny person
    print(recommend_Energy_kcal(food_df3,avg_bmi,1.70,80,'male')) ##overweight person


def recommend_Protein_g(food_df3,avg_bmi,input_height,input_weight,input_gender):
    bmi = input_weight/input_height **2
    if bmi > avg_bmi[input_gender]:
        #person is above BMI, RECOMMEND LOWEST ENERGY ITEM
        return food_df3.sort_values(by = 'Protein_g',ascending =True).iloc[0]['Descrip']
    else:
        #person is below average bmi, recommend highest energy item
        return food_df3.sort_values(by="Protein_g",ascending=False).iloc[0]['Descrip']

    print(recommend_Protein_g(food_df3,avg_bmi,1.70,80,'male'))
    print(recommend_Protein_g(food_df3, avg_bmi, 1.99,50,'male'))


def recommend_Fat_g(food_df3,avg_bmi,input_height,input_weight,input_gender):
    bmi = input_weight/input_height **2
    if bmi > avg_bmi[input_gender]:
        #person is above BMI, RECOMMEND LOWEST ENERGY ITEM
        return food_df3.sort_values(by = 'Fat_g',ascending =True).iloc[0]['Descrip']
    else:
        #person is below average bmi, recommend highest energy item
        return food_df3.sort_values(by="Fat_g",ascending=False).iloc[0]['Descrip']

    print(recommend_Fat_g(food_df3,avg_bmi,1.70,80,'male'))
    print(recommend_Fat_g(food_df3, avg_bmi, 1.99,50,'male'))



def recommend_Carb_g(food_df3,avg_bmi,input_height,input_weight,input_gender):
    bmi = input_weight/input_height **2
    if bmi > avg_bmi[input_gender]:
        #person is above BMI, RECOMMEND LOWEST ENERGY ITEM
        return food_df3.sort_values(by = 'Carb_g',ascending =True).iloc[0]['Descrip']
    else:
        #person is below average bmi, recommend highest energy item
        return food_df3.sort_values(by="Carb_g",ascending=False).iloc[0]['Descrip']
    print(recommend_Carb_g(food_df3,avg_bmi,2.70,80,'male'))

    print(recommend_Carb_g(food_df3,avg_bmi,1.70,90,'female'))


def recommend_Sugar_g(food_df3,avg_bmi,input_height,input_weight,input_gender):
    bmi = input_weight/input_height **2
    if bmi > avg_bmi[input_gender]:
        #person is above BMI, RECOMMEND LOWEST ENERGY ITEM
        return food_df3.sort_values(by = 'Sugar_g',ascending =True).iloc[0]['Descrip']
    else:
        #person is below average bmi, recommend highest energy item
        return food_df3.sort_values(by="Sugar_g",ascending=False).iloc[0]['Descrip']

    print(recommend_Sugar_g(food_df3, avg_bmi, 1.99,50,'male'))

    print(recommend_Sugar_g(food_df3,avg_bmi,1.70,80,'male'))


def recommend_Fiber_g(food_df3,avg_bmi,input_height,input_weight,input_gender):
    bmi = input_weight/input_height **2
    if bmi > avg_bmi[input_gender]:
        #person is above BMI, RECOMMEND LOWEST ENERGY ITEM
        return food_df3.sort_values(by = 'Fiber_g',ascending =True).iloc[0]['Descrip']
    else:
        #person is below average bmi, recommend highest energy item
        return food_df3.sort_values(by="Fiber_g",ascending=False).iloc[0]['Descrip']

print(recommend_Fiber_g(food_df3,avg_bmi,8.70,80,'male'))













