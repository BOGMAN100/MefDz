import pandas as pd

def cheque(price_list, **kwargs):

    data = []
    
   
    for product, number in kwargs.items():
       
        if product in price_list:
           
            price = price_list[product]
           
            cost = price * number
            
            data.append({'product': product, 'price': price, 'number': number, 'cost': cost})
        else:
            print(f"Warning: {product} не найден в прайс-листе.")
    
    
    df = pd.DataFrame(data)
    
    # Сортируем DataFrame по названию продукта 
    df = df.sort_values(by='product').reset_index(drop=True)
    
    return df
    
def discount(cheque_df):
    # чтобы избежать изменения оригинала
    discounted_df = cheque_df.copy()
    
    # apply пробегает по строкам, axis = 1 указывает на строки а не столбцы
    discounted_df['cost'] = discounted_df.apply(
        lambda row: row['cost'] * 0.5 if row['number'] > 2 else row['cost'], axis=1
    )
    
    return discounted_df


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)

result = cheque(price_list, soda=3, milk=2, cream=1)
print(result, "\n", discount(result))