---
layout: org-report
title: Open Source at CMS Metrics Report for Enterprise-CMCS | REPORT-2025-03-16
permalink: /Enterprise-CMCS/

org: Enterprise-CMCS
reportID: REPORT-2025-03-16
date_stampThisWeek: 2025-03-16
date_stampLastWeek: 2025-03-16
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
        <td>31590</td>
        <td>31438</td>
        <td style="color: #45c527" >152</td>
        <td style="color: #45c527" >0.48%</td>
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
        <td>180</td>
        <td>196</td>
        <td style="color: #45c527" >-16</td>
        <td style="color: #45c527" >8.5%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>14910</td>
        <td>14767</td>
        <td style="color: #45c527" >143</td>
        <td style="color: #45c527" >0.96%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4160</td>
        <td>4101</td>
        <td style="" >59</td>
        <td style="" >1.4%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>96</td>
        <td>93</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >3.2%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>184</td>
        <td>183</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.54%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>235</td>
        <td>241</td>
        <td style="color: #d31c08" >-6</td>
        <td style="color: #d31c08" >2.5%</td>
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