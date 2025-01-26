---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2025-01-26
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2025-01-26
date_stampThisWeek: 2025-01-26
date_stampLastWeek: 2025-01-26
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
        <td>4412</td>
        <td>4356</td>
        <td style="color: #45c527" >56</td>
        <td style="color: #45c527" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>203</td>
        <td>201</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.99%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>110</td>
        <td>108</td>
        <td style="" >2</td>
        <td style="" >1.8%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>93</td>
        <td>93</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>47</td>
        <td>53</td>
        <td style="color: #45c527" >-6</td>
        <td style="color: #45c527" >12%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>951</td>
        <td>938</td>
        <td style="color: #45c527" >13</td>
        <td style="color: #45c527" >1.4%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>194</td>
        <td>187</td>
        <td style="" >7</td>
        <td style="" >3.7%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>25</td>
        <td>24</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >4.1%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>72</td>
        <td>70</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >2.8%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>37</td>
        <td>37</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>26</td>
        <td>26</td>
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