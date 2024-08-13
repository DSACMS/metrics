# CMS Repository Metrics Website
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/DSACMS/metrics/badge)](https://securityscorecards.dev/viewer/?uri=github.com/DSACMS/metrics)

## About the Project
The CMS Repository Metrics Website shows an overview of software development activity across open source projects within a specified organization. This webpage is meant to be used by developers and program managers interested in repository health within CMS open source projects.

### Project Vision
A metrics website that automatically pulls GitHub Repository data each week to produce numerical statistics and visualizations to aid developers and PMs in monitoring project health.

## Core Team
An up-to-date list of core team members can be found in [MAINTAINERS.md](MAINTAINERS.md).

## Documentation Index 
- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [MAINTAINERS.md](./MAINTAINERS.md)
- [CODEOWNERS.md](./CODEOWNERS.md)
- [COMMUNITY_GUIDELINES.md](./COMMUNITY_GUIDELINES.md)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- [SECURITY.md](./SECURITY.md)
- [LICENSE](./LICENSE)
- [Documentation](docs/Main.md)

## Repository Structure
<!-- TODO: Using the "tree -d" command can be a helpful way to generate this information, but, be sure to update it as the project evolves and changes over time.-->
```
├── app
│   ├── dist
│   ├── node_modules
│   ├── site
│   └── src
├── scripts
│   ├── _metadata
│   ├── metricsLib
│   └── tests
└── templates
```

# Development and Software Delivery Lifecycle 

The following guide is for members of the project team who have access to the repository as well as code contributors. The main difference between internal and external contributions is that external contributors will need to fork the project and will not be able to merge their own pull requests. For more information on contribributing, see: [CONTRIBUTING.md](./CONTRIBUTING.md).

## Local Development

### Getting Started

To collect metrics, first make sure you have set the following environment variables:
    - GITHUB_TOKEN - The github api key that you are using to collect data
    - AUGUR_HOST - The api domain corresponding to an instance of [CHAOSS/Augur](https://github.com/chaoss/augur/)

Then, install the dependencies in requirements.txt.

Once the env is set up, either run the 'update data' GitHub Action in `.github/workflows/update_data.yml` or execute the `update.sh` shell script.

To run the server, make sure that your computer has npm installed.
Once npm is installed run `npm install` and `npm start` in the app/ directory.

### Installation

1. Clone the repo

    `git clone https://github.com/DSACMS/metrics.git`

2. Install the required packages in requirements.txt (preferably in a virtual env)

    `pip3 install -r requirements.txt`
    
3. Install node dependencies

    `cd app && npm install && cd ..`

## Coding Style and Linters

This project adheres to PEP8 rules and guidelines whenever possible when accepting
new contributions of Python code. Although, there are good reasons to ignore particular guidelines
in particular situations. Further information on PEP8 can be found [here.](https://peps.python.org/pep-0008/)

This project utilizes pylint as the primary linter for backend code, while eslint and prettier handle code formatting and linting for the frontend. Checks are implemented upon new pull requests into protected branches to ensure code quality and consistency.

Python code quality checks are extremely useful for lowering the
cost of maintenence of Python projects. Further information on Pylint can be found [here.](https://pylint.readthedocs.io/en/latest/)

## Branching Model

We follow the [GitHub Flow Workflow](https://guides.github.com/introduction/flow/)

1.  Fork the project 
2.  Check out the `main` branch 
3.  Create a feature branch
4.  Write code and tests for your change 
5.  From your branch, make a pull request against `dev` if you have a feature change and `main` if it is a hotfix 
6.  Work with repo maintainers to get your change reviewed and resolve git history if needed
7.  Wait for your change to be pulled into `dev` and later released into `main`
8.  Delete your feature branch

This project follows [trunk-based development](https://trunkbaseddevelopment.com/), which means:

* Make small changes in [short-lived feature branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/) and merge to `dev` frequently.
* Be open to submitting multiple small pull requests for a single ticket (i.e. reference the same ticket across multiple pull requests).
* Treat each change you merge to `dev` and `main` as immediately deployable to production. Do not merge changes that depend on subsequent changes you plan to make, even if you plan to make those changes shortly.
* Ticket any unfinished or partially finished work.
* Tests should be written for changes introduced, and adhere to the text percentage threshold determined by the project.

This project uses **continuous deployment** using [Github Actions](https://github.com/features/actions) which is configured in the [./github/worfklows](.github/workflows) directory.

Pull-requests are merged to `main` and the changes are immediately deployed to the development environment. Releases are created to push changes to production.

## Contributing

Thank you for considering contributing to an Open Source project of the US Government! For more information about our contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Codeowners

The contents of this repository are managed by the CMS Open Source Program Office. Those responsible for the code and documentation in this repository can be found in [CODEOWNERS.md](CODEOWNERS.md).

## Community

The CMS Repository Metrics Website team is taking a community-first and open source approach to the product development of this tool. We believe government software should be made in the open and be built and licensed such that anyone can download the code, run it themselves without paying money to third parties or using proprietary software, and use it as they will.

We know that we can learn from a wide variety of communities, including those who will use or will be impacted by the tool, who are experts in technology, or who have experience with similar technologies deployed in other spaces. We are dedicated to creating forums for continuous conversation and feedback to help shape the design and development of the tool.

We also recognize capacity building as a key part of involving a diverse open source community. We are doing our best to use accessible language, provide technical and process documents, and offer support to community members with a wide variety of backgrounds and skillsets. 

### Community Guidelines

Principles and guidelines for participating in our open source community are can be found in [COMMUNITY_GUIDELINES.md](COMMUNITY_GUIDELINES.md). Please read them before joining or starting a conversation in this repo or one of the channels listed below. All community members and participants are expected to adhere to the community guidelines and code of conduct when participating in community spaces including: code repositories, communication channels and venues, and events. 

## Feedback

If you have ideas for how we can improve or add to our capacity building efforts and methods for welcoming people into our community, please let us know at opensource@cms.hhs.gov. If you would like to comment on the tool itself, please let us know by [filing an issue on our GitHub repository](https://github.com/DSACMS/metrics/issues/new).

## Policies

### Open Source Policy

We adhere to the [CMS Open Source
Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any
questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

*Submit a vulnerability:* Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

For more information about our Security, Vulnerability, and Responsible Disclosure Policies, see [SECURITY.md](SECURITY.md).

## Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.