---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-11-03
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-11-03
date_stampThisWeek: 2024-11-03
date_stampLastWeek: 2024-11-03
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
        <td>54181</td>
        <td>54126</td>
        <td style="color: #45c527" >55</td>
        <td style="color: #45c527" >0.1%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>979</td>
        <td>938</td>
        <td style="color: #45c527" >41</td>
        <td style="color: #45c527" >4.3%</td>
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
        <td>871</td>
        <td>830</td>
        <td style="color: #45c527" >41</td>
        <td style="color: #45c527" >4.8%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>197</td>
        <td>188</td>
        <td style="" >9</td>
        <td style="" >4.7%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19745</td>
        <td>19696</td>
        <td style="color: #45c527" >49</td>
        <td style="color: #45c527" >0.25%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4489</td>
        <td>4479</td>
        <td style="" >10</td>
        <td style="" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>578</td>
        <td>575</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.52%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1445</td>
        <td>1443</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.14%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1802</td>
        <td>1800</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.11%</td>
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