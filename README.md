# RSS Aggregator v0.0.1

## Instructions to run Locally

### Pre Requisites

 - Docker
 - Docker Compose

### Run

  `docker-compose -up`

  Run the following if the above command fails and retry with the above command

  `docker-compose build`

  Point browser to localhost:8000

  To run as admin login with
  ```bash
  username: admin@test.com
  password: admin
  ```

  To add Feed Sources user needs to be admin, hence its,
  recommended to login as Admin first and add source,
  click on the Admin link on the Navigation bar in the UI

  `http://www.nu.nl/rss/Algemeen`

  `https://feeds.feedburner.com/tweakers/mixed`

## CI / Test
  `docker-compose -f docker-compose-test.yml build`
  Check the output of tests and linting for the code base

## Notes

  Some parts of the app are currently designed keeping in mind this is not production or real life app
  - Docker Compose: Use mini kube / kubernetes
  - RabbitMQ: Redis would better, thinking of even cache
  - Improvments in Security: Use SSL
  - Env Variables: More use of environment variables in certain places
  - Logic: Improvements on feed parsing logic to extract images etc
  - Tests: Only ability to run and implement tests has been added. Current code coverage is limited
  - UX: Use websockets to indicate new feeds to user