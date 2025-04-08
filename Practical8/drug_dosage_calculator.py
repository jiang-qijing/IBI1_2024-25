def drug_dosage_calculator(weight,strength):
    if strength=='120mg/5ml':
        strength=24
    elif strength=='250mg/5ml':
        strength=50
    else:
        print('Strength must be either 120mg/5ml or 250mg/5ml')
        return None
    if weight<10 or weight>100:
        print('Weight must be between 10 and 100 kg.')
        return None
    drug_amount=15*weight
    drug_dosage=drug_amount/strength
    return drug_dosage
weight=50
strength='120mg/5ml'
drug_dosage=drug_dosage_calculator(weight,strength)
if drug_dosage is not None:
    print(f'Volume of paracetamol required is {drug_dosage} ml.')
