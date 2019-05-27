def scrape():

# Dependencies
    from bs4 import BeautifulSoup
    from splinter import Browser
    import requests
    import pandas as pd

#Variables
    count = 0

#Open a new browser window
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

# MARS NEWS-------------------------------------------------------------------------------------

# URL of NASA Mars News Site 
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

#Initiating Web Scrapping...
    html = browser.html
# Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all elements that contain news info
    results = soup.find('div', class_='image_and_description_container')

    for r in results:
            if count == 1:
                break
            else:
                count = count + 1
                title = r.find('div', class_='bottom_gradient')
                news_title = title.find('h3').text
                news_p = r.find('div', class_='rollover_description_inner').text

    count = 0

# JPL--------------------------------------------------------------------------------------------

# URL of JPL Featured Space Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

#Initiating Web Scrapping...
    html = browser.html
# Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve the element with the link to the image (full image)
    results_jpl = soup.find_all('a', class_='button fancybox')

#We search into the <a> tag where is the link to the featured image
    for link in results_jpl:
        url_inc = link.get('data-fancybox-href')

#Forming the complete url to the image
    featured_image_url = 'https://www.jpl.nasa.gov' + url_inc

# TWITTER -----------------------------------------------------------------------------------------

# URL of Twitter Mars Weather Account
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

#Initiating Web Scrapping...
    html = browser.html
# Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve the element with the link to the image (full image)
    result_tw = soup.find('div', class_='js-tweet-text-container')
    twit = result_tw.find('p').text

    mars_weather = twit

# MARS FACTS ---------------------------------------------------------------------------------------

# URL of Mars Facts site
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

#Initiating Web Scrapping...
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('table', class_='tablepress tablepress-id-mars')

#Scrapping the data of the table
    for r in results:
    
            row1 = r.find('tr', class_='row-1 odd')
            col1_r1 = row1.find('td', class_='column-1').text
            col2_r1 = row1.find('td', class_='column-2').text

            row2 = r.find('tr', class_='row-2 even')
            col1_r2 = row2.find('td', class_='column-1').text
            col2_r2 = row2.find('td', class_='column-2').text
    
            row3 = r.find('tr', class_='row-3 odd')
            col1_r3 = row3.find('td', class_='column-1').text
            col2_r3 = row3.find('td', class_='column-2').text
    
            row4 = r.find('tr', class_='row-4 even')
            col1_r4 = row4.find('td', class_='column-1').text
            col2_r4 = row4.find('td', class_='column-2').text
    
            row5 = r.find('tr', class_='row-5 odd')
            col1_r5 = row5.find('td', class_='column-1').text
            col2_r5 = row5.find('td', class_='column-2').text
    
            row6 = r.find('tr', class_='row-6 even')
            col1_r6 = row6.find('td', class_='column-1').text
            col2_r6 = row6.find('td', class_='column-2').text
    
            row7 = r.find('tr', class_='row-7 odd')
            col1_r7 = row7.find('td', class_='column-1').text
            col2_r7 = row7.find('td', class_='column-2').text

            row8 = r.find('tr', class_='row-8 even')
            col1_r8 = row8.find('td', class_='column-1').text
            col2_r8 = row8.find('td', class_='column-2').text
    
            row9= r.find('tr', class_='row-9 odd')
            col1_r9 = row9.find('td', class_='column-1').text
            col2_r9 = row9.find('td', class_='column-2').text

# Structure of the table 
    data = [[col1_r1, col2_r1], 
            [col1_r2, col2_r2], 
            [col1_r3, col2_r3], 
            [col1_r4, col2_r4], 
            [col1_r5, col2_r5], 
            [col1_r6, col2_r6], 
            [col1_r7, col2_r7], 
            [col1_r8, col2_r8], 
            [col1_r9, col2_r9]]

# Dataframe with the table 
    df = pd.DataFrame(data, columns = ['Description', 'Data']) 
# Converting the data to a HTML table string
    result_html = df.to_html()
    df.to_html('mars_planet_profile.html')

# MARS HEMISPHERES

#Creating the dictionary with the info of hemispheres
    hemisphere_image_urls = [{"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
                            {"title": "Syrtis Major Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
                            {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
                            {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"}
                            ]

    scraped_data = [{"news_title": news_title, "news_p": news_p, "featured_image_url": featured_image_url, "mars_weather": mars_weather, 
                "Mars_Facts": result_html,"hemispheres_images": hemisphere_image_urls}]


    return(scraped_data)