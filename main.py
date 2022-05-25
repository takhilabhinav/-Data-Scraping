import requests
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
genres=[]
dires=[]
act=[]
runtimes=[]
grosses=[]
npages=239
sns=[]
from requests import get
from bs4 import BeautifulSoup


for i in range(4000,4500,50):
    try:
        url = 'https://www.imdb.com/search/title/?title_type=feature&year=2016-01-01,2016-12-31&start='+str(i)+'&ref_=adv_nxt'
        response = requests.get(url)
        print(url)
    except:
        break
    if response.status_code != 200:
        break
    
        #print(response.text[:1500])
    
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
    #print(type(movie_containers))
    #print(len(movie_containers))
    # Extract data from individual movie container
    for container in movie_containers:
    # If the movie has Metascore, then extract:
        
        name = container.h3.a.text

            #name = container.h3.find('span', class_ = 'lister-item-header').a.text
        names.append(name)
        sno = container.h3.find('span', class_ = 'lister-item-index unbold text-primary').text
        sns.append(sno)
    # The year
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)
    # The IMDB rating
        #if container.strong!=None: 
        if container.find('span',class_='metascore')!=None:
            imdb = float(container.strong.text)
            imdb_ratings.append(imdb)
    # The Metascore
        if container.find('span', class_ = 'metascore')!=None: 
            m_score = container.find('span', class_ = 'metascore').text
            metascores.append(int(m_score))
    # The number of votes
        if container.find('span',class_='metascore')!=None:  
            vote = container.find('span', attrs = {'name':'nv'})['data-value']
            votes.append(int(vote))
    # genre
        if container.find('span', class_ = 'genre')!=None:
            #info = container.find("p", "text-muted")
            genre = container.find('span', class_ = 'genre').text
                #genre = info.find_all("span", "genre").text
            genre=genre.strip()
            genre=genre.split(',')
            genres.append(" ".join(genre))
    #cast
        #director=container.find('p',class_='').find_all('a')[0].text
        #dires.append(director)
        #act.append([a.text for a in container.find('p',class_='').find_all('a')[1:]])
        nv = container.find_all('span', attrs = {'name':'nv'})
        gross= nv[1].text if len(nv) > 1 else '-'
        grosses.append(gross)
    #runtime
        if container.find('span', class_ = 'runtime')!=None:
            runs = container.find('span', class_ = 'runtime').text
            runtimes.append(runs)
        # directors
        
            #director=container.find('p',class_='').find_all('a')[0].text
            #dires.append(director)
            try:
                actors=container.find('p',class_='').find_all('a')[1].text
                act.append(actors)
            except IndexError:
                act.append('null')
            try:
                director=container.find('p',class_='').find_all('a')[0].text
                dires.append(director)
            except IndexError:
                dires.append('null')
                
            
            
        #Actors
        
