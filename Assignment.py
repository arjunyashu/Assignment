def get_weights_of_pages(dict_of_pages, query, weights):
    weight_of_pages = {}
    weights = list(reversed(range(1,9)))
    for page_name in dict_of_pages:
        calculated_weight = 0
        for element in dict_of_pages[page_name]:
            if(element in query):
                calculated_weight+=(weights[query.index(element)]* weights[dict_of_pages[page_name].index(element)])
        weight_of_pages[page_name] = calculated_weight
    return weight_of_pages


def get_best_match_pages_list(list_of_pages_queries, max_no_key_words):
    list_of_pages = []
    list_of_queries = []
    for entry in list_of_pages_queries:
        if entry[0] == 'P':
            list_of_pages.append(entry)
        if entry[0] == 'Q':
            list_of_queries.append(entry)
    
    dict_of_pages = {}
    for entry in list_of_pages:
        page = 'P'+str(list_of_pages.index(entry)+1)
        dict_of_pages[page] = list(filter(lambda s: s!='P', entry.split(' ')))
    dict_of_queries = {}
    for entry in list_of_queries:
        page = 'Q'+str(list_of_queries.index(entry)+1)
        dict_of_queries[page] = list(filter(lambda s: s!='Q', entry.split(' ')))
    weights = list(reversed(range(1,max_no_key_words+1)))
    werghts_per_query = {}
    for q in dict_of_queries:
        temp = get_weights_of_pages(dict_of_pages, dict_of_queries[q], weights)
        werghts_per_query[q] = list(reversed(sorted(temp.items(), key=lambda x: ((x[1]), -int(x[0][1:])))))
    output_list = []   
    for question in werghts_per_query:
        temp_string = ''
        for caluclated_weights in werghts_per_query[question]:
            if caluclated_weights[1] != 0:
                temp_string+=caluclated_weights[0]+ ' '
        output_list.append(question+': ' + temp_string.strip()) 
    return output_list, werghts_per_query

    
sample_input = ['P Ford Car Review',
                'P Review Car',
                'P Review Ford',
                'P Toyota Car',
                'P Honda Car',
                'P Car',
                'Q Ford',
                'Q Car',
                'Q Review',
                'Q Ford Review',
                'Q Ford Car',
                'Q cooking French'
                ]
number_of_key_words = 8
print("Sample Input")
print(sample_input)
print("Number of key words")
print(number_of_key_words)
output_list, werghts_per_query_dict = get_best_match_pages_list(sample_input,number_of_key_words)
print(output_list)
