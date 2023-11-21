<!--- # NOTE: Modify sections marked with `TODO` and then rename the file.-->

# Metrics Dashboard for CMS Open Source Projects
The Metrics Dashboard webpage shows a weekly and monthly overview across open source projects within a specified organization. This webpage is meant to be used by developers and program managers interested in strategy and web presence within CMS open source projects

## Getting Started
To collect metrics, first make sure you have set the following environment variables:
    - GITHUB_TOKEN - The github api key that you are using to collect data
    - AUGUR_HOST - The api domain corresponding to an instance of [CHAOSS/Augur](https://github.com/chaoss/augur/)

Then, install the dependencies in requirements.txt.

Once the env is set up, either run the 'update data' GitHub Action in .github/workflows/update_data.yml or execute the update.sh shell
script.


To run the server, make sure that your computer has npm installed.
Once npm is installed run `npm install` and `npm start` in the app/ directory.

### Project Vision
A metrics web page that automatically pulls github repo data each week to produce numerical and visual statistics to aid developers and PMs in monitoring project health. 

### Project Information
<!-- Example Innersource Project Info
 * [Project Website](https://cms.gov/digital-service-cms)
 * [Project Documentation:](https://confluence.cms.gov/)
 * [Project Sprint/Roadmap:](https://jira.cms.gov/)
 * [Project Slack Channel:](https://cmsgov.slack.com/archives/XXXXXXXXXX)
 * [Project Tools/Hosting/Deployment:](https://confluence.cms.gov)
 * Project Keyword(s) for Search: KEYWORD1, KEYWORD2
 * Project Members:
    * Team Lead: Remy
    * Fullstack intern: Nicole
    * Fullstack intern: Shweta
    PO, Delivery Lead, Approvers, Trusted Committers etc.
-->

<!-- Example Open Source Info
 * [Project Website](https://cms.gov/digital-service-cms)
 * [Project Documentation:](https://confluence.cms.gov/)
 * Public Contact: opensource@cms.hhs.gov (**NOTE: Do not use individual/personal email addresses**)
 * Follow [@CMSgov](https://twitter.com/cmsgov) on Twitter for updates.
-->

### Installation

1. Clone the repo

    `git clone https://github.com/DSACMS/metrics.git`

2. Install the required packages in requirements.txt (preferably in a virtual env)

    `pip3 install -r requirements.txt`
    

3. Install node dependencies

    `cd app && npm install && cd ..`

## Contributing

Thank you for considering contributing to an Open Source project of the US
Government! For more information about our contribution guidelines, see
[CONTRIBUTING.md](CONTRIBUTING.md)

## Security

For more information about our Security, Vulnerability, and Responsible
Disclosure Policies, see [SECURITY.md](SECURITY.md).

## Authors and Maintainers

For more information about our Authors and maintainers, see [MAINTAINERS.md](MAINTAINERS.md).
A full list of contributors can be found on [https://github.cms.gov/$USERNAME/$REPONAME/graphs/contributors](https://github.cms.gov/$USERNAME/$REPONAME/graphs/contributors).

## Public domain

This project is licensed within in the public domain within the United States,
and copyright and related rights in the work worldwide are waived through the
[CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0 dedication. By
submitting a pull request or issue, you are agreeing to comply with this waiver
of copyright interest.
