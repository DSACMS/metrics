---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-11-24
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-11-24
date_stampThisWeek: 2024-11-24
date_stampLastWeek: 2024-11-24
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
        <td>54372</td>
        <td>54320</td>
        <td style="color: #45c527" >52</td>
        <td style="color: #45c527" >0.096%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>983</td>
        <td>982</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.1%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>106</td>
        <td>110</td>
        <td style="color: #45c527" >-4</td>
        <td style="color: #45c527" >3.7%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>877</td>
        <td>872</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.57%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>196</td>
        <td>198</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >1%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19914</td>
        <td>19863</td>
        <td style="color: #45c527" >51</td>
        <td style="color: #45c527" >0.26%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4530</td>
        <td>4511</td>
        <td style="" >19</td>
        <td style="" >0.42%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>584</td>
        <td>583</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.17%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1449</td>
        <td>1448</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.069%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1882</td>
        <td>1789</td>
        <td style="color: #45c527" >93</td>
        <td style="color: #45c527" >5.1%</td>
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
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_top_committers.svg", title: "Top Committers" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_libyear_timeline.svg", title: "Dependency Libyears" %}
  </div>
</div>