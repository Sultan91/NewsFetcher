# NewsFetcher


## To run the app you should have docker and docker-compose installed

### After run:
`docker-compose up -d --build`

Return saved news posts from PostgreSQL:

`http://localhost:8000/posts`

`http://localhost:8000/posts?offset=10&limit=10&order=title`
