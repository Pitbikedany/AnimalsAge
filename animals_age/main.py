# se o gato tem 1 ano = 15 anos
# se tem 2 anos = 15 + 9 anos
# se tem mais de 2 = anos * 4 anos humanos 

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_yeats = 15
    elif human_years == 2:
        cat_years = 15 + 9 
        dog_years = 15 + 9
    elif human_years > 2:
        cat_years = 24 + (human_years-2) * 4 
        dog_years = 24 + (human_years-2 * 5)
         
    return [human_years,cat_years,dog_years]

human_years = int(input('Insira a sua idade: '))
print(human_years_cat_years_dog_years(human_years))