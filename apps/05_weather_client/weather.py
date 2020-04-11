import requests
import bs4
import collections


WeatherReport = collections.namedtuple('WeatherReport', 'location, condition, temp')


def main():
    print_header()
    state = input('What US state do you want the weather for (e.g. CA)? ')
    city = input('What city do you want the weather for (e.g. New San Francisco)')
    html = get_html_from_web(state, city)
    report = get_weather_from_html(html)
    display_weather_report(report)


def print_header():
    print('-----------------------------')
    print('        WEATHER APP')
    print('-----------------------------')


def get_html_from_web(state, city):
    city_name_for_url = city.replace(' ', '-')
    url = f'http://www.wunderground.com/weather/us/{state}/{city_name_for_url}'
    print('Getting weather data, please wait .......')
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find('h1').get_text() \
        .replace(' Weather Conditions', '') \
        .replace('star_ratehome', '')
    condition = soup.find(class_='condition-icon').find('p').get_text()
    temp = soup.find(class_='current-temp').find(class_='wu-value wu-value-to').get_text()

    return WeatherReport(location=location, condition=condition, temp=temp)


def display_weather_report(report: WeatherReport):
    print(f'The current weather condition in {report.location} is {report.condition} '
          f'and the temperature is {report.temp} F')


if __name__ == '__main__':
    main()
