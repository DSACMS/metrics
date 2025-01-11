---
layout: org-report
title: Open Source at CMS Metrics Report for measureauthoringtool | REPORT-2025-01-11
permalink: /measureauthoringtool/

org: measureauthoringtool
reportID: REPORT-2025-01-11
date_stampThisWeek: 2025-01-11
date_stampLastWeek: 2025-01-11
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
        <td>45094</td>
        <td>44898</td>
        <td style="color: #45c527" >196</td>
        <td style="color: #45c527" >0.44%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>145</td>
        <td>145</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>26</td>
        <td>26</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>119</td>
        <td>119</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>625</td>
        <td>611</td>
        <td style="" >14</td>
        <td style="" >2.3%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>10170</td>
        <td>10100</td>
        <td style="color: #45c527" >70</td>
        <td style="color: #45c527" >0.69%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4078</td>
        <td>4074</td>
        <td style="" >4</td>
        <td style="" >0.098%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>197</td>
        <td>197</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>185</td>
        <td>185</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>530</td>
        <td>530</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>17</td>
        <td>17</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/measureauthoringtool_issue_gauge.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the organization. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/measureauthoringtool_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months", modal_description: "These graphs illustrate the number of new contributors joining the organization over time. They show data for six-month intervals, providing insights into contributor growth and onboarding rates." %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/measureauthoringtool_top_committers.svg", title: "Top Committers", modal_description: "This graph highlights the top contributors with the organizations, ranked by the number of commits they have made. It provides insights into the most active members driving developement efforts and their relative contributions to the organization's repositories." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/measureauthoringtool_libyear_timeline.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the organization in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
  </div>
</div>