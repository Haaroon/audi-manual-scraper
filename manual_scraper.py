import requests
import shutil


referer = 'http://bordbuch-online.audi.de/AudiBordbuch/docs/xxxxxxxx-xxx-xxxxx/100/' # e.g http://bordbuch-online.audi.de/AudiBordbuch/docs/xxxx-xx-xxxxx'
uni = 'xXXXXXXXXXXXX' # e.g. some numbers
url =  'http://bordbuch-online.audi.de/AudiBordbuch/docs/xxxxxxxx-xxx-xxxxx/files/assets/common/page-html5-substrates/page' # e.g. 'http://bordbuch-online.audi.de/AudiBordbuch/docs/xxx-xxx-xxxxxxx-xxxxx/files/assets/common/page-html5-substrates/page'
min_page = 1
max_page = 412
write_path = 'manual'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'image/webp,*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': '',
    'DNT': '1',
    'Connection': 'keep-alive',
}

params = (
    ('uni', ''),
)


def page_num_converter(page_num):
    as_str = str(page_num)
    if len(as_str) < 4:
        current_len = len(as_str)
        max_len = 4
        for i in range(current_len, max_len, 1):
            as_str = '0'+as_str
    return as_str


def scrape(min_page,max_page, save_path):
    page_numbers = range(min_page, max_page+1, 1)
    errors = []
    for i in page_numbers:
        print('Page %i/%i' % (i, max_page))
        page_num = page_num_converter(i)
        response = requests.get(url+page_num+'_4.jpg', headers=headers, params=params, stream=True)
        if response.status_code != 200:
            print('Error with page %i' % i)
            errors.append(i)
        elif response.status_code == 200:
            file_name = page_num+'.jpg'
            with open(save_path+'/'+file_name, 'wb') as f:
                for chunk in response:
                    f.write(chunk)
        else:
            print('Error: Status code %i' % i)
            errors.append(i)
    return errors


def convert_to_pdf():
    pass

errors = scrape(min_page,max_page, write_path)
convert_to_pdf()

# TODO Download manual index
# TODO Convert into PDF
# TODO Index pdf
