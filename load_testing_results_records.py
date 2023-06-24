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
    ax.set_xlabel('Number of Stores records')
    ax.set_xticklabels(x_labels)
    ax.set_title(title)

    for median in boxplot['medians']:
        median.set(color='black')
    
    plt.savefig(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_folder_50k')
    parser.add_argument('input_folder_100k')
    parser.add_argument('input_folder_full')
    parser.add_argument('output_folder_stores')
    parser.add_argument('output_folder_products')
    parser.add_argument('num_of_vus_stores')
    parser.add_argument('num_of_vus_products')
    args = parser.parse_args()

    stores_request_durations_50k = \
        create_request_durations_list(f'./{args.input_folder_50k}/stores_{args.num_of_vus_stores}_vus.json', 'SearchStores')

    stores_request_durations_100k = \
        create_request_durations_list(f'./{args.input_folder_100k}/stores_{args.num_of_vus_stores}_vus.json', 'SearchStores')

    stores_request_durations_full = \
        create_request_durations_list(f'./{args.input_folder_full}/stores_{args.num_of_vus_stores}_vus.json', 'SearchStores')

    stores_request_durations = [
        stores_request_durations_50k,
        stores_request_durations_100k,
        stores_request_durations_full
    ]

    create_boxplot(stores_request_durations, 
                 title='Stores', 
                 x_labels=['50k', '100k', '145k'], 
                 path=f'./{args.output_folder_stores}/stores_boxplots.png')
    
    with open(f'./{args.output_folder_stores}/stores_ci.txt', 'w', encoding='utf-8') as stores_ci_file:
        stores_ci_50k = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(stores_request_durations_50k), 
            scale=st.sem(stores_request_durations_50k))

        stores_ci_file.write('The confidence interval of the mean response time for the /stores '
                             f'endpoint with 50k Stores is: {stores_ci_50k}\n\n')
        
        stores_ci_100k = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(stores_request_durations_100k), 
            scale=st.sem(stores_request_durations_100k))

        stores_ci_file.write('The confidence interval of the mean response time for the /stores '
                             f'endpoint with 100k Stores is: {stores_ci_100k}\n\n')
        
        stores_ci_full = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(stores_request_durations_full), 
            scale=st.sem(stores_request_durations_full))

        stores_ci_file.write('The confidence interval of the mean response time for the /stores '
                             f'endpoint with 145k Stores is: {stores_ci_full}\n\n')
    
    products_request_durations_50k = \
        create_request_durations_list(f'./{args.input_folder_50k}/products_{args.num_of_vus_products}_vus.json', 'SearchProducts')

    products_request_durations_100k = \
        create_request_durations_list(f'./{args.input_folder_100k}/products_{args.num_of_vus_products}_vus.json', 'SearchProducts')

    products_request_durations_full = \
        create_request_durations_list(f'./{args.input_folder_full}/products_{args.num_of_vus_products}_vus.json', 'SearchProducts')
    
    products_request_durations = [
        products_request_durations_50k,
        products_request_durations_100k,
        products_request_durations_full
    ]

    create_boxplot(products_request_durations, 
                 title='Products', 
                 x_labels=['25', '50', '100'], 
                 path=f'./{args.output_folder_products}/products_boxplots.png')

    with open(f'./{args.output_folder_products}/products_ci.txt', 'w', encoding='utf-8') as products_ci_file:
        products_ci_50k = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(products_request_durations_50k), 
            scale=st.sem(products_request_durations_50k))

        products_ci_file.write('The confidence interval of the mean response time for the /products '
                               f'endpoint with 50k Stores is: {products_ci_50k}\n\n')
        
        products_ci_100k = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(products_request_durations_100k), 
            scale=st.sem(products_request_durations_100k))

        products_ci_file.write('The confidence interval of the mean response time for the /products '
                               f'endpoint with 100k Stores is: {products_ci_100k}\n\n')
        
        products_ci_full = st.norm.interval(
            confidence=0.95, 
            loc=np.mean(products_request_durations_full), 
            scale=st.sem(products_request_durations_full))

        products_ci_file.write('The confidence interval of the mean response time for the /products '
                               f'endpoint with 145k Stores is: {products_ci_full}\n\n')
