---
layout: org-report
title: Open Source at CMS Metrics Report for Enterprise-CMCS | REPORT-2025-01-19
permalink: /Enterprise-CMCS/

org: Enterprise-CMCS
reportID: REPORT-2025-01-19
date_stampThisWeek: 2025-01-19
date_stampLastWeek: 2025-01-19
---
<div class="summary-table">
  <table class="usa-table usa-table--borderless">
    <h2> Summary Table </h2>
    <thead>
      <tr>
        <th scope="col">Metric</th>
        <th scope="col">Latest</th>
        <th scope="col">Previous</th>
        <th scope="col">Diff</th>
        <th scope="col">% Diff</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Commits</th>
        <td>31034</td>
        <td>30978</td>
        <td style="color: #45c527" >56</td>
        <td style="color: #45c527" >0.18%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>3206</td>
        <td>3206</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>314</td>
        <td>314</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>2892</td>
        <td>2892</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>218</td>
        <td>213</td>
        <td style="" >5</td>
        <td style="" >2.3%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>14350</td>
        <td>14286</td>
        <td style="color: #45c527" >64</td>
        <td style="color: #45c527" >0.45%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>3809</td>
        <td>3785</td>
        <td style="" >24</td>
        <td style="" >0.63%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>91</td>
        <td>91</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>181</td>
        <td>181</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>243</td>
        <td>243</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>30</td>
        <td>30</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2 class="graph-section-title">Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_issue_gauge.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the organization. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months", modal_description: "These graphs illustrate the number of new contributors joining the organization over time. They show data for six-month intervals, providing insights into contributor growth and onboarding rates." %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_top_committers.svg", title: "Top Committers", modal_description: "This graph highlights the top contributors with the organizations, ranked by the number of commits they have made. It provides insights into the most active members driving developement efforts and their relative contributions to the organization's repositories." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_libyear_timeline.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the organization in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
  </div>
</div>