'''
Documentation, License etc.

@package htoolkit
'''
import modules.torrific as torrific
import modules.data_mining as mining

if __name__ == '__main__':

    # inits torrific
    torrific.initialize('http://192.168.1.123:8118')

    text_data = torrific.get_url_data('http://www.detran.pe.gov.br/')

    if text_data == -1:
        exit(-1)

    urls = mining.get_all_urls(text_data)

    for u in urls:
        print u
