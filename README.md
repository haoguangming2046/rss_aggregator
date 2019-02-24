# RSS Aggregator v0.1

## Instructions to run Locally

### Pre Requisites

 - Docker
 - Docker Compose

### Run

`docker-compose -up`

  Point browser to localhost:8000

  To run as admin login with
  ```bash
  admin@test.com
  admin
  ```

  To add Feed Sources user needs to be admin, hence its,
  recommended to login as Admin first and add source,
  click on the Admin link on the Navigation bar in the UI

  `http://www.nu.nl/rss/Algemeen`
  `https://feeds.feedburner.com/tweakers/mixed`

## Notes

  Some parts of the app are currently designed keeping in mind this is not production or real life app
  - Docker Compose and not mini kube / kubernetes
  - RabbitMQ: Redis would better, thinking of even cache
  - Websockets: To indicate new feeds to user
  - Pagination: Getting results in pieces / lazy loading
  - Improvments in Security: Use SSL
  - More use of environment variables in certain places
  - Improvements on feed parsing logic to extract images etc
