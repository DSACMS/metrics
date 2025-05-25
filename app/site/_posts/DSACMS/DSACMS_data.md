---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2025-05-25
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2025-05-25
date_stampThisWeek: 2025-05-25
date_stampLastWeek: 2025-05-25
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
        <td>5625</td>
        <td>5356</td>
        <td style="color: #45c527" >269</td>
        <td style="color: #45c527" >4.9%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>278</td>
        <td>265</td>
        <td style="color: #45c527" >13</td>
        <td style="color: #45c527" >4.8%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>172</td>
        <td>161</td>
        <td style="" >11</td>
        <td style="" >6.6%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>106</td>
        <td>104</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >1.9%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>92</td>
        <td>86</td>
        <td style="" >6</td>
        <td style="" >6.7%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1373</td>
        <td>1221</td>
        <td style="color: #45c527" >152</td>
        <td style="color: #45c527" >12%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>304</td>
        <td>283</td>
        <td style="" >21</td>
        <td style="" >7.2%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>45</td>
        <td>38</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >17%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>86</td>
        <td>83</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >3.6%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>38</td>
        <td>38</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>30</td>
        <td>28</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >6.9%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2 class="graph-section-title">Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_issue_gauge.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the organization. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months", modal_description: "These graphs illustrate the number of new contributors joining the organization over time. They show data for six-month intervals, providing insights into contributor growth and onboarding rates." %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_top_committers.svg", title: "Top Committers", modal_description: "This graph highlights the top contributors with the organizations, ranked by the number of commits they have made. It provides insights into the most active members driving developement efforts and their relative contributions to the organization's repositories." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_libyear_timeline.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the organization in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
  </div>
</div>