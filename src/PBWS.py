from bs4 import BeautifulSoup
from requests import get
import PBDB

draw_links = [i.split('\n') for i in open('Info.txt', 'r').read().split('\n\n')]

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_data(link):
    '''
    gets all bonds information on the draw with
    a link to the draw given as a arg
    '''

    all_bonds = []

    def data_format(draw_name_info):
        '''
        a function which formats the data and returns it so
        that it can add it to the database in a standerized format
        NOTE: to get a better understanding of the output see the
        draw_name_info var
        '''
        def extract_date(time):
            '''
            seprately gives a standerdized date to each draw in the
            year-month-day format
            '''
            months_info = dict(jan=1, feb=2, mar=3, apr=4, may=5,
                               jun=6, jul=7, aug=8, sep=9, oct=10,
                               nov=11, dec=12)
            return f'{time[2]}-{months_info[time[1][:3]]}-{time[0]}'

        return int(draw_name_info[3]), int(draw_name_info[1]), extract_date(draw_name_info[5:8]), draw_name_info[10][:3].upper()

    # most of the data extraction a pre processing happen
    # here and above

    raw_link_info = get(link, headers=headers)
    parsed_link_info = BeautifulSoup(raw_link_info.text, 'html.parser')

    draw_name_info = link[41:].strip().split('-')
    name_format = data_format(draw_name_info)

    [all_bonds.append((int(td.text.strip()), 1, *name_format))
     for td in parsed_link_info.find_all('td', class_='first_td')]

    [all_bonds.append((int(td.text.strip()), 2, *name_format))
     for td in parsed_link_info.find_all('td', class_='second_td')]

    [all_bonds.append((int(td.text.strip()), 3, *name_format))
     for td in parsed_link_info.find_all('td', class_='third_td')]

    return all_bonds


def get_prizebondnet(link):
    '''
    TODO:
    function which will help in verification of data
    '''
    pass


def consestincy_test(pbnet, hamweb):
    '''
    TODO:
    COMPARE PRIZEBOND.NET TO HAMARIWEB.COM DRAWS
    '''
    def compare():
        pass
    pass


def main(value_selector):
    '''
    main function which runs the program
    and allows for some user selection
    '''
    for link in draw_links[value_selector]:

        try:
            draw_results = get_data(link)

            if len(draw_results) > 100:
                PBDB.insert_data(draw_results)
                print(f'INSERTED DRAW: {link}\n')

            else:
                print(f'ERROR EXTREMELY LOW BOND COUNT: {link} NOT INSERTED\n')

        except Exception as e:
            print(f'ERROR {e}: {link} NOT INSERTED\n')

    PBDB.close()


if __name__ == '__main__':

    raw_value = input('what value bond do you want to add to the database: ')
    input_processer = {'100': 0, '200': 1, '750': 2, '1500': 3,
                       '7500': 4, '15000': 5, '25000': 6, '40000': 7}

    main(input_processer[raw_value])
