def human_years_cat_years_dog_years(human_years):
    dog_years = 15
    cat_years = 15
    count = 1 
    years = 1

    
    while years != human_years:
        if count == 1:
            dog_years += 9
            cat_years += 9
            count += 1
        else:
            dog_years += 5
            cat_years += 4
        years += 1
    return [human_years , cat_years , dog_years]