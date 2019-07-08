# Django Graphs
Django Graphs is a free and open source Django application that allows collection and visualization of any kind of time series data.

![Dashboard](https://i.imgur.com/SqhgJuU.png)

**<u>Features</u>**

- Collect time series data trough a fully featured REST API courtesy of the [Django Rest Framework](https://www.django-rest-framework.org/)
- Visualize your Data using Graphs
  - Simple/Mobile view using [Chart.js](https://www.chartjs.org/)
  - Advanced view using (more data + zoom) [MetricsGraphicsjs](https://metricsgraphicsjs.org/)
- Create displays to show most recent data
- Permission System with multiple access levels
  - Secure API endpoints using either session, basic or token authentication
  - Attribute to make Graphs/Displays public
  - `Viewer` group that can only view graphs/displays
  - `User` group that can edit/delete graphs/displays/selectors/types/instances and post data
- Localization support (currently English and German available)

## Usage

The usage is pretty straight forward after understanding a few basic concepts

- `Data Entries` are created via the API. They consist of a (automatic) timestamp and a type, instance and value.
- `Types` define of which type a data entry is (Basically its name and unit).
- `Instances` are used to differentiate between data sources. For example if measuring temperature one instance could be outside and one 
- `Graph Selectors` are basically the lines of a graph. By defining a type and instance the data entries are filtered and then displayed in the graph.

Usage of the API is explained in the build in API Docs. If used from anywhere else than the API browser you basically need to supply authentication (either basic or token) and a json body containing a type, instance and value.

## Installation

The default `docker-compose.yml` is meant to run behind [Jwilder's nginx-proxy container](https://github.com/jwilder/nginx-proxy). The setup can look something like [this](https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion).

If you don't want to the `nginx-proxy` you only need to make a few changes in the `dcoker-compose.yml`.

1. Clone this repository at your desired location `git clone https://github.com/vabene1111/DjangoGraphs.git`
2. Copy `.env.template` to `.env` and fill in all required fields
3. Bring up the container by running `docker-compose up -d --build`
4. Run `sh install.sh` to populate the database and create your default user

If you want to install it without docker you can follow a tutorial like [this one](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04), note that you have to manually set the environment variables in the `.env.template` file.

### Updating

**ALWAYS** backup your database before updating!

To update using the default settings simply `git pull` and run `sh update.sh`.

Some updates might require to rebuild the container if new requirements where added.

Postgresql container updates can cause database incompatibilities. To update create a db dump before updating and import it afterwards.

## License

See `LICENSE.md` for licensing information.