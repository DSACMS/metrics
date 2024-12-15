---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-12-15
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-12-15
date_stampThisWeek: 2024-12-15
date_stampLastWeek: 2024-12-15
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
        <td>54513</td>
        <td>54455</td>
        <td style="color: #45c527" >58</td>
        <td style="color: #45c527" >0.11%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>987</td>
        <td>985</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.2%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>108</td>
        <td>108</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>879</td>
        <td>877</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.23%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>194</td>
        <td>205</td>
        <td style="color: #45c527" >-11</td>
        <td style="color: #45c527" >5.5%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>20055</td>
        <td>19995</td>
        <td style="color: #45c527" >60</td>
        <td style="color: #45c527" >0.3%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4557</td>
        <td>4540</td>
        <td style="" >17</td>
        <td style="" >0.37%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>587</td>
        <td>586</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.17%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1462</td>
        <td>1455</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >0.48%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1882</td>
        <td>1881</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.053%</td>
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