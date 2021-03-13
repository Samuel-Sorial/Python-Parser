<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
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

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Parser Using Python</h3>

  <p align="center">
    A simple parser built using python as part of a hiring process.
    <br />
    <a href="https://github.com/Samuel-Sorial/Python-Parser/issues">Report Bug</a>
    
  </p>
</p>

---

<!-- TABLE OF CONTENTS -->
<details open="open">
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
    <li><a href="#testing">Testing</a></li>
    <li><a href="#usage-instructions">Usage Instructions</a></li>
  </ol>
</details>

---

<!-- ABOUT THE PROJECT -->
<br />

## About The Project

A simple parser built using python as part of a hiring process. It supports parser data from CSV & XML to JSON. The project was built in a way that makes it easy to extend to a new format, and easy to add new features. I've decided to only use built-in modules in my task, as I wanted to show my algorithmic skills (especially in the XML Parser) alongside my software engineering skills.

### Built With

- [Python](https://www.python.org/)

<!-- GETTING STARTED -->

<br />

## Getting Started

The application is very simple, which means that initializing it won't be a big deal.

### Prerequisites

- Python3

### Installation

1. Clone the repo

```sh
git clone https://github.com/Samuel-Sorial/Python-Parser.git
```

2. Go to the clone directory

```sh
cd Python-Parser
```

   <!-- Testing -->

---

## Testing

After initializing the project from the previous section, simply run:

```sh
python3 -m unittest discover test
```

**Note:** if your default python version is python3, you can only type python instead of python3

---

<br />

<!-- DOCUMENTATION -->

## Usage Instructions

### Parse to json

```sh
python3 parser.py <format> <files>
```

- Supported formats are:
  - `CSV`
  - `XML`
- Output format: `json`

**Sample xml usage:**

```sh
python3 parser.py xml ./data/xml/customer1.xml
```

**Sample xml output:** `customer.json` file that contains:

```sh
{
  "transaction": {
    "date": "2021-12-07",
    "customer": {
      "name": "Shirish Suchak",
      "address": "1429  Joyce Street",
      "phone": "252-414-7396",
      "units": {
        "vehicle": {
          "make": "Honda",
          "vin_number": "WDBFA63E7RF125264",
          "id": "V1824"
        }
      },
      "id": "ID1011200"
    }
  },
  "file_name": "xml/customer1.xml"
}
```

---

**Sample csv usage:**

```sh
python3 parser.py csv ./data/csv/vehicles.csv
```

**Sample xml output:** `vehicles.json` file that contains:

```sh
[
  {
    "id": "V3015",
    "make": "Chevrolet",
    "vin_number": "1HGFA16548L016469",
    "owner_id": "ID9857"
  },
  {
    "id": "V2014",
    "make": "Honda",
    "vin_number": "1G6KD57Y46U180996",
    "owner_id": "ID9857"
  },
  {
    "id": "V1475",
    "make": "Ford",
    "vin_number": "2HKYF18575H574967",
    "owner_id": "ID5410"
  },
  {
    "id": "V786",
    "make": "Nissan",
    "vin_number": "2GTEK13M481177784",
    "owner_id": "ID6651"
  }
]
```
