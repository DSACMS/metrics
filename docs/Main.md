# Metrics
This project defines a static GitHub Pages website that populates itself from a GitHub repository that holds data.
The data is fetched by a python program defined in the scripts/ directory. Both the frontend website and the program
that gathers the needed data are run at regular intervals via GitHub action. 

The frontend is built using Eleventy.


# General Update Process

The backend update process looks like this:
    1. Fetch all JSON data for orgs and repositories, overwriting existing data.
    2. Generate reports based on that data gathered, seperating the previous from the next.
    3. Write reports to file given the desired format defined in a markdown file in templates/
    4. Generate graphs based on the data gathered using PyGals python library
    5. Write graphs to file for use in the frontend

Relevant: https://www.markdownguide.org/extended-syntax/


# Website Home Page

Standard landing page. You can click to repository or organization based metrics from the two buttons shown.

# Repo Page

Shows various weekly statistics by repo when the user scrolls down the page. The top of the page shows a 
markdown table populated with the below raw counts compared to the last values from when it was run last:

- Commits
- Issues 
- Open Issues
- Closed Issues
- Pull Requests
- Open Pull Requests
- Merged Pull Requests
- Closed Pull Requests
- Forks
- Stars
- Watchers

The rest of the page have the more complex metrics shown. See [ListOfMetrics.md](ListOfMetrics.md) for a 
complete list. 

# Org Page

The org page is much the same as the repo page but instead it shows organization specific metrics. Below are
the raw counts measured in the org page of the repository:

- Commits
- Issues 
- Open Issues
- Closed Issues
- Pull Requests
- Open Pull Requests
- Merged Pull Requests
- Closed Pull Requests
- Forks
- Stars
- Watchers
- Followers

The rest of the page have the more complex metrics shown. See [ListOfMetrics.md](ListOfMetrics.md) for a 
complete list. 
