---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-10-02
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-10-02
date_stampThisWeek: 2024-10-02
date_stampLastWeek: 2024-10-02
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
        <td>53844</td>
        <td>53772</td>
        <td style="color: #45c527" >72</td>
        <td style="color: #45c527" >0.13%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>937</td>
        <td>937</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>111</td>
        <td>111</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>826</td>
        <td>826</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>215</td>
        <td>219</td>
        <td style="color: #45c527" >-4</td>
        <td style="color: #45c527" >1.8%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19502</td>
        <td>19445</td>
        <td style="color: #45c527" >57</td>
        <td style="color: #45c527" >0.29%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4407</td>
        <td>4384</td>
        <td style="" >23</td>
        <td style="" >0.52%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>572</td>
        <td>572</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1430</td>
        <td>1421</td>
        <td style="color: #45c527" >9</td>
        <td style="color: #45c527" >0.63%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1795</td>
        <td>1794</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.056%</td>
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
  </div>
</div>