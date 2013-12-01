'''
Documentation, License etc.

@package htoolkit
'''
import modules.torrific as torrific
import modules.data_mining as mining

if __name__ == '__main__':

    # inits torrific
    torrific.initialize('http://192.168.1.123:8118')

    text_data = torrific.get_url_data('http://200.238.107.82/.bashrc')

    if text_data == -1:
        exit(-1)

    print text_data

    urls = mining.get_all_urls(text_data)

    for u in urls:
        print u

    ips = mining.get_all_ips(text_data)
    for ip in ips:
        print ip
