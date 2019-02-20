import requests, sys
search_word = sys.argv[1]
api_url = 'https://ja.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
api_params['titles'] = search_word
wiki_data = requests.get(api_url, params=api_params)
fo = open('/Users/akaoshun/Desktop/study/Python/wiki/' + search_word + '.html', 'w')
fo.write(wiki_data.text)
fo.close()
