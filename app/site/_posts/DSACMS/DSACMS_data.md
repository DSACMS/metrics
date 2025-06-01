---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2025-06-01
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2025-06-01
date_stampThisWeek: 2025-06-01
date_stampLastWeek: 2025-06-01
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
        <td>5701</td>
        <td>5625</td>
        <td style="color: #45c527" >76</td>
        <td style="color: #45c527" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>279</td>
        <td>278</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.36%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>173</td>
        <td>172</td>
        <td style="" >1</td>
        <td style="" >0.58%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>106</td>
        <td>106</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>108</td>
        <td>92</td>
        <td style="" >16</td>
        <td style="" >16%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1385</td>
        <td>1373</td>
        <td style="color: #45c527" >12</td>
        <td style="color: #45c527" >0.87%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>305</td>
        <td>304</td>
        <td style="" >1</td>
        <td style="" >0.33%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>46</td>
        <td>45</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >2.2%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>88</td>
        <td>86</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >2.3%</td>
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