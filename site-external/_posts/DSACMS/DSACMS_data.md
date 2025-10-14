---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2025-06-15
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2025-06-15
date_stampThisWeek: 2025-06-15
date_stampLastWeek: 2025-06-15
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
        <td>5822</td>
        <td>5701</td>
        <td style="color: #45c527" >121</td>
        <td style="color: #45c527" >2.1%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>286</td>
        <td>279</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >2.5%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>179</td>
        <td>173</td>
        <td style="" >6</td>
        <td style="" >3.4%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>107</td>
        <td>106</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.94%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>112</td>
        <td>108</td>
        <td style="" >4</td>
        <td style="" >3.6%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1447</td>
        <td>1385</td>
        <td style="color: #45c527" >62</td>
        <td style="color: #45c527" >4.4%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>318</td>
        <td>305</td>
        <td style="" >13</td>
        <td style="" >4.2%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>50</td>
        <td>46</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >8.3%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>91</td>
        <td>88</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >3.4%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>39</td>
        <td>38</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >2.6%</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_issue_gauge.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the organization. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months", modal_description: "These graphs illustrate the number of new contributors joining the organization over time. They show data for six-month intervals, providing insights into contributor growth and onboarding rates." %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_top_committers.svg", title: "Top Committers", modal_description: "This graph highlights the top contributors with the organizations, ranked by the number of commits they have made. It provides insights into the most active members driving developement efforts and their relative contributions to the organization's repositories." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_libyear_timeline.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the organization in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
  </div>
</div>