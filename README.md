# NotifyMe

NotifyMe is a web scraper that emails you if an item on your wishlist has changed its price.

### Features
- Built with the conda package management system. See the [conda docs](https://conda.io/docs/user-guide/tasks/manage-environments.html) for initializing your own environment from the provided ```.yml```.
- Uses Scrapy to parse data from website URLs specified in ```wishlist.txt```.
- Saves the scraped data in a ```.json``` file.
- Script that runs once an hour. Compares the new data to the old and if there has been a change, send an email.

### Usage
- Initialize the venv.
- ```cd``` into ```notify-me/notifyme/notifyme/spiders```.
- Run ```scrapy crawl <spider name>``` with an instance of the ```mongod``` daemon running in a separate terminal to test the connection to MongoDB.
- Alternatively, run ```scrapy crawl <spider name> -o data.json -t json``` to save the collected data in ```data.json```.

### Todo
- Proxies
- Rotate user agents from a pool of well known ones
- Disable cookies
- Use download delays (2 or higher)
- If possible, use Google cache to fetch pages instead of getting the info directly
- Rotate IPs (Scrapoxy?)
