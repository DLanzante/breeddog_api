<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">This is not only a README Template but this is my Code Repo as well!
  <br />
    <a href="https://github.com/DLanzante/breeddog_api/"><strong>Explore My Code »</strong></a>
    <br /></h3>

  <p align="center">
    This is an awesome README template to jumpstart your projects! I would recommend this to anyone starting github projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Specification
You should build a new Django Application with two API endpoints. The first endpoint allows an end user to create a new Dog model by making a POST to /api/dogs, view current dogs that have been saved to the server before by making a GET to /api/dogs, and get, modify, or delete an existing Dog record by making a GET, PUT, or DELETE request (respectively) to /api/dogs/<id> where <id> is the id of the Dog record to be retrieved, modified, or deleted. Since a Dog includes a foreign key to the breed, you also need to make the same type of endpoints for dog breed at /api/breeds/ and /api/breeds/<id>.

Dog model
A dog should contain the following fields:

1. name (a character string)
2. age (an integer)
3. breed (a foreign key to the Breed Model)
4. gender (a character string)
5. color (a character string)
6. favoritefood (a character string)
7. favoritetoy (a character string)

Breed Model
A breed should contain the following fields:

1. name (a character string)
2. size (a character string) [should accept Tiny, Small, Medium, Large]
3. friendliness (an integer field) [should accept values from 1-5]
4. trainability (an integer field) [should accept values from 1-5]
5. sheddingamount (an integer field) [should accept values from 1-5]
6. exerciseneeds (an integer field) [should accept values from 1-5]

Todo List
To do this, do the following:

- track all of your changes using github.
- create a new repository on github following these instructions: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repositoryLinks to an external site.
- Using a local file folder, call git init
- in that folder create a new django server like we did in the labs
- create a new app in your django server called dogapi
- add a Dog and Breed models to models.py
- migrate your database to include tables for Dog and Breed

Do one of the following:

- Use class-based views
add two class-based API view controllers for handling Dog REST endpoints to controllers.py
call one DogDetail and one DogList to conform to best practice nomenclature
The DogDetail class should have three methods named get, put, delete
The DogList class should have two methods named get and post
refer to http://www.django-rest-framework.org/tutorial/3-class-based-views/Links to an external site. for examples

- OR
add a two class-based API view controllers for handling Breed REST endpoints to controllers.py
call one BreedDetail and one BreedList to conform to best practice nomenclature
The BreedDetail class should have three methods named get, put, delete
The BreedList class should have two methods named get and post
refer to http://www.django-rest-framework.org/tutorial/3-class-based-views/Links to an external site. for examples
use viewsets (one for breed and one for dogs)
This is probably the best (and easiest approach)

In either case:

> add the appropriate url patterns to the urls.py file to accept all of the patterns and map them to the correct controller

> test your endpoints with POSTMAN, taking screenshots of each type of request. There should be 5 requests total for each type of model, for a total of 10 tests and screenshots.

> GET (list), POST to /api/dogs/

> GET, PUT, DELETE to /api/dogs/<id>

> GET (list), POST to /api/breeds/

> GET, PUT, DELETE to /api/breeds/<id>

10 bonus points: Commit your code and save the version number (make sure to link to this commit in your submission below). Now rework your API to use the other type of (class based views or viewsets). Save your changes and provide an additional link to your repository state using the alternative approach.

### Top contributors:

<a href="https://github.com/othneildrew/Best-README-Template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=othneildrew/Best-README-Template" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [](https://github.com/DLanzante/breeddog_api) - DLanzante Github Repo

Project Link: [https://github.com/DLanzante/breeddog_api]([https://github.com/DLanzante/breeddog_api])

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
