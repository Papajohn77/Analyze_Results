import json
import argparse
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

def create_request_durations_list(path, tag):
    with open(path, encoding='utf-8') as requests_file:
        request_durations = []
        for request_txt in requests_file:
            request_dict = json.loads(request_txt)
            if request_dict['metric'] == 'http_req_duration' and request_dict['type'] == 'Point' and request_dict['data']['tags']['name'] == tag:
                request_durations.append(request_dict['data']['value'])
    return request_durations

def create_boxplot(df, title, x_labels, path):
    fig, ax = plt.subplots()
    boxplot = ax.boxplot(df, 0, '')
    ax.set_ylabel('HTTP request duration (ms)')
    ax.set_xlabel('Virtual Users')
    ax.set_xticklabels(x_labels)
    ax.set_title(title)

    for median in boxplot['medians']:
        median.set(color='black')
    
    plt.savefig(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_folder')
    parser.add_argument('output_folder')
    args = parser.parse_args()

    stores_request_durations_50_vus = \
        create_request_durations_list(f'./{args.input_folder}/stores_50_vus.json', 'SearchStores')

    stores_request_durations_100_vus = \
        create_request_durations_list(f'./{args.input_folder}/stores_100_vus.json', 'SearchStores')

    stores_request_durations_200_vus = \
        create_request_durations_list(f'./{args.input_folder}/stores_200_vus.json', 'SearchStores')

    stores_request_durations = [
        stores_request_durations_50_vus,
        stores_request_durations_100_vus,
        stores_request_durations_200_vus
    ]

    create_boxplot(stores_request_durations, 
                 title='Stores', 
                 x_labels=['50', '100', '200'], 
                 path=f'./{args.output_folder}/stores_boxplots.png')
    
    with open(f'./{args.output_folder}/stores_ci.txt', 'w', encoding='utf-8') as stores_ci_file:
        stores_ci_50_vus = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(stores_request_durations_50_vus), 
            scale=st.sem(stores_request_durations_50_vus))

        stores_ci_file.write('The confidence interval of the mean response time for the /stores '
                             f'endpoint with 50 virtual users is: {stores_ci_50_vus}\n\n')
        
        stores_ci_100_vus = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(stores_request_durations_100_vus), 
            scale=st.sem(stores_request_durations_100_vus))

        stores_ci_file.write('The confidence interval of the mean response time for the /stores '
                             f'endpoint with 100 virtual users is: {stores_ci_100_vus}\n\n')
        
        stores_ci_200_vus = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(stores_request_durations_200_vus), 
            scale=st.sem(stores_request_durations_200_vus))

        stores_ci_file.write('The confidence interval of the mean response time for the /stores '
                             f'endpoint with 200 virtual users is: {stores_ci_200_vus}\n\n')
    
    products_request_durations_25_vus = \
        create_request_durations_list(f'./{args.input_folder}/products_25_vus.json', 'SearchProducts')

    products_request_durations_50_vus = \
        create_request_durations_list(f'./{args.input_folder}/products_50_vus.json', 'SearchProducts')

    products_request_durations_100_vus = \
        create_request_durations_list(f'./{args.input_folder}/products_100_vus.json', 'SearchProducts')
    
    products_request_durations = [
        products_request_durations_25_vus,
        products_request_durations_50_vus,
        products_request_durations_100_vus
    ]

    create_boxplot(products_request_durations, 
                 title='Products', 
                 x_labels=['25', '50', '100'], 
                 path=f'./{args.output_folder}/products_boxplots.png')

    with open(f'./{args.output_folder}/products_ci.txt', 'w', encoding='utf-8') as products_ci_file:
        products_ci_25_vus = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(products_request_durations_25_vus), 
            scale=st.sem(products_request_durations_25_vus))

        products_ci_file.write('The confidence interval of the mean response time for the /products '
                               f'endpoint with 25 virtual users is: {products_ci_25_vus}\n\n')
        
        products_ci_50_vus = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(products_request_durations_50_vus), 
            scale=st.sem(products_request_durations_50_vus))

        products_ci_file.write('The confidence interval of the mean response time for the /products '
                               f'endpoint with 50 virtual users is: {products_ci_50_vus}\n\n')
        
        products_ci_100_vus = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(products_request_durations_100_vus), 
            scale=st.sem(products_request_durations_100_vus))

        products_ci_file.write('The confidence interval of the mean response time for the /products '
                               f'endpoint with 100 virtual users is: {products_ci_100_vus}\n\n')
