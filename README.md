<a id="readme-top"></a>



<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/alarmichanin/crypto_analyzer">
    <img src="images/logo.png" alt="Logo" width="480" height="145">
  </a>

<h3 align="center">Crypto analyzer</h3>

  <p align="center">
    Simple app to track your crypto portrofilo, receive price change notifications and smart sugestions.
    <br />
    <a href="https://github.com/alarmichanin/crypto_analyzer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alarmichanin/crypto_analyzer">View Demo</a>
    &middot;
    <a href="https://github.com/alarmichanin/crypto_analyzer/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/alarmichanin/crypto_analyzer/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Simple app to track your crypto portrofilo, receive price change notifications and smart sugestions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Flask][Flask.com]][Flask-url]
* [![React][React.com]][React-url]
* [![Tailwind][Tailwind.com]][Tailwind-url]
* [![PostgreSQL][PostgreSQL.com]][PostgreSQL-url]
* [![Redis][Redis.com]][Redis-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* pip
  ```sh
  python -m pip install --upgrade pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/alarmichanin/crypto_analyzer.git
   ```
2. Install pip packages
   ```sh
   cd api
   python -m venv .venv
   source .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Fill .env file

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Development and Deploy

1. Build app image
   ```sh
   docker-compose build
   ```
2. Start docker container(Dev)
   ```sh
   docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
3. Start docker container (Prod)
   ```sh
   docker compose -f docker-compose.yml up --build
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/alarmichanin/crypto_analyzer/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alarmichanin/crypto_analyzer" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alarmichanin/crypto_analyzer.svg?style=for-the-badge
[contributors-url]: https://github.com/alarmichanin/crypto_analyzer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alarmichanin/crypto_analyzer.svg?style=for-the-badge
[forks-url]: https://github.com/alarmichanin/crypto_analyzer/network/members
[stars-shield]: https://img.shields.io/github/stars/alarmichanin/crypto_analyzer.svg?style=for-the-badge
[stars-url]: https://github.com/alarmichanin/crypto_analyzer/stargazers
[issues-shield]: https://img.shields.io/github/issues/alarmichanin/crypto_analyzer.svg?style=for-the-badge
[issues-url]: https://github.com/alarmichanin/crypto_analyzer/issues
[license-shield]: https://img.shields.io/github/license/alarmichanin/crypto_analyzer.svg?style=for-the-badge
[license-url]: https://github.com/alarmichanin/crypto_analyzer/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/stable/ 
[React.com]: https://img.shields.io/badge/-ReactJs-61DAFB?logo=react&logoColor=white&style=for-the-badge
[React-url]: https://react.dev/ 
[PostgreSQL.com]: https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/ 
[Redis.com]: https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/ 
[Tailwind.com]: https://img.shields.io/badge/Tailwind_CSS-grey?style=for-the-badge&logo=tailwind-css&logoColor=38B2AC
[Tailwind-url]: https://tailwindcss.com/ 